import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np

width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=12)

fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=.097, bottom=.1, right=.985, top=.985, wspace=.0)

file = "/home/lewis/phdshizz/pMC/data/jmean/bvsg/int-b-0.015-0.00-0.0005.raw"
data = np.fromfile(file=file, sep="", dtype=np.float64)
data = data.reshape((100, 100, 300), order="F")

axs[0, 0].imshow(data[:, 50, :], extent=[-0.5, 0.05, 0, .15])  # sideways
axs[0, 1].imshow(data[:, :, 299], extent=[-0.5, 0.05, -0.5, 0.05], aspect="auto")  # top

axs[1, 0].imshow(data[:, :, 270], extent=[-0.5, 0.05, -0.5, 0.05], aspect="auto")  # mid
axs[1, 1].imshow(data[:, :, 0], extent=[-0.5, 0.05, -0.5, 0.05], aspect="auto")  # bottom

axs[1, 0].set_xlabel("Distance/mm")
axs[1, 0].set_ylabel("Distance/mm")

axs[1, 1].set_xticks([], [])
axs[0, 1].set_xticks([], [])
axs[0, 1].set_yticks([], [])
axs[1, 1].set_yticks([], [])

fig.set_size_inches(width, height)
fig.savefig('selfheal.pdf')
plt.show()
