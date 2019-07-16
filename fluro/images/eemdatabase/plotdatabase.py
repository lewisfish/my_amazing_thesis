import numpy as np
import matplotlib.pyplot as plt

file = "Elastin_eem.txt"
file2 = "nadh-emit.dat"
x, y = np.loadtxt(file2, unpack=True)

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
plt.plot(emit, prop / np.amax(prop))
plt.plot(emit, x2 / np.amax(x2))
plt.plot(emit, x1 / np.amax(x1))
# plt.plot(x, y)
plt.show()
