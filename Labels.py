import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

 # You can also label the axis
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
# And add a title
plt.title("Health Stuff", loc = "left") # you can change where it appears by adding loc = "your_direction"

# You can also make a grid appear by adding 
plt.grid() # you can change which grid lines appear by adding axis = "x or y"
# You can also edit the way the grid lines appear with ls = "" and linewidth = ""

plt.show()