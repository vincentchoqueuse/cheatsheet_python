import numpy as np 
import matplotlib.pyplot as plt

Fe = 1000
f = 15
a = 2

t = np.arange(0, 1, 1/Fe)  # create a numpy array
s = np.sin(2*np.pi*f*t)  # compute a numpy array
plt.plot(t, s)  # plot a function
plt.xlabel("t [s]")  # change the xlabel
plt.show()