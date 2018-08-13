import matplotlib.pylab as plt
import numpy as np
import random
import math


def lineFormula(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    c = y2 - m*x2
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
for i in lines:
    plt.axvline(i, color="Black")

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
            plt.plot([x1, x2], [y1, y2], color="red")
        else:
            plt.plot([x1, x2], [y1, y2])
    if counter > 0:
        print(float(trials)*2.*needleLength/(lineDist*float(counter)))
plt.show()
