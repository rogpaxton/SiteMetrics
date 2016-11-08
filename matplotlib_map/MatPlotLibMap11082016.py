import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#[43,-100]

fig = plt.figure()
ax = plt.axes()

themap = Basemap(projection='gall',
              llcrnrlon = -15,              # lower-left corner longitude
              llcrnrlat = 28,               # lower-left corner latitude
              urcrnrlon = 45,               # upper-right corner longitude
              urcrnrlat = 73,               # upper-right corner latitude
              resolution = 'l',
              area_thresh = 100000.0,
              )

themap.drawcoastlines()
themap.drawcountries()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')

x, y = themap(0,44 )
themap.plot(x, y,
            'o',                    # marker shape
            color='Indigo',         # marker colour
            markersize=4            # marker size
            )

#mouseover message

annotation = ax.annotate("Mouseover point",
        xy=(0, 44), xycoords='data',
        textcoords='data',
        horizontalalignment="left",
        arrowprops=dict(arrowstyle="simple",
                        connectionstyle="arc3,rad=-0.2"),
        bbox=dict(boxstyle="round", facecolor="w",
                  edgecolor="0.5", alpha=0.9)
        )
    # by default, disable the annotation visibility
annotation.set_visible(False)

#mouseover function
visibility_changed = False
for point, annotation in points_with_annotation:
    should_be_visible = (point.contains(event)[0] == True)

    if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)

    if visibility_changed:
        plt.draw()


plt.show()
