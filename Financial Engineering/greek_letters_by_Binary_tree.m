clear;
%% Parameters
S0 = 50;
sigma = 0.3;
K = 52;
T = 2;
r = 0.05;
q = 0;
NT = T*252;

dt = T/NT;
u = exp(sigma*sqrt(dt));
d = 1/u;
a = exp((r-q)*dt);
p = (a-d)/(u-d);

%% stock Price
Su = S0*u;
Sd = S0*d;
Suu = Su*u;
Sdd = Sd*d;

%% 運用binomial model 計算 Put price
f = zeros(NT+1, NT+1);
% Put Price at maturity
for j = 0:NT
    f(NT+1, j+1) = max(K - S0*(u^j)*(d^(NT-j)), 0);
end
%backward induction
for i = (NT-1):-1:0
    for j = 0:i
    % Put European
        EV = 0; %Put European 提早履約價值 = 0
        f(i+1, j+1) = max(EV, exp(-r*dt)*(p*f(i+2, j+2)+(1-p)*f(i+2, j+1)));
    end
end
%% 當sigma變動0.0001
sigma_v = 0.3001;

u_v = exp(sigma_v*sqrt(dt));
d_v = 1/u_v;
p_v = (a-d_v)/(u_v-d_v);
f_v = zeros(NT+1,NT+1);

for j = 0:NT
    f_v(NT+1,j+1) = max(K-S0*(u_v^j)*(d_v^(NT-j)),0);
end

for i = (NT-1):-1:0
    for j = 0:i
        f_v(i+1,j+1) = exp(-r*dt)*(p_v*f_v(i+2,j+2)+(1-p_v)*f_v(i+2,j+1));
    end
end
%% 當r變動0.0001
r_r = 0.0501;

a_r = exp((r_r-q)*dt);
p_r = (a_r-d)/(u-d);
f_r = zeros(NT+1,NT+1);

for j = 0:NT
    f_r(NT+1,j+1) = max(K-S0*(u^j)*(d^(NT-j)),0);
end

for i = (NT-1):-1:0
    for j = 0:i
        f_r(i+1,j+1) = exp(-r_r*dt)*(p_r*f_r(i+2,j+2)+(1-p_r)*f_r(i+2,j+1));
    end
end
%% caculation
delta = (f(2,2)-f(2,1))/(Su-Sd);
gamma = ((f(3,3)-f(3,2))/(Suu-S0)-(f(3,2)-f(3,1))/(S0-Sdd))/(0.5*(Suu-Sdd));
theta = (f(3,2)-f(1,1))/(2*dt);
vega = (f_v(1,1)-f(1,1))*10000;
rho = (f_r(1,1)-f(1,1))*10000;

delta, gamma, theta, vega, rho