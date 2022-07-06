import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

# make up some data
x = np.random.rand(200)
y = np.random.rand(200)
z = np.random.rand(200)

# set up the figure
fig = plt.figure(figsize=(10,8))
ax = fig.gca(projection='3d')

# create the heatmap
ax.scatter3D(x, y, z)

# format the axes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


# add a title
ax.set_title('A random distribution')
plt.savefig('scatter3d.png')