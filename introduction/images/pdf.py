import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt


def kennymethod(arr, arr2):
    summ = 0.
    cdf = np.zeros(len(arr) - 1)
    for i in range(0, len(arr) - 1):
        summ += 0.5 * (arr[i + 1] + arr[i]) * (arr2[i+1] - arr2[i])
        cdf[i] = summ
    return cdf / cdf[-1]


def getCDF(arr):
    cdf = np.zeros(len(arr))
    summ = 0.
    arr /= sum(arr)
    for i, j in enumerate(arr):
        summ += j
        cdf[i] = summ
    return cdf


def interp(targ, c, pos, i):
    return float(targ[i] + (targ[i + 1] - targ[i]) * ((pos - c[i]) / (c[i + 1] - c[i])))


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


spectrum = "solar.dat"
x, y = np.loadtxt(spectrum, unpack=True, delimiter=",")

cdfK = kennymethod(y, x)

tmp = y
tmp /= np.sum(y)
cdf = np.cumsum(tmp)
waves = []
fluxs = []
for i in range(1, 100):
    xi = np.random.rand(1)
    loc = int(np.searchsorted(cdf, xi) - 1)
    wave = interp(x, cdf, xi, loc)
    flux = interp(y, x, wave, loc)
    waves.append(wave)
    fluxs.append(flux)
    # plt.scatter(wave, flux, color="orange", marker="x")

    # loc = int(np.searchsorted(cdfK, xi) - 1)
    # wave = interp(x, cdfK, xi, loc)
    # flux = interp(y, x, wave, loc)
    # plt.scatter(wave, flux + .001, color="blue")


ax.plot(x, y, label="Original")
ax.scatter(waves, fluxs, label="Randomly sampled", color="orange", marker="x")
ax.set_ylabel("Flux/AU")
ax.set_xlabel("Wavelength/nm")
ax.legend()
fig.set_size_inches(width, height)
fig.savefig('solar-sample.pdf')
plt.show()
