import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np
import glob as gb
from scipy import ndimage


def func(element):
    listt = ["12.0", "10.0", "2.00", "6.00"]
    if element[-8:-4] not in listt:
        return element


width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=12)

twommf = gb.glob("2mm/*.dat")
fivemmf = gb.glob("0.5mm/*.dat")

twommf.sort()
fivemmf.sort()

twommf = list(filter(func, twommf))
fivemmf = list(filter(func, fivemmf))

xtwo = np.linspace(-1, 1, 2001)
xfive = np.linspace(-.25, .25, 501)

twoshape = (2001, 2001)
fiveshape = (501, 501)

fig, axs = plt.subplots(1, 3)
axs = axs.flatten()
plt.subplots_adjust(hspace=0.2, wspace=0.00, left=0.09, right=0.98, top=0.945, bottom=0.12)
for i, file in enumerate(twommf):
    data = np.fromfile(file, sep="", dtype=np.float64)
    data = data.reshape(twoshape)
    data /= np.amax(data)

    data = ndimage.gaussian_filter(data, .5)
    axs[i].plot(xtwo, data[:, 1000], label="Large")

    data = np.fromfile(fivemmf[i], sep="", dtype=np.float64)
    data = data.reshape(fiveshape)
    data /= np.amax(data)
    data = ndimage.gaussian_filter(data, .5)
    axs[i].plot(xfive, data[:, 250], label="Small")
    axs[i].set_title("IL volume=" + fivemmf[i][-8:-4] + r"$\mu L$")
    axs[i].set_xlim(-.075, .075)
    axs[i].set_xlabel("Position/mm")
    if i == 0:
        axs[i].set_ylabel("Intensity/arb.")
    else:
        axs[i].set_yticks([])
    if i == 2:
        axs[i].legend()
fig.set_size_inches(width, height)
fig.savefig('compare-med-size.pdf')
plt.show()
