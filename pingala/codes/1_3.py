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
        return an(n0-1, alpha, beta)
    else:
        return 0.0

vec_bn = scipy.vectorize(bn)

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2

n = np.arange(1,100)

def f4(n, alpha, beta):
    return alpha**n + beta**n

vec_f4 = scipy.vectorize(f4)

l4 = vec_bn(n, alpha, beta)
l5 = vec_f4(n, alpha, beta)

plt.subplot(211)
plt.plot(n, l4, label=r'$b_{n}', color = 'r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(n, l5, label=r'$\alpha^n+\beta^n$')
plt.grid()
plt.legend()
plt.savefig('../figs/1_3.png')
plt.show()
