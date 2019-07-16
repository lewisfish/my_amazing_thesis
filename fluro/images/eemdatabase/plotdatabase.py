import numpy as np
import matplotlib.pyplot as plt
import glob as gb

files = gb.glob("*.txt")
files.sort()
cor = ["FAD_eem.txt"]
for file in files:
    eem = []
    excite = []

    with open(file, "r") as infile:
        lines = infile.readlines()
    emit = [float(i) for i in lines[0].split(" ")]

    eem = np.loadtxt(file, skiprows=1)
    eem = np.array(eem)
    eem = eem.reshape((28, 100))
    excite = eem[:, 0][::-1]
    eem = eem[:, 1:]

    # plt.imshow(eem, extent=[emit[0], emit[-1], excite[0], excite[-1]], interpolation="gaussian")

    val = len(excite) - np.searchsorted(excite, 365) + 1
    x1 = eem[val - 1, :]
    x2 = eem[val, :]
    prop = (x2 + x1) / 2
    if file in cor:
        prop /= np.amax(prop)
        plt.plot(emit, prop, label=file[:-8])
plt.legend()
plt.show()
