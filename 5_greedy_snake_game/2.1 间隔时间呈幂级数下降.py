import numpy as np
import pylab as plt

intervals = []
delta = 190
L = 100
for i in range(L):
    interval = delta + 10
    intervals.append(interval)
    delta *= 0.95
speeds = 1 / (np.array(intervals) / 1000)
plt.plot(range(L), intervals, label="interval time (ms)")
plt.plot(range(L), speeds, label="speed (pixel / second)")
plt.xlabel("length of snake")
plt.ylabel("interval time (ms)")
plt.grid(alpha=0.5)
plt.legend(loc="best")
plt.savefig("figure.png")
plt.show()
