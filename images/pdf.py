import numpy as np
import matplotlib.pyplot as plt


def trapInt(wave, flux):
    summ = 0.
    cdf = np.zeros(len(wave) - 1)
    for i in range(0, len(wave) - 1):
        summ += 0.5 * (flux[i+1] + flux[i]) * (wave[i + 1] - wave[i])
        cdf[i] = summ
    return cdf / cdf[-1]


def getwaves(ws, c, l, xis):
    waves = np.zeros(len(l))
    for j, i in enumerate(l):
        waves[j] = ws[i] + (ws[i + 1] - ws[i]) * ((xis[j] - c[j]) / (c[j + 1] - c[j]))
    return waves


spectrum = "solar.dat"
f = open(spectrum, "r")
lines = f.readlines()
x = []
y = []
for line in lines:
    data = line.split(",")
    x.append(float(data[0]))
    y.append(float(data[1]))


cdf = trapInt(x, y)
xis = np.random.rand(10)
locs = np.searchsorted(cdf, xis)
locs -= 1

waves = getwaves(x, cdf, locs, xis)
print(waves)
plt.plot(x, y)
plt.show()
