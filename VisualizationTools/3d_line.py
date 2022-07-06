import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# make up some data
z = np.linspace(0, 31.4, 1000)
x = np.sin(z)
y = np.cos(z)

# set up the figure
fig = plt.figure(figsize=(10,8))
ax = fig.gca(projection='3d')

# create the heatmap
ax.plot3D(x, y, z)

# format the axes
ax.set_xlabel('$sin(z)$')
ax.set_ylabel('$cos(z)$')
ax.set_zlabel('z')

# add a title
ax.set_title('A Spiral')

plt.savefig('3dline.png')