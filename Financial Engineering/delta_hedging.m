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
op_t=20/T;
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
%% delta
T1 = op_t + 1;
delta = zeros(T1, NS);
cost = zeros(T1, NS);
cum_cost = zeros(T1, NS);

for j = 1:NS
    for i = 1:T1
        d1 = (log(S(i,j)/K) + (r+0.5*(sigma^2))*(T1-i)*dt) / (sigma*sqrt((T1-i)*dt));
        delta(i, j) = normcdf(d1);

        if i == 1
            cost(i, j) = delta(i, j)*num_call*S(i,j);
            cum_cost(i, j) = cost(i, j);
        else
            cost(i,j) = S(i,j) * (delta(i,j)-delta((i-1),j)) * num_call;
            cum_cost(i,j) = cum_cost((i-1),j) + cost(i,j) + cum_cost((i-1),j)*(r*dt);
        end

        if i == T1
            if S(i, j) > K
                cum_cost(i, j) = cum_cost(i, j) - K*num_call;
            end
        end
    end
end
%% Performance of delta hedging
[Call, Put] = blsprice(S0, K, r, (op_t/N), sigma);
Performance = std(cum_cost(T1,:))/240000;
Performance
