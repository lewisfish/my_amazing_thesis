#!/home/lewis/anaconda3/bin/python
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pylab as plt
import numpy as np
import glob as gb
import matplotlib.gridspec as gridspec
from matplotlib.colorbar import Colorbar
from matplotlib.patches import Polygon


def tri(t):
    m = pwr / pulseLength
    c = 2. * pwr
    if t >= pulseLength:
        return max(0., -m * t + c)
    else:
        return min(pwr, m * t)
    return n

width = 6.510  # inches
height = width / 1.618

# plt.rc('font', family='serif', serif='Times')
# plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('axes', labelsize=10)
fig, ax = plt.subplots()

gs = gridspec.GridSpec(2, 2, height_ratios=[1.0, .2], width_ratios=[1.0, 0.025])
plt.subplots_adjust(top=0.979, bottom=0.1, left=0.096, right=0.9, hspace=0.064, wspace=0.039)

ax1 = plt.subplot(gs[0, 0])
cbax = plt.subplot(gs[:, 1])
ax3 = plt.subplot(gs[1, 0])

files = gb.glob("temp-*.dat")
files.sort()

t = np.linspace(0, 2, 1000)
pwr = 70
pulseLength = 0.4628571429

array = []
for file in files:
    data = np.fromfile(file=file, dtype=np.float64, sep="")
    data = data.reshape((82, 82, 82), order="F")
    data = data[1:81, 1:81, 1:81]
    array.append(data[40, 40, ::-1] - 273.15)

array = np.transpose(np.array(array))

pl = ax1.imshow(array, aspect="auto", extent=[0, 2, 0.16, .0])
ax1.set_ylabel("Depth/cm")
ax1.set_xticks([])

verts = np.where(array > 450, 1, 0)
verts = (verts!=0).argmax(axis=1)
for i in range(array.shape[1] - len(verts)):
    verts = np.append(verts, 0)


dx = 2. / (array.shape[1])
dy = .16 / (array.shape[0])

xs = []
ys = []
for j, i in enumerate(verts):
    if i != 0:
        xs.append(i*dx)
        ys.append(j*dy)
    else:
        if len(xs) == 0:
            xs.append(0)
            ys.append(0)
        else:
            xs.append(min(2, xs[-1]+dx))
            ys.append(ys[-1])

verts = [*zip(xs, ys), (2., 0)]

poly = Polygon(verts, facecolor='0.9', edgecolor="red", alpha=0.4, hatch="/", linewidth=3)
ax1.add_patch(poly)

ax3.plot(t, list(map(tri, t)))
ax3.set_xlabel("Time/s")
ax3.set_ylabel("Power/W")
ax3.set_xlim(0, 2)
ax3.set_ylim(0,)

cb = Colorbar(ax=cbax, mappable=pl)
cb.set_label("Temperature/C")
fig.set_size_inches(width, height)
fig.savefig('temp-profile-middle.pdf')
plt.show()
