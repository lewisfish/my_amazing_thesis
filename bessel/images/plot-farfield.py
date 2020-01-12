import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np

width = 6.510  # inches
height = width

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=12)

xmax = 1.5
extr = [-xmax, xmax, -xmax, xmax]

fig, ax = plt.subplots()
fig.subplots_adjust(left=.097, bottom=.1, right=.985, top=.985)

file = "bessel-farfield.dat"
data = np.fromfile(file=file, dtype=np.float64, sep="")
data = data.reshape((501, 501))
ax.imshow(data, aspect="auto", extent=extr)
ax.set_xlabel("Position/mm")
ax.set_ylabel("Position/mm")

fig.set_size_inches(width, height)
fig.savefig('farfield.pdf')
plt.show()
