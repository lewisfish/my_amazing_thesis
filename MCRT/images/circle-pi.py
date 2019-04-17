import matplotlib as mpl
import numpy as np
import random
import math
mpl.use('pdf')
import matplotlib.pylab as plt


def stylize_axes(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.xaxis.set_tick_params(top=False, direction='out', width=1)
    ax.yaxis.set_tick_params(right=False, direction='out', width=1)
    ax.xaxis.set_tick_params(left=False, direction='out', width=1)
    ax.yaxis.set_tick_params(bottom=False, direction='out', width=1)

rng = random.seed(5564750958806547488)  # yields pi = 3.12


width = 6.510  # inches
height = 6.510  # width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)


fig, ax = plt.subplots()
fig.subplots_adjust(left=.01, bottom=.01, right=.99, top=.99)


def circ(r, phi):
    return r * np.cos(phi), r * np.sin(phi)


def intersect(m, c, x1, x2, lines):
    if x1 > x2:
        tmp = x1
        x1 = x2
        x2 = tmp
    for i in lines:
        if x1 < i and x2 > i:
            return True
    return False


# setup vars
trials = 200

# setup square
ax.axvline(-.5, color="Black", lw=5)
ax.axvline(.5, color="Black", lw=5)
ax.axhline(-.5, color="Black", lw=5)
ax.axhline(.5, color="Black", lw=5)

rs = .5
phis = np.linspace(0., np.pi * 2., 1000)
ax.plot(*circ(rs, phis), color="red")
stylize_axes(ax)
inner = 0
outer = 0
for i in range(trials):
    x1 = random.random() - .5
    y1 = random.random() - .5

    r1 = np.sqrt(x1**2 + y1**2)
    if r1 <= rs:
        inner += 1
        plt.scatter(x1, y1, color="red")
    else:
        outer += 1
        plt.scatter(x1, y1, color="black")

print(4. * inner / (inner + outer))
ax.set_xlim(-.5, .5)
ax.set_ylim(-.5, .5)

fig.set_size_inches(width, height)
fig.savefig('picirc.pdf')
plt.show()
