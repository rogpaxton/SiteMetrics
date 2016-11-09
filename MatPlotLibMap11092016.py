import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.pyplot import figure, show
from numpy.random import rand
import matplotlib.image as mpimg


#image = mpimg.imread("plot44.0.png")
#plt.imshow(image)
#plt.show()


fig = plt.figure()
ax = plt.axes()

points_with_annotation = []
#for i in range(10):
#    point, = plt.plot(i, i, 'o', markersize=10)

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

#Mouseover

#for i in range(10):
x, y = themap(0,44)
point, = themap.plot(x, y, 'o', color='Blue',markersize=10)

annotation = ax.annotate("Mouseover point",
    xy=(x, y), xycoords='data',
    xytext=(0, 44), textcoords='data',
    horizontalalignment="left",
    arrowprops=dict(arrowstyle="simple",
                        connectionstyle="arc3,rad=-0.2"),
    bbox=dict(boxstyle="round", facecolor="w",
                  edgecolor="0.5", alpha=0.9)
    )
    # by default, disable the annotation visibility
annotation.set_visible(False)

points_with_annotation.append([point, annotation])


def on_move(event):
    visibility_changed = False
    for point, annotation in points_with_annotation:
        should_be_visible = (point.contains(event)[0] == True)

        if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)


    if visibility_changed:
#        plt.draw()
        image = mpimg.imread("plot44.0.png")
        plt.imshow(image)
        plt.draw()

on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()