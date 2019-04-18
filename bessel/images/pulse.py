import numpy as np
import matplotlib.pylab as plt


def gauss(x, a, b, c):
    return a * np.exp(-(x - b)**2 / (2. * c**2))


def triangular(x, a):
    return a


def tophat(x, a, plength):
    if x > plength:
        return a
    else:
        return 0.


pwr = 70
pulsel = 0.25
t = np.linspace(0, 2., 1000)

sig = pulsel * np.sqrt(2. * np.log(2))
mean = pulsel * np.sqrt(2. * np.log(2))
plt.plot(t, gauss(t, pwr, mean, sig))
plt.plot(t, tophat(t, pwr, pulsel))
plt.show()
