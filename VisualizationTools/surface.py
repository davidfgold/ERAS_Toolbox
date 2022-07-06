import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# make up some data
x = np.linspace(-1.5, 1.5, 1000)
y = np.linspace(-1.5, 1.5, 1000)

# make a grid that is a combination of every x and every y
X, Y = np.meshgrid(x, y)
Z = np.sqrt((np.sin(X)**2 + np.cos(Y)**2))

# set up the figure
fig = plt.figure(figsize=(10,8))
ax = fig.gca(projection='3d')

# create the heatmap
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# format the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('$Z=sin(x)^2 + sin(y)^2$')

# add a title
ax.set_title('A Simple Trig Function')

fig.colorbar(surf, shrink=0.5, aspect=5, label = '$Z=sin(x)^2 + sin(y)^2$')

plt.savefig('Surface_plot.png')