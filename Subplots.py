import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) # the figure has 1 row, 2 columns and this plot appears in the 1st position
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2) # the figure has 1 row, 2 columns and this plot appears in the 2nd position
plt.plot(x,y)


# here there are two different plots but as the .show() method is written after both the mini graphs they appear on one

plt.suptitle("Interesting") # you can also add a title to the figure
plt.show()