
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
# Normal graph
plt.plot(xpoints, ypoints)
plt.show()


# Graph with different styled lines
plt.plot(xpoints, ypoints, linestyle = "dotted") # linestyle allows you to edit how the line appears
# it can also be written shorthand with ls = ":"
plt.show()

# you can also edit the colour 
plt.plot(xpoints, ypoints, color = "r") # instead of r your can use hexidecimal values
plt.show()

# Graph with differently sized lines
plt.plot(xpoints, ypoints, linewidth = "22.5")
plt.show()


# Multiple Lines on One Graph
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()