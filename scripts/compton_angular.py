import numpy as np
import matplotlib.pyplot as plt

plt.style.use("beamer")

cos = np.linspace(-1.0, 1.0, 1000)
energies = [0.0, 0.5, 5.0]
crs = []
me = 0.511

for E in energies:
    P = 1.0 / (1.0 + E / me * (1 - cos))
    crs.append(P**2.0 * (P + P**-1.0 + cos**2.0 - 1.0))

for sigma in crs:
    plt.plot(cos, sigma, "-")


plt.xlim(-1.0, 1.0)
plt.ylim(0.0, 2.0)
plt.xlabel(r"$\cos\theta$")
plt.ylabel(r"$\frac{\mathrm{d}\sigma}{\mathrm{d} \Omega}$ / a.u.")

plt.tick_params(axis="y", labelleft="off")

plt.text(0.0, 1.2, r"$E_\gamma \approx \SI{0}{MeV}$", ha="center", color="#E41A1C")
plt.text(-0.84, 0.42, r"$E_\gamma = \SI{0.5}{MeV}$", ha="left", color="#377EB8")
plt.text(-0.84, 0.12, r"$E_\gamma = \SI{5}{MeV}$", ha="left", color="#4DAF4A")

fig = plt.gcf()
fig.set_size_inches(2.1, 1.9)
plt.xticks([-1.0, -0.5, 0.0, 0.5, 1.0])

plt.tight_layout(pad=0.2)
plt.savefig("figures/compton_angular.pdf")
plt.close()
