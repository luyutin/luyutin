clear;
%% Parameters
T = 0.25; % week
N = 52;
dt = T/N; 

mu = 0.13;
sigma = 0.2;
S0 = 49;
K = 50;
r = 0.05;
num_call = 100000;

NS = 1000; % 10000, 100000
op_t = 20/T;
%% building Stock Price Pace
ds = zeros(op_t, NS);
dz = randn(op_t,NS)*sqrt(dt);
S = zeros(op_t+1, NS);

for j = 1:NS
    S(1, j) = S0;
    for i = 1:op_t
        ds = S(i, j)*(mu*dt + sigma*dz(i, j));
        S(i+1, j) = ds + S(i, j);
    end
end
%% Stop Loss Strategy
T1 = op_t + 1;
cost = zeros(T1, NS);
cum_cost = zeros(T1, NS);

for j = 1:NS
    for i = 2:T1
        if S(i, j) > 50 && S(i-1, j) <= 50
            cost(i, j) = S(i,j)*num_call + cost(i-1, j);
        elseif S(i, j) < 50 && S(i-1, j) >= 50
            cost(i, j) = -S(i,j)*num_call + cost(i-1, j);
        else
            cost(i, j) = 0 + cost(i-1, j);
        end
        
        if i == T1
            if S(i, j) > K
                cost(i, j) = cost(i, j) - K*num_call;
            end
        end
    end
end
%% Performance of delta hedging
[Call, Put] = blsprice(S0, K, r, (op_t/N), sigma);
Performance = std(cost(T1,:))/240000;
Performance
