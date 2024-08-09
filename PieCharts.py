import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15]) # percentages
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# starts East

plt.pie(y, labels = mylabels)
plt.show() 

# You can also get a part of the pie chart to seperate
explode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = explode, shadow = True) # the shadow makes it look cool
plt.show() 