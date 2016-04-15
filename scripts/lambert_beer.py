import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

plt.style.use("beamer")

x = np.linspace(0.0, 5.0, 2000)
y = np.exp(-x)

plt.xlim(0.0, 5.0)
plt.ylim(0.0, 1.1)

plt.xlabel(r"position $x / \lambda$")
plt.ylabel(r"relative count rate")

plt.axhline(np.exp(-1.0), 0.0, 1. / 5.0, ls=":", c="k")
plt.axvline(1.0, 0.0, np.exp(-1.0) / 1.1, ls=":",c="k")

plt.plot(x, y, "-")

plt.tight_layout(pad=0.1)
plt.savefig("figures/lambert_beer_exp.pdf")
plt.close()