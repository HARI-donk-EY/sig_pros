import numpy as np

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2

#Problem 1.1

n = 100
k = np.linspace(1, n, n)
ak = (alpha**k - beta**k)/(alpha - beta)
sak = np.cumsum(ak)

if (np.allclose(sak[:98], ak[2:] - 1)): print("1.1 correct")
else: print("1.1 incorrect")


#Problem 1.2

t = 10**k
ta = ak*(1/t)
eps = 1e-6
lim = 10/89
sta = np.cumsum(ta)

if (abs(sta[-1] - lim) < eps): print("1.2 correct")
else: print("1.2 incorrect")

#Problem 1.3

b = ak[2:] + ak[:98]
b = np.pad(b, (1, 0), 'constant', constant_values=(1, 0))
b_new = alpha**k + beta**k

if (np.allclose(b, b_new[:99])): print("1.3 correct")
else: print("1.3 incorrect")

#Problem 1.4
tb = b*(1/t[:99])
eps = 1e-6
lim = 8/89
stb = np.cumsum(tb)
if (abs(stb[-1] - lim) < eps): print("1.4 correct")
else: print("1.4 incorrect")
