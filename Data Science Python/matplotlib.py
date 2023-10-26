import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([2,9,8,5,4,3,4])
ypoints = np.array([0,2,5,9,6,3,4])

plt.plot(xpoints, ypoints)

# plt.show()
plt.savefig('plotlib.png',dpi=300)



