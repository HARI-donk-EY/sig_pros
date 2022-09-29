import numpy as np
import matplotlib.pyplot as plt



N = 20


#print(X), (H)
X = np.loadtxt('xkreal.dat')
H = np.loadtxt('hkreal.dat')

#subplots
plt.subplot(2,1,1)
plt.stem(range(0,N),X)
plt.title('')
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.grid()# minor

plt.subplot(2,1,2)
plt.stem(range(0,N),H)
plt.title('')
plt.xlabel('$k$')
plt.ylabel('$H(k)$')
plt.grid()# minor
plt.savefig('../../../figs/xkhk.pdf')
plt.show()   


