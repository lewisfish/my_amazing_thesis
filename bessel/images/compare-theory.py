import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np
import scipy.special as spl


width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=12)


def bessel(r, wave):
    wavelength = wave
    alpha = 5. * np.pi / 180.
    n = 1.4630
    beta = np.arcsin(n * np.sin(alpha)) - alpha
    kr = (2. * np.pi / wavelength) * np.sin(beta)
    return spl.j0(kr * r)**2


file = "sascha exp/0.5mm/bessel-testtt-0.00.dat"

fig, axs = plt.subplots(1, 1)
fig.subplots_adjust(left=.1, bottom=.12, right=.99, top=.95, hspace=0.0, wspace=0.0)


width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=12)

xmax = .25e-3
xs = np.linspace(-xmax, xmax, 501)
xt = np.linspace(-xmax, xmax, 10000)


data = np.fromfile(file=file, dtype=np.float64, sep="")
data = data.reshape((501, 501), order="F")

data = data / data.max()
axs.scatter(xs*1e5, data[:, 250], label="MCRT Simulation", color="#ff8f0e")
axs.plot(xt * 1e5, bessel(xt, 488e-9), label="Theory")
axs.set_xlim(-4., 4.)
axs.set_ylim(0., 1.1)

axs.set_xlabel(r"Distance/$\mu$ m")
axs.set_ylabel(r"Intensity/arb.")
axs.legend()
fig.set_size_inches(width, height)
fig.savefig('compare-theory.pdf')

plt.show()
