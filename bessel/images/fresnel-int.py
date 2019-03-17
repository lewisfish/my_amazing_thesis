#!/home/lewis/anaconda3/bin/python
import numpy as np
import matplotlib.pylab as plt
from scipy.special import fresnel
import argparse


def getInt(x, y, y1, y2, z1, z2, fact):
    """
        get intensity at a point a1, b1 from the centre
        from hecht p520-522 5th ed
    """
    u1 = fact * (y1 + x)
    u2 = fact * (y2 + x)
    v1 = fact * (z1 + y)
    v2 = fact * (z2 + y)
    return intp(u1, u2, v1, v2)


def intp(u1, u2, v1, v2):
    """
        get intensity for a point x, y
    """
    fresu1 = fresnel(u1)
    fresu2 = fresnel(u2)
    fresv1 = fresnel(v1)
    fresv2 = fresnel(v2)
    ip = ((fresu2[1] - fresu1[1])**2 + ((fresu2[0] - fresu1[0])**2)) * ((fresv2[1] - fresv1[1])**2 + (fresv2[0] - fresv1[0])**2)
    return ip / 4.

parser = argparse.ArgumentParser(description="CLI program to calculate Fresnel diffraction")
parser.add_argument("wavelength", metavar="l", type=np.float64, help="wavelength of light in nm")
parser.add_argument("fnumber", metavar="F", type=np.float64, help="Fresnel number")
parser.add_argument("apeture_width", metavar="a", type=np.float64, help="apeture width in um")
parser.add_argument("imagerange", metavar="r", type=np.float64, help="image range in um")
parser.add_argument("pixels", metavar="a", type=int, help="Number of pixels")
parser.add_argument("-filename", metavar="f", type=str, help="Name of output file", default="test.out")

args = parser.parse_args()

wave = args.wavelength * 1e-9
# apeture width
a = args.apeture_width * 1e-6

# Fresnel number
F = args.fnumber
r0 = (a**2 * 2.) / (F**2 * wave)

# set coordinates based on apeture. they are the corners. 0 is the centre
y1 = -a / 2.
y2 = -y1
z1 = y1
z2 = y2

fact = np.sqrt(2. / (wave * r0))

# grid computation takes place on
xs = np.linspace(-args.imagerange * 1e-6, args.imagerange * 1e-6, args.pixels)
zs = xs
xv, zv = np.meshgrid(xs, zs)

fs = getInt(xv, zv, y1, y2, z1, z2, fact)
# plt.imshow(fs)
np.savetxt(args.filename, np.transpose([xs * 1e6, fs[:, int(args.pixels / 2)] / np.amax(fs[:, int(args.pixels / 2)])]))
plt.show()
