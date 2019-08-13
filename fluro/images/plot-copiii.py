import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
import numpy as np

files = ["/home/lewis/phdshizz/Ga-salvo-2018/res/Coproporphyrin.dat", "/home/lewis/phdshizz/Ga-salvo-2018/res/Coproporphyrin_fluro.dat"]

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=12)
fig, axs = plt.subplots(1, 2)

fig.subplots_adjust(left=.1, bottom=.12, right=.98, top=.99, wspace=.3)


for i, file in enumerate(files):
    x, y = np.loadtxt(file, unpack=True)
    axs[i].plot(x, y)
    axs[i].set_xlabel("Wavelength/nm")
    if "fluro" in file:
        axs[i].set_ylabel("Intensity/arb.")
    else:
        axs[i].set_ylabel(r"Absorption coefficient/$cm^{-1}$")

axs[0].text(350, .35, "a)", fontsize="14", fontweight='bold')
axs[1].text(550, .98, "b)", fontsize="14", fontweight='bold')
fig.set_size_inches(width, height)
fig.savefig('cop-optprop-1.pdf')
plt.show()
