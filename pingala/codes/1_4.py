import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

def an(n0, alpha, beta):
    if n0<=0:
        return 0.0
    else:
        return(alpha**n0 - beta**n0)/(alpha - beta)

vec_an = scipy.vectorize(an)

def bn(n0, alpha, beta):
    if n0>=1:
        return an(n0-1, alpha, beta) + an(n0+1, alpha, beta)
    else:
        return 0.0

vec_bn = scipy.vectorize(bn)

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2

n = np.arange(1,100)

def f5(n, alpha, beta):
    return np.dot(vec_bn(np.arange(n), alpha, beta), np.array([1/(10**i) for i in range(n)]))-8/89

vec_f5 = scipy.vectorize(f5)

l6 = vec_f5(n, alpha, beta)

plt.plot(n, l6, label=r'$\sum_{k=1}^{n}\frac{b_{k}}{10^k}-\frac{8}{89}$')
plt.legend()
plt.grid()
plt.savefig('../figs/1_4.png')
plt.show()

