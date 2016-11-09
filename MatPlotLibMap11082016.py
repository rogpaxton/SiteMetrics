import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#[43,-100]

fig = plt.figure()
ax = plt.axes()

points_with_annotation = [(0, -44), 'note']
for i in range(10):
    point, = plt.plot(i, i, 'o', markersize=10)

#llcrnrlon=-180,llcrnrlat=-90, urcrnrlon=180 and urcrnrlat=90)

themap = Basemap(projection='gall',
              llcrnrlon = -180,              # lower-left corner longitude
              llcrnrlat = -90,               # lower-left corner latitude
              urcrnrlon = 180,               # upper-right corner longitude
              urcrnrlat = 90,               # upper-right corner latitude
              resolution = 'l',
              area_thresh = 100000.0,
              )

themap.drawcoastlines()
themap.drawcountries()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')

x, y = themap(0,44)
themap.plot(x, y,
            'o',                    # marker shape
            color='Red',         # marker colour
            markersize=6            # marker size
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
