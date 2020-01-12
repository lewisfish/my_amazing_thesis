# #!/home/lewis/anaconda3/bin/python
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np


width = 6.510  # inches
height = width / 1.618

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=12)


fig, ax = plt.subplots()
fig.subplots_adjust(left=.12, bottom=.12, right=.99, top=.95)
xmax = .02
zmax = .3
waist = 0.5
# file = "/home/lewis/phdshizz/bessel beam/data/jmean/phase-g-0.015-0.00-0.0005.raw"
file = "/home/lewis/phdshizz/bessel beam/data/jmean/int-g-0.015-0.00-0.0015.raw"
data = np.fromfile(file, sep="", dtype=np.float64)
data = data.reshape((100, 100, 200), order="F")

im = ax.imshow(data[:, 50, :], aspect="auto", extent=[2.0, 0.0, -10, 10])
# ax.set_yticks([])
# ax.set_xticks([])

ax.set_xlabel("Depth/mm")
ax.set_ylabel(r"Width/$\mu$m")
cbar = fig.colorbar(im)
cbar.set_label("Intensity/arb.")

fig.set_size_inches(width, height)
fig.savefig('spherabbr.pdf')
plt.show()
