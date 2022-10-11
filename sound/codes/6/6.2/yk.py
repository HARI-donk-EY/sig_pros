import numpy as np
import matplotlib.pyplot as plt

# using termux
import subprocess
import shlex

N = 20

Y = np.loadtxt('ykreal.dat')

plt.stem(range(0,N), Y)
plt.title('Filter Output Using DFT')
plt.xlabel('$k$')
plt.ylabel('$Y(k)$')
plt.grid()

plt.savefig('../../../figs/yk.pdf')
plt.savefig('../../../figs/yk.eps')
plt.show()
#subprocess.run(shlex.split("termux-open ../../../figs/yk.pdf"))
