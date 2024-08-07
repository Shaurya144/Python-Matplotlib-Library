# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.
# The function takes parameters for specifying points in the diagram.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8]) # this gives the starting and ending x coordinates
ypoints = np.array([3, 10])# this gives the starting and ending y coordinates

plt.plot(xpoints, ypoints)
plt.show()

# to plot without lines you use 'o', which means rings
plt.plot(xpoints, ypoints, 'o')
plt.show()

# you can plot multiple points by
moreXpoints = np.array([1, 3, 5, 7])
moreYpoints = np.array([5, 10, 15, 20])

plt.plot(moreXpoints, moreYpoints, marker = "*") # using marker = "*" you can make the points appear as *