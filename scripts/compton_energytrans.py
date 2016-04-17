import numpy as np
import matplotlib.pyplot as plt

plt.style.use("beamer")

E = [0.5, 1.0, 1.5]
me = 0.511

T = np.linspace(0.0, 1.5, 1000)

intensity = []
for energy in E:
    epsilon = energy / me
    s = T / energy
    
    continuum = s < 2.0 * epsilon / (1.0 + 2.0 * epsilon)
    
    sigma = np.zeros(len(s))
    s = s[continuum]
    sigma[continuum] = epsilon**-2 * (2 + s**2 / (epsilon**2 *(1- s)**2) +
                         s / (1 - s) * (s - 2.0 / epsilon))
    intensity.append(sigma)

for E, I in zip(E, intensity):
    plt.plot(T, I, "-", label=r"$E_\gamma = " + r"\SI{" + r"{}".format(E) +r"}{MeV}$")

plt.xlim(0.0, 1.5)
plt.xlabel("energy transfer $T_\mathrm{e}$ / \si{MeV}")
plt.ylabel(r"$\frac{\mathrm{d}\sigma}{\mathrm{d} T_\mathrm{e}}$ / a.u.")

plt.tick_params(axis="y", labelleft="off")

plt.legend(loc=0, fontsize=9, handlelength=1)

fig = plt.gcf()
fig.set_size_inches(2.1, 2.3)
plt.xticks([0.0, 0.5, 1.0, 1.5])

plt.tight_layout(pad=0.2)
plt.savefig("figures/compton_energytrans.pdf")
plt.close()
