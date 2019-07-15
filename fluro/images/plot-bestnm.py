import numpy as np
import matplotlib.pyplot as plt

files = ["best_fluro.dat", "target-10d.dat"]
for file in files:
    x = np.loadtxt(file, unpack=True)
    plt.plot(x, label=file)

x = np.loadtxt("target-8.dat", unpack=True)
plt.plot(x, linestyle="--", color="k", zorder=0, label="full target")
plt.ylim(0, 1.)

plt.legend()
plt.show()
