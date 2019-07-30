import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
from scipy import interpolate


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
fig.subplots_adjust(left=.08, bottom=.1, right=.93, top=.98)


spectrum = "solar.dat"
x, y = np.loadtxt(spectrum, unpack=True, delimiter=",")
f = interpolate.interp1d(x, y)
xnew = np.linspace(301, 689, 1000)
ynew = f(xnew)

cdfK = kennymethod(y, x)

tmp = ynew
tmp /= np.sum(ynew)
cdf = np.cumsum(tmp)
waves = []
fluxs = []
for i in range(1, 5000000):
    xi = np.random.rand(1)
    loc = int(np.searchsorted(cdf, xi)) - 1
    wave = interp(xnew, cdf, xi, loc)
    # flux = interp(y, x, wave, loc)
    waves.append(wave)
    # fluxs.append(flux)
    # plt.scatter(wave, flux, color="orange", marker="x")

    # loc = int(np.searchsorted(cdfK, xi) - 1)
    # wave = interp(x, cdfK, xi, loc)
    # flux = interp(y, x, wave, loc)
    # plt.scatter(wave, flux + .001, color="blue")

hist, bins = np.histogram(waves, bins="auto")
ax.hist(waves, bins="auto", label="MC sampled spectrum")
ax1 = ax.twinx()  # instantiate a second axes that shares the same x-axis
lines, labels = ax.get_legend_handles_labels()
lns2 = ax1.plot(xnew, ynew * 1000, label="Original spectrum", color="orange")
lines2, labels2 = ax1.get_legend_handles_labels()


# plt.plot(np.linspace(300, 690, len(hist)), hist / np.amax(hist))
ax.set_ylabel(r"Sample counts/\#")
ax1.set_ylabel("Flux/AU")
ax.set_xlabel("Wavelength/nm")
ax1.legend(lines + lines2, labels + labels2, loc=0)
fig.set_size_inches(width, height)
fig.savefig('solar-sample.pdf')
plt.show()
