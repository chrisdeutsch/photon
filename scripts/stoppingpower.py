import numpy as np
import matplotlib.pyplot as plt

plt.style.use("beamer")

data = np.loadtxt("data/stoppingpower.csv", delimiter=",")


x = data[:,0]
x /= 27.1019

dEdx = data[:,1]
dEdx /= dEdx.max()

plt.xlim(0.0, 1.1)
plt.ylim(0.0, 1.1)

plt.xlabel(r"depth $x$ / $R$", fontsize=11)
plt.ylabel(r"stopping power $\frac{\mathrm{d}E}{\mathrm{d}x}$ / a.u.", fontsize=11)


plt.plot(x, dEdx, "-")

plt.tight_layout(pad=0.3)
plt.savefig("figures/stoppingpower.pdf")
plt.close()




