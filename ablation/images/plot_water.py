import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np


def stylize_axes(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.xaxis.set_tick_params(top=False, direction='out', width=1)
    ax.yaxis.set_tick_params(right=False, direction='out', width=1)


width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)


fig, ax = plt.subplots()
fig.subplots_adjust(left=.15, bottom=.16, right=.99, top=.97)

# https://stackoverflow.com/questions/18215276/how-to-fill-rainbow-color-under-a-curve-in-python-matplotlib


def rect(x, y, w, h, c):
    ax = plt.gca()
    polygon = plt.Rectangle((x, y), w, h, color=c)
    ax.add_patch(polygon)


def rainbow_fill(X, Y, cmap=plt.get_cmap("jet")):
    plt.plot(X, Y, lw=0)  # Plot so the axes scale correctly

    dx = X[1] - X[0]
    N = float(X.size)

    for n, (x, y) in enumerate(zip(X, Y)):
        color = cmap(n / N)
        rect(x, 0.0001, dx, y, color)

file = "water absor.dat"
x, y = np.loadtxt(file, unpack=True)


X = np.linspace(390, 700, 10)
Y = np.empty(len(X))
Y.fill(1000000000)
rainbow_fill(X, Y)


ax.semilogy(x, y, color="Black", label="Water absorption")
ax.set_xlim(0, 11000)
ax.set_ylim(10**-4, 10**5)

ax.axvline(10600, linestyle="--", color="Blue", label=r"$10.6\ \mu m$")
ax.axvline(2940, linestyle="--", color="Red", label=r"$2940\ nm$")

ax.set_xlabel("Wavelength/nm")
ax.set_ylabel(r"Absorption coefficient/cm$^{-1}$")
ax.legend()

fig.set_size_inches(width, height)
fig.savefig('water.pdf')
plt.show()
