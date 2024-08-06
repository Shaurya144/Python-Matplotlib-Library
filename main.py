# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
# Matplotlib was created by John D. Hunter.
# Matplotlib is open source and we can use it freely.
# Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

# import matplotlib # you start by importing the library first
# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
# so instead 
import matplotlib.pyplot as plt

# Now you can draw a line by
import numpy as np

xpoints = np.array([0, 6])   # -->
ypoints = np.array([0, 250]) # ^

plt.plot(xpoints, ypoints)
plt.show() # this is very fun to mess around with