import matplotlib as mpl
mpl.use('pdf')
import numpy as np
import matplotlib.pyplot as plt


width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=12)

fig, axs = plt.subplots(1, 2)
plt.subplots_adjust(top=.99, bottom=.1, right=.99, left=.1, wspace=0.0)

files = ["fluro_out.dat", "fluro_outl.dat"]
for file in files:
    x = np.loadtxt(file, unpack=True)
    x /= np.amax(x)
    axs[0].plot(x, label=file)

files = ["fluro_outf.dat", "fluro_outlf.dat"]
for file in files:
    x = np.loadtxt(file, unpack=True)
    if "lf" in file:
        lab = "Many photons"
    else:
        lab = "Less photons"
    axs[1].plot(x, label=lab)

for ax in axs:
    ax.set_xlim(310, 760)
    ax.set_ylim(0., 1.01)
axs[0].set_ylabel("Signal/arb.")
axs[0].set_xlabel("Wavelength/nm")
axs[1].set_xlabel("Wavelength/nm")
axs[1].set_yticks([])

axs[1].legend()
axs[0].text(320, .94, "a)", fontweight="bold", fontsize="15")
axs[1].text(320, .94, "b)", fontweight="bold", fontsize="15")

fig.set_size_inches(width, height)
fig.savefig('sgfilter-prrof-1.pdf')

plt.show()
