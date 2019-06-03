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
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=10)

file = "/home/lewis/phdshizz/bessel beam/bin/double-slit.dat"
data = np.fromfile(file, sep="", dtype=np.float64)
data = data.reshape((2051, 2051))

fig, ax = plt.subplots()
fig.subplots_adjust(left=.08, bottom=.1, right=.99, top=.99)


wave = 488e-9
a = 20. * wave
d = 80. * wave
xmax = .5e-3
L = 10000 * wave

x = np.linspace(-xmax, xmax, 2051)
k = 2. * np.pi / wave

alp = (k * 0.5 * a * x) / np.sqrt(L**2 + x**2)
bet = (k * d * x) / (2. * np.sqrt(L**2 + x**2))


yhat = scipy.signal.savgol_filter(data[1025, :], 61, 3)
x = np.linspace(-.5, .5, 2051)

ax.plot(x, theory(alp, bet), label="Theory")
ax.scatter(x[::5], yhat[::5] / np.amax(yhat), marker="x", color="orange", label="MCRT data")
ax.set_xlabel("Distance/mm")
ax.set_ylabel("Intensity/arb.")
ax.legend()


fig.set_size_inches(width, height)
fig.savefig('doubleslit.pdf')
plt.show()
