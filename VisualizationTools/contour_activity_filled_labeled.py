import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable


# make up some data
x = np.linspace(-4.0, 4.0, 1000)
y = np.linspace(-4.0, 4.0, 1000)

# make a grid that is a combination of every x and every y
X, Y = np.meshgrid(x, y)
Z = np.sqrt(abs(X**3 + Y**3))

# set up the figure
fig = plt.figure(figsize=(8,8))
ax = fig.gca()

# create the heatmap
contour_filled = ax.contourf(X, Y, Z, levels=8, cmap='inferno_r')
contour_lines = ax.contour(X, Y, Z, levels=8, colors='black', linestyles='dashed')
plt.clabel(contour_lines, inline=True, fontsize=10)

# format the axes
ax.set_xlabel('Horizontal Position (in)')
ax.set_ylabel('Vertical Position (in)')

# add a title
ax.set_title('Onion Energy Field')


# create colorbar on a new an axis to the right of ax. The colorbar
# will be called cax. The width of cax will be 5% of ax
# and the padding between cax and ax will be fixed at .5 inches.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=.5)

cbar = fig.colorbar(contour_filled, cax=cax, label='Cubic Dispersion (OEUs)')

plt.savefig('contour_filled_labeled.png')