import matplotlib as mpl
import numpy as np
import random
import math
mpl.use('pdf')
import matplotlib.pylab as plt


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


def lineFormula(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    c = y2 - m * x2
    return (m, c)


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
needleLength = 1  # cm
lineDist = 1.5  # cm
height = 10  # cm
width = 10  # cm
twopi = math.pi * 2.
trials = 100

# setup board
lines = np.arange(lineDist, width, lineDist)
cnt = 0
for i in lines:
    if cnt == 0:
        ax.axvline(i, color="Black", label="Line")
        cnt += 1
    else:
        ax.axvline(i, color="Black")

counter = 0
for i in range(trials):
    x1 = random.random() * width
    y1 = random.random() * height

    theta = random.random() * twopi
    x = math.sqrt(lineDist) * math.cos(theta)
    y = math.sqrt(lineDist) * math.sin(theta)
    x2 = x1 + x
    y2 = y1 + y
    if (x2 > 0. and x2 < width) and (y2 > 0. and y2 < height):
        m, c = lineFormula(x1, x2, y1, y2)
        if intersect(m, c, x1, x2, lines):
            counter += 1
            if counter == 1:
                ax.plot([x1, x2], [y1, y2], color="blue", label="Crossed Line")
            else:
                ax.plot([x1, x2], [y1, y2], color="blue")
        else:
            if i == 1:
                ax.plot([x1, x2], [y1, y2], color="gold", label="Missed Line")
            else:
                ax.plot([x1, x2], [y1, y2], color="gold")
    if counter > 0:
        print(float(trials) * 2. * needleLength / (lineDist * float(counter)))
ax.legend()
fig.set_size_inches(width, height)
fig.savefig('buffon.pdf')
plt.show()