import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np
import matplotlib.animation as animation
from scipy.optimize import rosen

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)


fig, ax = plt.subplots()
fig.subplots_adjust(left=.05, bottom=.05, right=.98, top=.99)


def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def sphere(x):
    return sum(x[1:]**2 + x[:-1]**2)


def ackley(x, y):
    return -20. * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2. * np.pi * x) + np.cos(2. * np.pi * y))) + np.exp(1.) + 20.

npts = 201
x, y = np.mgrid[-5:5:npts * 1j, -5:5:npts * 1j]
x.shape = (npts**2)
y.shape = (npts**2)
# z = rosen(np.vstack((x, y)))
z = ackley(x, y)
x.shape = (npts, npts)
y.shape = (npts, npts)
z.shape = (npts, npts)


def animate(i):

    x, y, fit = np.loadtxt("ackley-thesis.dat", unpack=True)

    for i in range(0, len(x), 3):
        p1 = [x[i], y[i]]  # seperate points
        p2 = [x[i + 1], y[i + 1]]
        p3 = [x[i + 2], y[i + 2]]

        # put points into area so that full tetrahedron is inscribed
        xs = [p1[0], p2[0], p3[0], p1[0], p2[0], p3[0]]
        ys = [p1[1], p2[1], p3[1], p1[1], p2[1], p3[1]]

        ax.plot(xs, ys)


ax.scatter(0., 0., marker="o", s=50, color="black", zorder=10)
# ax.scatter(-2.805118, 3.113186, marker="o", s=50, color="black", zorder=10)
# ax.scatter(-3.779310, -3.283186, marker="o", s=50, color="black", zorder=10)
# ax.scatter(3.584458, -1.848126, marker="o", s=50, color="black", zorder=10)

animate(0)
levels = np.logspace(0.35, 3.2, 30)
ax.contour(x, y, z, levels, colors="k")

fig.set_size_inches(width, height)
fig.savefig('ackley.pdf')
plt.show()