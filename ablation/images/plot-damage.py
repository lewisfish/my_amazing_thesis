#!/home/lewis/anaconda3/bin/python3.6
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np
import matplotlib.ticker as ticker

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=12)

fig, ax = plt.subplots()
# stylize_axes(ax)
fig.subplots_adjust(left=.10, bottom=.15, right=.99, top=.92)

voxels = 80
shape = (voxels, voxels, voxels)
zmax2 = .09e-2
xmax2 = .03e-2
ymax2 = .03e-2

file = "damage.dat"

f = open(file, "rb")
data = np.fromfile(file=f, dtype=np.float64, sep="")
f.close()
data = data.reshape(shape)
slic = data[::-1, :, :]
slic = slic[1:44, 42, :]
levels = np.arange(0, 10, 1)

masked = np.ma.masked_where(slic == -1, slic, copy=True)

im = ax.imshow(masked, aspect="auto", extent=[(-xmax2 / 2.) * 1000, (xmax2 / 2.) * 1000, zmax2 * 1000, 0.])

cbar = fig.colorbar(im)
cbar.set_label(r"Degree of burn")

ax.set_ylabel("Vertical distance/mm")
ax.set_xlabel("Horizontal distance/mm")

hres = xmax2
vres = zmax2
# plt.gca().invert_yaxis()

# ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * hres))
# ax.xaxis.set_major_formatter(ticks)
# ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y * vres))
# ax.yaxis.set_major_formatter(ticks)

ax.set_title(r"P=70, $T_a$=338, $E_p$=400")
fig.set_size_inches(width, height)
fig.savefig("damage-slice.pdf")
plt.show()
