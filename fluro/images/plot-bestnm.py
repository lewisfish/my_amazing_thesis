import matplotlib as mpl
mpl.use('pdf')
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=12)

fig, ax = plt.subplots()
fig.subplots_adjust(left=.075, bottom=.1, right=.99, top=.98)

files = ["thesis_out.dat", "fad_out.dat", "nadh_out.dat", "collagen_out.dat"]
for file in files:
    x = np.loadtxt(file, unpack=True)
    name = file[0].upper() + file[1:-8]
    xs = signal.savgol_filter(x, 101, 2)
    if "thesis" in file:
        maxval = np.amax(xs)
        name = "NM output"
    if "ad" in name:
        name = name.upper()
    ax.plot(xs / maxval, label=name)


x = np.loadtxt("target-10d.dat", unpack=True)
ax.plot(x, linestyle="--", color="k", zorder=0, label="Target")

ax.set_xlabel("Wavelength/nm")
ax.set_ylabel("Fluorescence intensity/AU")
ax.set_ylim(0, 1.)

ax.legend()
fig.set_size_inches(width, height)
fig.savefig('nm-bestfit.pdf')
plt.show()
