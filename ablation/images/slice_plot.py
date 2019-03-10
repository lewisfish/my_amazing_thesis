#!/home/lewis/anaconda3/bin/python3.6
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec  # GRIDSPEC !


def add_inner_title(ax, title, loc, size=None, **kwargs):
    from matplotlib.offsetbox import AnchoredText
    from matplotlib.patheffects import withStroke
    if size is None:
        size = dict(size=plt.rcParams['legend.fontsize'])
    at = AnchoredText(title, loc=loc, prop=size,
                      pad=0., borderpad=0.5,
                      frameon=False, **kwargs)
    ax.add_artist(at)
    at.txt._text.set_path_effects([withStroke(foreground="w", linewidth=3)])
    return at

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)

fig = plt.figure()
plt.subplots_adjust(hspace=0.2, wspace=0.01)
gs = gridspec.GridSpec(1, 3, height_ratios=[1.0], width_ratios=[1.0, 1.0, 0.08])

# first graph
ax1 = plt.subplot(gs[0, 0])

# second graph
ax2 = plt.subplot(gs[0, 1])
ax3 = plt.subplot(gs[0, 2])

# plt.pcolor(df2, cmap='Greys')


voxels = 240
shape = (voxels, voxels, voxels)
zmax2 = .2e-2
xmax2 = 1.2e-2
ymax2 = 1.2e-2

file = "rhokap-timestep-test2-240-300-400.dat"

f = open(file, "rb")
data = np.fromfile(file=f, dtype=np.float64, sep="")
f.close()
data = data.reshape(shape, order='F')
slic = data[43, :, :]

im1 = ax1.imshow(slic, aspect="auto")

im2 = ax2.imshow(data[:, :, 239], aspect="auto")
cbar = plt.colorbar(im2, cax=ax3)
cbar.set_label(r"Absorption coiefficent/cm$^{-1}$")

ax1.set_xlabel("Vertical distance/cm")
ax1.set_ylabel("Horizontal distance/cm")

ax2.set_xlabel("Vertical distance/cm")
# ax2.set_ylabel("Horizontal distance/cm")

ax2.axes.get_yaxis().set_visible(False)

hres = 8.e-4
vres = 5e-3

ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * hres))
ax1.xaxis.set_major_formatter(ticks)
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y * vres))
ax1.yaxis.set_major_formatter(ticks)


ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y * vres))
ax2.xaxis.set_major_formatter(ticks)
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y * vres))
ax2.yaxis.set_major_formatter(ticks)

list1 = ["a)", "b)"]
for ax, text in zip([ax1, ax2], list1):
    t = add_inner_title(ax, text, loc=2)
    t.patch.set_alpha(0.5)

fig.set_size_inches(width, height)
fig.savefig("slice.pdf")
plt.show()
