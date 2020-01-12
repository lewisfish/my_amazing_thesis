import matplotlib as mpl
mpl.use('pdf')
import numpy as np
import matplotlib.pylab as plt


def pwrLaw(x, a, b):
    return a * x**b

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=12)

fig, ax = plt.subplots()
fig.subplots_adjust(left=.1, bottom=.12, right=.98, top=.99)

ws = np.linspace(400, 900, 10000)
ys = pwrLaw(ws, 3.873e9, -2.397)

ax.plot(ws, ys)

ax.set_xlabel("Wavelegnth/nm")
ax.set_ylabel(r"Scattering Coefficient/$m^{-1}$")
ax.set_xlim(400, 900)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


fig.set_size_inches(width, height)
fig.savefig('scat-prop-il.pdf')
plt.show()
