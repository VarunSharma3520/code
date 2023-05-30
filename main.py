<<<<<<< HEAD
a=input("Enter your name")
print(a)
=======

import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')

xpoints = np.array([2,9,8,5,4,3,4])
ypoints = np.array([0,2,5,9,6,3,4])

plt.plot(xpoints, ypoints)
# plt.pie(xpoints)

plt.show()

print("Hello World")

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

>>>>>>> 8f71937606a243d6666bddbd6e446611303d273b