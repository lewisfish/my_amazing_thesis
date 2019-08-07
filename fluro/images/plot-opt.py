#!/home/lewis/anaconda3/bin/python
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np


ln10 = np.log(10)


def readFile(file):
    x, y = np.loadtxt(file, unpack=True)
    return [x, y]


def base(wave):
    return 7.84 * (10.**8) * wave**(-3.255)


def eumel(wave):
    return 6.6 * (10**11) * wave**(-3.33)


def pheomel(wave):
    return 2.9 * (10**15) * wave**(-4.75)


def Oxy_Hb(wave, array):
    nlow = np.searchsorted(array[0], wave)
    ynew = np.interp(wave, array[0][nlow], array[1][nlow])
    return np.where(wave >= 250, 150. * ln10 * ((ynew) / 64458.), np.nan)


def DeOxy_Hb(wave, array):
    nlow = np.searchsorted(array[0], wave)
    ynew = np.interp(wave, array[0][nlow], array[1][nlow])
    return np.where(wave >= 250, 150. * ln10 * ((ynew) / 64458.), np.nan)


def Bcarotene(wave, array):
    nlow = np.searchsorted(array[0], wave)
    ynew = np.interp(wave, array[0][nlow], array[1][nlow])
    return np.where(wave > 220, np.where(wave < 700., ynew / 537., np.nan), np.nan)


def Bilirubin(wave, array):
    nlow = np.searchsorted(array[0], wave)
    ynew = np.interp(wave, array[0][nlow], array[1][nlow])
    return np.where(wave > 240, np.where(wave < 700., ynew / 585., np.nan), np.nan)


def Water(wave, array):
    nlow = np.searchsorted(array[0], wave)
    ynew = np.interp(wave, array[0][nlow], array[1][nlow])
    return ynew


def blood(waves, a1, a2, SO):
    return SO * Oxy_Hb(waves, a1) + (1. - SO) * DeOxy_Hb(waves, a2)


def stratum(waves, base, water):
    W = .05
    ax.plot(waves, ((Bcarotene(waves, Caro) * 2.1e-4) + base(waves)), label="Stratum Corenum")


def epidermis(waves, water, Caro):
    nu_m = 2. / 100.
    W = 0.2
    mua = nu_m * eumel(waves) + (1. - nu_m) * base(waves)
    # plt.plot(waves, (nu_m * (eumel(waves) + pheomel(waves)) + (base(waves) + ln10 * Bcarotene(waves, Caro) * 2.1e-4) * (1. - nu_m)) * (1. - W) + W * Water(waves, water), label="epi")
    ax.plot(waves, mua, label="Epidermis")


def pap(waves, water, Caro, Bili, DeoxyHb, OxyHb):
    W = 0.5
    Vb = 6. / 100.
    mua = ((blood(waves, OxyHb, DeoxyHb, .75) + ln10 * Bcarotene(waves, Caro) * 2.1e-4 + Bilirubin(waves, Bili) * .05) * Vb + base(waves) * (1. - Vb)) * (1. - W) + W * Water(waves, water)
    ax.semilogy(waves, mua, label="Papillary Dermis")


def ret(waves, water, Caro, Bili, DeoxyHb, OxyHb):
    W = 0.7
    Vb = 4.5 / 100.
    mua = ((blood(waves, OxyHb, DeoxyHb, .75) + ln10 * Bcarotene(waves, Caro) * 7e-5 + Bilirubin(waves, Bili) * .05) * Vb + base(waves) * (1. - Vb)) * (1. - W) + W * Water(waves, water)
    ax.semilogy(waves, mua, label="Reticular Dermis")


def hypo(waves, water, Caro, Bili, DeoxyHb, OxyHb):
    W = 0.7
    Vb = 5. / 100.
    mua = (blood(waves, OxyHb, DeoxyHb, .75) * Vb + base(waves) * (1. - Vb)) * (1. - W) + W * Water(waves, water)
    ax.semilogy(waves, mua, label="Hypodermis")


plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=16)

fig, ax = plt.subplots()

xs = np.linspace(200, 700, 500)

water = readFile("/home/lewis/phdshizz/Ga-salvo-2018/res/water absor.dat")
OxyHb = readFile("/home/lewis/phdshizz/Ga-salvo-2018/res/Oxy-Hb.dat")
DeoxyHb = readFile("/home/lewis/phdshizz/Ga-salvo-2018/res/Deoxy-Hb.dat")
Caro = readFile("/home/lewis/phdshizz/Ga-salvo-2018/res/B-carotene.dat")
Bili = readFile("/home/lewis/phdshizz/Ga-salvo-2018/res/bilirubin.dat")


# plt.plot(xs, base(xs), label="Baseline")
# plt.plot(xs, eumel(xs), label="Melanin")
# plt.plot(xs, Oxy_Hb(xs, OxyHb), label="Oxygenated blood")
# plt.plot(xs, DeOxy_Hb(xs, DeoxyHb), label="Deoxygenated blood")
# plt.plot(xs, Water(xs, water), label="Water")
# plt.semilogy(xs[:320], Bilirubin(xs[:320], Bili), label="Bilirubin")
# plt.plot(xs[:320], Bcarotene(xs[:320], Caro), label=r"$\beta$-Carotene")

stratum(xs, base, water)
epidermis(xs, water, Caro)
pap(xs, water, Caro, Bili, DeoxyHb, OxyHb)
ret(xs, water, Caro, Bili, DeoxyHb, OxyHb)
hypo(xs, water, Caro, Bili, DeoxyHb, OxyHb)


ax.set_ylabel(r"Absorption coefficient/$cm^{-1}$")
ax.set_xlabel(r"Wavelength/nm")

# files = ["bin/hypo.dat", "bin/stratum.dat", "bin/epi.dat", "bin/pap.dat", "bin/ret.dat"]
# for file in files:
#     print(file)
#     x, mus, mua = np.loadtxt(file, unpack=True)
#     plt.plot(x, mua, label=file[:-4])

width = 6.510  # inches
height = width / 1.618


fig.subplots_adjust(left=.1, bottom=.13, right=.99, top=.99)
ax.legend()

fig.set_size_inches(width, height)
fig.savefig('absorbs-1.pdf')
plt.show()
