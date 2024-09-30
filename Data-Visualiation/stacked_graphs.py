import numpy as np
import matplotlib.pyplot as plt

#Generate random data
groupOne = np.random.randint(1,10,10)
groupTwo = np.random.randint(1,10,10)
groupThree = np.random.randint(1,10,10)

#Creating the stacked area
y = np.row_stack((groupOne, groupTwo, groupThree))
x = np.arange(10)

y1, y2, y3 = (groupOne, groupTwo, groupThree)

fig, ax = plt.subplots()
ax.stackplot(x,y)

plt.title("Stacked area chart example")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()