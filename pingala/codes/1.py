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

def f1(n, alpha, beta):
    return an(n+2, alpha, beta)

vec_f1 = scipy.vectorize(f1)

def f2(n, alpha, beta):
    return np.sum(vec_an(np.arange(n), alpha, beta))

vec_f2 = scipy.vectorize(f2)

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2

n = np.arrange(1,100)

l1 = vec_f1(n,alpha,beta)
l2 = vec_f2(n,alpha,beta)

plt.subplot(211)
plt.plot(n, l1, label=r'$a_{n+2}-1$', color = 'r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(n, l2, label=r'$sum_{k=1}^{n}a_{k}$')
plt.grid()
plt.legend()
plt.savefig('../figs/1_1.png')


