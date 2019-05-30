#!/home/lewis/anaconda3/bin/python
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np

fig, ax = plt.subplots()

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=12)
fig.subplots_adjust(left=.1, bottom=.1, right=.98, top=.995)

file = "target.dat"
x = np.loadtxt(file, unpack=True)
ax.plot(x)
ax.set_xlabel("Wavelength/nm")
ax.set_ylabel("Fluorescence Intensity/arb.")

fig.set_size_inches(width, height)
fig.savefig('target-toy.pdf')
plt.show()
