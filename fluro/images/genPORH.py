import matplotlib as mpl
mpl.use('pdf')
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=15)

fig, ax1 = plt.subplots()
fig.subplots_adjust(left=.05, bottom=.1, right=.94, top=.99)


data = np.random.normal(scale=0.1, size=1000)
time = np.linspace(0., 15., 1000)
data = np.where(time >= 1, np.where(time <= 4, data, 2 + data), 2 + data)
datap = signal.savgol_filter(data[:300], 61, 8)
data[:300] = datap
data = np.where(time > 4, np.where(time < 5, data + 5, data), data)
data = np.where(time > 5, np.where(time < 6, data + 2, data), data)
data = np.where(time > 6, np.where(time < 7, data + 1, data), data)
data[300:] = signal.savgol_filter(data[300:], 101, 2)
data = signal.medfilt(data, 1)
a = ax1.plot(time, data, color=u"#1f77b4", label="Perfusion during PORH")
ax1.set_xlabel("time/min")
ax1.set_ylabel("Perfusion/AU")

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
data = np.random.normal(scale=0.1, size=1000) + 3
data = np.where(time >= 1, np.where(time <= 2, 1 + data, data), data)
data = np.where(time >= 2, np.where(time <= 3, 2 + data, data), data)
data = np.where(time >= 3, np.where(time <= 4, 2.5 + data, data), data)

data = np.where(time > 4, np.where(time <= 5, data - 2.5, data), data)
data = np.where(time > 5, np.where(time <= 5.5, data - 1, data), data)
data = signal.savgol_filter(data, 51, 3)

b = ax2.plot(time, data, color=u"#ff7f0e", label="Fluorescence during PORH")
ax2.set_ylabel("Fluorescence intensity/AU")

ab = a + b
labs = [l.get_label() for l in ab]
ax1.legend(ab, labs, loc=0)

fig.set_size_inches(width, height)
fig.savefig('porh-example.pdf')
plt.show()
