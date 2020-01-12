#!/home/lewis/anaconda3/bin/python
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np
import scipy.signal


def theory(alpha, beta):
    return np.cos(beta)**2 * (np.sin(alpha) / alpha)**2


width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=12)

file = "/home/lewis/phdshizz/bessel beam/bin/double-slit.dat"
data = np.fromfile(file, sep="", dtype=np.float64)
data = data.reshape((2051, 2051))

fig, axs = plt.subplots(2, 1)
fig.subplots_adjust(left=.11, bottom=.12, right=.99, top=.99, hspace=0.)


wave = 488e-9
a = 20. * wave
d = 80. * wave
xmax = .5e-3
L = 10000 * wave

x = np.linspace(-xmax, xmax, 2051)
k = 2. * np.pi / wave

alp = (k * 0.5 * a * x) / np.sqrt(L**2 + x**2)
bet = (k * d * x) / (2. * np.sqrt(L**2 + x**2))


yhat = scipy.signal.savgol_filter(data[1025, :], 61, 2)
x = np.linspace(-.5, .5, 2051)

axs[0].plot(x, theory(alp, bet), label="Theory")
axs[0].scatter(x[::5], yhat[::5] / np.amax(yhat), marker="x", color="orange", label="MCRT data")
axs[0].set_ylabel("Intensity/arb.")
axs[0].legend()

axs[1].imshow(data, extent=[-.5, .5, -.5, .5], aspect="auto")
axs[1].set_xlabel("Distance/mm")
axs[1].set_ylabel("Distance/mm")

fig.set_size_inches(width, height)
fig.savefig('doubleslit.pdf')
plt.show()
