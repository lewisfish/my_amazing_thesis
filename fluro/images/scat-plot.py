#!/home/lewis/anaconda3/bin/python
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np


def redscat(wave, a, b, f):
    return a * (f * (wave / 500)**(-4) + (1. - f) * (wave / 500.)**(-b))


fig, ax = plt.subplots()

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=12)
fig.subplots_adjust(left=.1, bottom=.1, right=.98, top=.99)

ws = np.linspace(200, 1000, 1000)
ax.plot(ws, redscat(ws, 66.70, .69, 0.29), label="Epidermis")
ax.plot(ws, redscat(ws, 43.6, .35, .41), label="Dermis")
ax.semilogy(ws, 1050.6 * ws**(-.68), label="Hypodermis")

ax.set_xlabel("Wavelength/nm")
ax.set_ylabel(r"Reduced Scattering coiefficent/$cm^{-1}$")
ax.legend()

fig.set_size_inches(width, height)
fig.savefig('scat-plot.pdf')
plt.show()
