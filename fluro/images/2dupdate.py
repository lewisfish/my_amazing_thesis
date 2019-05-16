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


def banana(x, y):
    a = 1.
    b = 100.
    return (a - x)**2 + b * (y - x**2)**2

#sum(100.0*(x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0


def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    # return sum((x[1:]**2 + x[:-1] - 11)**2 + (x[1:] + x[:-1]**2 - 7)**2)


def sphere(x):
    return sum(x[1:]**2 + x[:-1]**2)


npts = 201
x, y = np.mgrid[-5:5:npts * 1j, -5:5:npts * 1j]
x.shape = (npts**2)
y.shape = (npts**2)
# z = himmelblau(np.vstack((x, y)))
z = himmelblau(x, y)
x.shape = (npts, npts)
y.shape = (npts, npts)
z.shape = (npts, npts)


def animate(i):

    x, y, fit = np.loadtxt("himmelblau-thesis.dat", unpack=True)

    for i in range(0, len(x), 3):
        p1 = [x[i], y[i]]  # seperate points
        p2 = [x[i + 1], y[i + 1]]
        p3 = [x[i + 2], y[i + 2]]

        # put points into area so that full tetrahedron is inscribed
        xs = [p1[0], p2[0], p3[0], p1[0], p2[0], p3[0]]
        ys = [p1[1], p2[1], p3[1], p1[1], p2[1], p3[1]]

        ax.plot(xs, ys)


ax.scatter(3., 2., marker="o", s=50, color="black", zorder=10)
ax.scatter(-2.805118, 3.283186, marker="o", s=50, color="black", zorder=10)
ax.scatter(-3.779310, -3.283186, marker="o", s=50, color="black", zorder=10)
ax.scatter(3.584458, -1.848126, marker="o", s=50, color="black", zorder=10)

animate(0)
levels = np.logspace(0.00001, 5.5, 10.)
ax.contour(x, y, z, levels, colors="k")

fig.set_size_inches(width, height)
fig.savefig('himmelblau.pdf')
plt.show()