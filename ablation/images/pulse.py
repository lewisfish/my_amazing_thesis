#!/home/lewis/anaconda3/bin/python3.6
import matplotlib as mpl
mpl.use('pdf')
import numpy as np
import matplotlib.pylab as plt


def gauss(x, a, b, c):
    return a * np.exp(-(x - b)**2 / (2. * c**2))


def triangular(x, a, plength):
    m = a / plength
    c = 2. * a
    return np.where(x <= plength, m * x,
                    np.maximum(-m * x + c, np.zeros(1000)))


def tophat(x, a, plength):
    return np.where(x < plength, a, 0.)

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=12)

fig, ax = plt.subplots()
plt.subplots_adjust(right=.99, left=.08, top=.99, bottom=.1)

width = 6.510  # inches
height = width / 1.618


pwr = 70
pulsel = 0.2
t = np.linspace(0, 1.5, 1000)

fact = np.sqrt(2. * np.log(2))
sig = (pulsel) / fact
mean = (pulsel) * 2.8 * fact

# ax.plot(t, gauss(t, pwr, mean, sig), label="Gaussian, same pulselength")

sig = (.471 * pulsel) / fact
mean = (.471 * pulsel) * 2.8 * fact
ax.plot(t, gauss(t, pwr, mean, sig), label="Gaussian, same area")
ax.plot(t, tophat(t, pwr, pulsel), label="Tophat")
ax.plot(t, triangular(t, pwr, pulsel), label="Triangular")
ap1 = np.cumsum(triangular(t, pwr, pulsel))
ap2 = np.cumsum(tophat(t, pwr, pulsel))
ap3 = np.cumsum(gauss(t, pwr, mean, sig))
print(ap1[-2:-1], ap2[-2:-1], ap3[-2:-1])
ax.set_xlabel("Time/s")
ax.set_ylabel("Power/W")
ax.set_xlim(0, 0.7)

plt.legend(fontsize="12")

fig.set_size_inches(width, height)
fig.savefig("profilespulse.pdf")
plt.show()
