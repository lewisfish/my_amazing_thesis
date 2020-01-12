import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np


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

# plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('axes', labelsize=12)

fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=.11, bottom=.12, right=.999, top=.985, wspace=.3, hspace=0.3)

file = "/home/lewis/phdshizz/bessel beam/data/jmean/selfheal-int-b-0.015-0.00-0.0005.raw"
data = np.fromfile(file=file, sep="", dtype=np.float64)
data = data.reshape((100, 100, 200), order="F")

axs[0, 0].imshow(data[:, 50, :], extent=[.15, .0, -.05, .05], aspect="auto")  # sideways
axs[0, 1].imshow(data[:, :, 199], extent=[-0.05, 0.05, -0.5, 0.05], aspect="auto")  # top

axs[1, 0].imshow(data[:, :, 170], extent=[-0.05, 0.05, -0.05, 0.05], aspect="auto")  # mid
axs[1, 1].imshow(data[:, :, 0], extent=[-0.05, 0.05, -0.05, 0.05], aspect="auto")  # bottom

axs[1, 0].set_xlabel("Distance(x)/mm")
axs[1, 0].set_ylabel("Distance(y)/mm")
axs[1, 1].set_xlabel("Distance(x)/mm")
axs[1, 1].set_ylabel("Distance(y)/mm")

axs[0, 1].set_xlabel("Distance(x)/mm")
axs[0, 1].set_ylabel("Distance(y)/mm")

axs[0, 0].set_xlabel("Distance(y)/mm")
axs[0, 0].set_ylabel("Distance(z)/mm")

# axs[1, 1].set_xticks([], [])
# axs[0, 1].set_xticks([], [])
# axs[0, 1].set_yticks([], [])
# axs[1, 1].set_yticks([], [])

list1 = (r'a)', r'b)', r'c)', r'd)')
axs = axs.flatten()

for ax, text in zip(axs, list1):
    t = add_inner_title(ax, text, loc=2)
    t.patch.set_alpha(0.5)

fig.set_size_inches(width, height)
fig.savefig('selfheal.pdf')
plt.show()
