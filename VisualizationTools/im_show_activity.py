import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Data processing
heatwave = pd.read_csv('Project/heatwave.csv')
searches = heatwave.columns.values
data = heatwave[searches[1:]].values
data = data.transpose()
dates = heatwave[searches[0]]

# set up the figure
fig = plt.figure(figsize=(14,6))
ax = fig.gca()

# create the heatmap
im = ax.imshow(data, cmap='RdYlBu_r')

# Set up ticks:
#  y-axis will have each categoy
#  x-axis will have dates
ax.set_xticks(np.arange(0,len(dates),7))
ax.set_yticks(np.arange(len(searches[1:])))
ax.set_xticklabels(dates[::7])
ax.set_yticklabels(searches[1:])

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# fix a small bug that only plots half of the first and last row
ax.set_ylim(-.5 ,8.5)

# set the title
ax.set_title("Google trends summer, 2018", fontsize=14)

# create colorbar on a new an axis below ax. The colorbar
# will be called cax the width of cax will be 12.5% of ax
#  and the padding between cax and ax will be fixed at 1.2 inches.
divider = make_axes_locatable(ax)
cax = divider.append_axes("bottom", size="12.5%", pad=1.2)

cbar = fig.colorbar(im, cax=cax, label='Search Interest Index', 
orientation='horizontal')
cbar.set_label('Search Interest Index', labelpad=-50, 
rotation=0, fontsize=12)

# save the figure
fig.tight_layout()
plt.show()