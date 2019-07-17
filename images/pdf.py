import numpy as np
import matplotlib.pyplot as plt


def getCDF(wave, flux):
    cdf = np.zeros(len(wave) - 1)

    for j in range(0, 37):
        summ = 0.
        for i in range(0, j):
            summ += 0.5 * (flux[i + 1] + flux[i]) * (wave[i + 1] - wave[i])
        cdf[j] = summ
    # summ = 0.
    # cdf = np.zeros(len(wave) - 1)
    # for i in range(0, len(wave) - 1):
    #     summ += 0.5 * (flux[i + 1] + flux[i]) * (wave[i + 1] - wave[i])
    #     cdf[i] = summ
    return cdf / cdf[-1]


def interp(targ, c, pos, i):
    return float(targ[i] + (targ[i + 1] - targ[i]) * ((pos - c[i]) / (c[i + 1] - c[i])))


spectrum = "solar.dat"
x, y = np.loadtxt(spectrum, unpack=True, delimiter=",")

cdf = getCDF(x, y)
waves = []
flux = []
for i in range(1, 10000):
    xi = np.random.rand(1)
    loc = int(np.searchsorted(cdf, xi) - 1)
    wave = interp(x, cdf, xi, loc)
    waves.append(wave)
    flux.append(interp(y, x, wave, loc))

plt.plot(x, y, label="Original")
plt.scatter(waves, flux, label="")
plt.legend()
plt.show()
