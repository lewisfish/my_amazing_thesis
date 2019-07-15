import matplotlib as mpl
mpl.use('pdf')
import numpy as np
import matplotlib.pyplot as plt

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=12)

fig, ax = plt.subplots()
fig.subplots_adjust(left=.1, bottom=.1, right=.94, top=.99)

file = "UV 7.csv"
x, y = np.loadtxt(file, delimiter=";", unpack=True)
ax.plot(x, y, label="Raw data")
ax.axvline(365., label="Incident light", color="k", linestyle="--")
ax.text(390, 2150, "Backscatter", fontsize=12)
ax.text(500, 450, "Autofluorescence peak", fontsize=12)
ax.text(630, 50, "Artifacts", fontsize=12)
ax.text(750, 100, "Unknown peak", fontsize=12)

ax.set_ylabel("Fluorescence intensity/AU")
ax.set_xlabel("Wavelength/nm")
ax.legend()

fig.set_size_inches(width, height)
fig.savefig('raw-spectra.pdf')

plt.show()
