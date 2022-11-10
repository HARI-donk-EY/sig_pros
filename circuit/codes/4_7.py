import numpy as np
from matplotlib import pyplot as plt
import scipy as sp

k = 1.5e6
def vn_con(t):
    return 2*(1 - np.exp(-k*t))/3

def u(n):
    if n>=0:
        return 1.00
    else:
        return 0.00

def y_diff(n):
    if n < 0:
        return 0
    else:
        return y_diff(n-1)*(((1 - 0.075)/(1 + 0.075))**(n*1e7))+((u(n)+u(n-1))*2/3)*(1 - ((1 - 0.075)/(1 + 0.075))**(n*1e7))

y_diff_vec = sp.vectorize(y_diff)

vn_con_vec = sp.vectorize(vn_con)
spice = np.loadtxt('4_7.dat')
T = 1e-7
tau = 2e-6/3
p = (2*tau-T)/(2*tau+T)
R1 = 1
R2 = 2
C0 = 1e-6
t = np.linspace(0, 1e-5, 101)
n = np.arange(0, 101, 1)
vn = 1 - p**n
vn = np.pad(vn, (0,1), constant_values=(0,0)) + np.pad(vn, (1,0), constant_values=(0,0))
vn[0] = 0
plt.plot(t, vn_con_vec(t))
plt.plot(t, (2*tau/(2*C0*R2))*vn[:len(t)], 'o')
plt.plot(spice[:,0], spice[:,1], '.')
plt.plot(t,y_diff_vec(t),'.')
plt.legend(['Theory (continuous)', 'Theory (discrete)', 'Simulation (Ngspice)', '$y_{diff}(n)$'])
plt.savefig('../figs/4_7.png')
plt.show()
