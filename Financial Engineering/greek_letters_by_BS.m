clear;
%% Parameters
S0 = 50;
sigma = 0.3;
K = 52;
T = 2;
r = 0.05;
q = 0;

%% calculation of greek letters of put options
d1 = (log(S0/K) + (r+0.5*(sigma^2))*T) / (sigma*sqrt(T));
d2 = (log(S0/K) + (r-0.5*(sigma^2))*T) / (sigma*sqrt(T));
delta = exp(-q*T)*(normcdf(d1)-1);
gamma = normpdf(d1)*exp(-q*T)/(S0*sigma*sqrt(T));
Theta = -S0*normpdf(d1)*sigma*exp(-q*T)/(2*sqrt(T)) + q*S0*normcdf(-d1)*exp(-q*T) + r*K*exp(-r*T)*normcdf(-d2);
Vega = S0*sqrt(T)*normpdf(d1)*exp(-q*T);
Rho = -K*T*exp(-r*T)*normcdf(-d2);

delta, gamma, Theta, Vega, Rho


