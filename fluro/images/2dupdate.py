# import matplotlib as mpl
# mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np
import matplotlib.animation as animation
from scipy.optimize import rosen

width = 6.510  # inches
height = width / 1.618

# plt.rc('font', family='serif', serif='Times')
# plt.rc('text', usetex=True)
# plt.rc('xtick', labelsize=8)
# plt.rc('ytick', labelsize=8)
# plt.rc('axes', labelsize=8)


fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=.05, bottom=.05, right=.98, top=.99, wspace=0, hspace=0)


def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def sphere(x, y):
    return x**2 + y**2


def ackley(x, y):
    return -20. * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2. * np.pi * x) + np.cos(2. * np.pi * y))) + np.exp(1.) + 20.


def animate(i, ax, name):

    x, y, fit = np.loadtxt(name, unpack=True)

    for i in range(0, len(x), 3):
        p1 = [x[i], y[i]]  # seperate points
        p2 = [x[i + 1], y[i + 1]]
        p3 = [x[i + 2], y[i + 2]]

        # put points into area so that full tetrahedron is inscribed
        xs = [p1[0], p2[0], p3[0], p1[0], p2[0], p3[0]]
        ys = [p1[1], p2[1], p3[1], p1[1], p2[1], p3[1]]

        ax.plot(xs, ys)


animate(0, axs[0, 0], "ackley-thesis.dat")
npts = 201
x, y = np.mgrid[-5:5:npts * 1j, -5:5:npts * 1j]
x.shape = (npts**2)
y.shape = (npts**2)
z = ackley(x, y)
x.shape = (npts, npts)
y.shape = (npts, npts)
z.shape = (npts, npts)
levels = np.logspace(0.35, 3.2, 30)
axs[0, 0].contour(x, y, z, levels, colors="k")
axs[0, 0].scatter(0., 0., marker="o", s=50, color="black", zorder=10)


animate(0, axs[1, 1], "bannana-thesis.dat")
x, y = np.mgrid[-5:5:npts * 1j, -5:5:npts * 1j]
x.shape = (npts**2)
y.shape = (npts**2)
z = rosen(np.vstack((x, y)))
x.shape = (npts, npts)
y.shape = (npts, npts)
z.shape = (npts, npts)
levels = np.logspace(0.0, 5.2, 10)
axs[1, 1].contour(x, y, z, levels, colors="k")
axs[1, 1].set_xlim(-2, 2)
axs[1, 1].set_ylim(-.5, 3)
axs[1, 1].scatter(1., 1., marker="o", s=50, color="black", zorder=10)


animate(0, axs[1, 0], "himmelblau-thesis.dat")
x, y = np.mgrid[-5:5:npts * 1j, -5:5:npts * 1j]
x.shape = (npts**2)
y.shape = (npts**2)
z = himmelblau(x, y)
x.shape = (npts, npts)
y.shape = (npts, npts)
z.shape = (npts, npts)
levels = np.logspace(0.0, 5.2, 15)
axs[1, 0].contour(x, y, z, levels, colors="k")
axs[1, 0].scatter(3., 2., marker="o", s=50, color="black", zorder=10)
axs[1, 0].scatter(-2.805118, 3.113186, marker="o", s=50, color="black", zorder=10)
axs[1, 0].scatter(-3.779310, -3.283186, marker="o", s=50, color="black", zorder=10)
axs[1, 0].scatter(3.584458, -1.848126, marker="o", s=50, color="black", zorder=10)

animate(0, axs[0, 1], "himmelblau-thesis.dat")
x, y = np.mgrid[-5:5:npts * 1j, -5:5:npts * 1j]
x.shape = (npts**2)
y.shape = (npts**2)
z = sphere(x, y)
x.shape = (npts, npts)
y.shape = (npts, npts)
z.shape = (npts, npts)
levels = np.logspace(0.0, 5.2, 15)
axs[0, 1].contour(x, y, z, levels, colors="k")
axs[0, 1].scatter(0., 0., marker="o", s=50, color="black", zorder=10)

axs[0, 0].axes.get_xaxis().set_visible(False)
axs[0, 0].axes.get_yaxis().set_visible(False)

axs[0, 1].axes.get_xaxis().set_visible(False)
axs[0, 1].axes.get_yaxis().set_visible(False)

axs[1, 1].axes.get_xaxis().set_visible(False)
axs[1, 1].axes.get_yaxis().set_visible(False)


axs[1, 0].axes.get_xaxis().set_visible(False)
axs[1, 0].axes.get_yaxis().set_visible(False)


# fig.set_size_inches(width, height)
# fig.savefig('ackley.pdf')
plt.show()