import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Generate random data
n = 10
g1 = (0.1+0.2*np.random.rand(n),
      np.random.rand(n), 0.4+0.1*np.random.rand(n))
g2 = (0.7+0.9*np.random.rand(n),
      0.2*np.random.rand(n), 0.51*np.random.rand(n))
g3 = (0.6*np.random.rand(n),
      0.7*np.random.rand(n), 0.4+0.1*np.random.rand(n))

#Create visualisation
data = (g1,g2,g3)
print(type(data), data)
colours = ("green", "orange", "purple")
groups = ("A", "B", "C")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#get the current 3D axes on the figure
ax = fig.gca(projection="3d")

for  data, colour, group in zip(data, colours, groups):
    x, y, z = data
    ax.scatter(x, y, z, alpha = 1, c = colour, edgecolors = "none",
               s = 35, label = group)
    
ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_zlabel("Z label") 

plt.title("3D scatter plot example")
plt.legend(loc = 2)
plt.show()