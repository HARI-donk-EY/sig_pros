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

def f3(n, alpha, beta):
    return np.dot(vec_an(np.arange(n), alpha, beta), np.array([1/(10**i) for i in range(n)]))-10/89

vec_f3 = scipy.vectorize(f3)

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2

n = np.arange(1,100)

l3 = vec_f3(n,alpha,beta)

plt.plot(n, l3, label=r'$\sum_{k=1}^{n}\frac{a_{k}}{10^k}-\frac{10}{89}$', color = 'r')
plt.legend()
plt.grid()
plt.savefig('../figs/1_2.png')
plt.show()
