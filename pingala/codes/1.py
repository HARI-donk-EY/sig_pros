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

def f1(n, alpha, beta):
    return an(n+2, alpha, beta)

vec_f1 = scipy.vectorize(f1)

def f2(n, alpha, beta):
    return np.sum(vec_an(np.arange(n), alpha, beta))

def f3(n, alpha, beta):
    return np.dot(vec_an(np.arange(n), alpha, beta), np.array([1/(10**i) for i in range(n)]))-10/89

vec_f2 = scipy.vectorize(f2)
vec_f3 = scipy.vectorize(f3)

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2

n = np.arange(1,100)

# pblm 1.1

l1 = vec_f1(n,alpha,beta)
l2 = vec_f2(n,alpha,beta)
l3 = vec_f3(n,alpha,beta)

plt.subplot(211)
plt.plot(n, l1, label=r'$a_{n+2}-1$', color = 'r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(n, l2, label=r'$\sum_{k=1}^{n}a_{k}$')
plt.grid()
plt.legend()
plt.savefig('../figs/1_1.png')
plt.show()

# pblm 1.2

plt.plot(n, l3, label=r'$\sum_{k=1}^{n}\frac{a_{k}}{10^k}-\frac{10}{89}$', color = 'r')
plt.legend()
plt.grid()
plt.savefig('../figs/1_2.png')
plt.show()

# pblm 1.3

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
