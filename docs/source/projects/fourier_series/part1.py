import numpy as np
import matplotlib.pyplot as plt 


Fs = 1000
f0 = 1
t = np.arange(0, 1, 1/Fs)

L = 8
a = np.array([0, 1, 0, 1/3, 0, 1/5, 0, 1/7, 0])
phi = (np.pi/2)*np.ones(8)

x = np.zeros(len(t))
for l in range(L):
    x += a[l]*np.cos(2*np.pi*l*f0*t+phi[l])

plt.plot(t, x)
plt.xlabel("time [s]")
plt.ylabel("x(t)")
plt.show()