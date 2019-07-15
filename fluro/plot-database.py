import matplotlib.pyplot as plt
import numpy as np

file = "database.dat"
f = open(file, "r")
lines = f.readlines()

exc = []
emit = []
for i in lines[0].split(" "):
    emit.append(float(i))

for line in lines[1:]:
    data = line.split(" ")
    exc.append(float(data[0]))
vals = []
for line in lines[1:]:
    data = line.split(" ")
    for i, datum in enumerate(data):
        if i > 0:
            vals.append(float(datum))

vals = np.array(vals)
vals = vals.reshape((28, 99))
xs = np.linspace(260, 750, 99)
plt.plot(xs, vals[16, :])
plt.plot(xs, vals[17, :])
plt.plot(xs, vals[15, :])

# plt.imshow(vals, extent=[emit[0], emit[-1], exc[-1], exc[0]], interpolation="gaussian")
plt.show()
