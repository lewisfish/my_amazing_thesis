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
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)

fig, ax = plt.subplots()
# stylize_axes(ax)
fig.subplots_adjust(left=.10, bottom=.10, right=.90, top=.90)

voxels = 80
shape = (voxels, voxels, voxels)
zmax2 = .09e-2
xmax2 = .03e-2
ymax2 = .03e-2

file = "damage.dat"

f = open(file, "rb")
data = np.fromfile(file=f, dtype=np.float64, sep="")
f.close()
data = data.reshape(shape, order='F')
slic = data[42, :, 35:79]

levels = np.arange(0, 10, 1)

masked = np.ma.masked_where(slic == -1, slic, copy=True)

im = ax.imshow(masked, aspect="auto")

cbar = fig.colorbar(im)
cbar.set_label(r"Thermal tissue damage")

ax.set_xlabel("Vertical distance/cm")
ax.set_ylabel("Horizontal distance/cm")

hres = 44. * 2. * zmax2
vres = voxels * 2. * xmax2
plt.gca().invert_yaxis()

ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * hres))
ax.xaxis.set_major_formatter(ticks)
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y * vres))
ax.yaxis.set_major_formatter(ticks)


fig.set_size_inches(width, height)
fig.savefig("slice.pdf")
plt.show()
