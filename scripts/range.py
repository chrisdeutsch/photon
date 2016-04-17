import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

plt.style.use("beamer")

mu = 1.0
sigma = 0.04

x = np.linspace(0.0, 2.0, 2000)
y = 0.5 * erfc( (x - mu) / np.sqrt(2. * sigma**2))

plt.xlim(0.0, 1.3)
plt.ylim(0.0, 1.1)

plt.xlabel(r"depth $x$ / $R$")
plt.ylabel(r"relative count rate")

plt.axhline(0.5, 0.0, 1. / 1.3, ls=":", c="k")
plt.axvline(1.0, 0.0, 0.5 / 1.1, ls=":",c="k")

plt.plot(x, y, "-")

plt.tight_layout(pad=0.1)
plt.savefig("figures/range.pdf")
plt.close()