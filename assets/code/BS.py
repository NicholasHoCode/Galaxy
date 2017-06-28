© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

# SAMPLE CODE

def sim(S_0, vol, T):
    p = np.zeros(T+1)
    p[0] = S_0
    for t in range(T):
        p[t+1] = p[t] * np.exp(-vol**2/2.0 + np.random.randn()*vol)
    return p

def smoothing(data, W):
    T = len(data)
    smoothed = np.zeros(T)
    for t in range(T):
        count = 0
        for wdw in range(t-W, t+W+1):
            if wdw >= 0 and wdw < T:
                smoothed[t] += p[wdw]
                i += 1
        smoothed[t] /= i
    return smoothed     

def bScholes(S_0, sp, vo, T):
    d1 = (np.log(S_0/sp) + (vol**2/2.0)*T) / (vol*np.sqrt(T))
    d2 = (np.log(S_0/sp) + (-vol**2/2.0)*T) / (vol*np.sqrt(T))
    return scipy.stats.norm.cdf(d1)*S_0 - scipy.stats.norm.cdf(d2)*sp

i_price = 10
vol = 0.01
T = 1000
sp = 80
W = 25
N_repeats = 1000
p = sim(i_price, vol, T)
from pylab import *
plt.plot(pr)
smoothed_p = smoothing(p, W)
plt.plot(smoothed_p, 'r')
##plt.show()

simulated_op = np.zeros(N_repeats)

simulated_op = np.zeros(N_repeats)
for i in range(N_repeats):
    end_p = sim(i_price, vol, T)[-1]
    if end_p < sp:
        simulated_op[i] = 0.0
    else:
        simulated_op[i] = end_p - sp
np.mean(simulated_op)
bScholes(i_price, sp, vol, T)




























