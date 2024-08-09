import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"]) # these are your labels for the bars
y = np.array([3, 8, 1, 10]) # these are the values

plt.bar(x,y)
plt.show()