import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.pyplot import figure, show
from numpy.random import rand
import matplotlib.image as mpimg
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from matplotlib._png import read_png


def visualize():
    fig = plt.figure()

    ax = plt.axes()

    points_with_annotation = []

    themap = Basemap(projection='gall',
                llcrnrlon = -180,
                llcrnrlat = -90,
                urcrnrlon = 180,
                urcrnrlat = 90,
                resolution = 'l',
                area_thresh = 100000.0,
                )

    themap.drawcoastlines()
    themap.drawcountries()
    themap.fillcontinents(color = 'gainsboro')
    themap.drawmapboundary(fill_color='steelblue')

    #site 1
    x1, y1 = themap(0,44)
    point, = themap.plot(x1, y1, 'o', color='Red',markersize=10)
    fn = get_sample_data("/Users/rogpaxton/Galvanize/SiteMetrics/plot44.0.png", asfileobj=False)
    arr_lena = read_png(fn)
    imagebox = OffsetImage(arr_lena, zoom=0.5)
    xy1 = (0, 44)

    annotation = AnnotationBbox(imagebox, xy1,
                        xybox=(50, 150),
                        xycoords='data',
                        boxcoords="offset points",
                        pad=0.5,
                        arrowprops=dict(arrowstyle="->",
                                        #connectionstyle="angle,angleA=0,angleB=90,rad=3")
                        ))

    annotation.set_visible(False)

    points_with_annotation.append([point, annotation])

    x2, y2 = themap(90,44)
    themap.plot(x2, y2,
            'o',                    # marker shape
            color='Red',         # marker colour
            markersize=6            # marker size
            )

    #site 2
    x2, y2 = themap(90,44)
    point, = themap.plot(x2, y2, 'o', color='Red',markersize=10)
    fn = get_sample_data("/Users/rogpaxton/Galvanize/SiteMetrics/plot45.0.png", asfileobj=False)
    arr_lena = read_png(fn)
    imagebox = OffsetImage(arr_lena, zoom=0.5)
    xy2 = (90, 44)

    annotation = AnnotationBbox(imagebox, xy2,
                        xybox=(50, 150),
                        xycoords='data',
                        boxcoords="offset points",
                        pad=0.5,
                        #arrowprops=dict(arrowstyle="->",
                                        #connectionstyle="angle,angleA=0,angleB=90,rad=3")
                        )

    annotation.set_visible(False)

    points_with_annotation.append([point, annotation])

    #site 3
    x3, y3 = themap(120,-34)
    point, = themap.plot(x3, y3, 'o', color='Red',markersize=10)
    fn = get_sample_data("/Users/rogpaxton/Galvanize/SiteMetrics/plot46.0.png", asfileobj=False)
    arr_lena = read_png(fn)
    imagebox = OffsetImage(arr_lena, zoom=0.5)
    #image = mpimg.imread("plot44.0.png")
    xy3 = (120, -34)

    annotation = AnnotationBbox(imagebox, xy3,
                        xybox=(50, 150),
                        xycoords='data',
                        boxcoords="offset points",
                        pad=0.5,
                        arrowprops=dict(arrowstyle="->",
                                        connectionstyle="angle,angleA=0,angleB=90,rad=3")
                        )

    annotation.set_visible(False)

    points_with_annotation.append([point, annotation])

    #Mouseover
    
    def on_move(event):
        visibility_changed = False
        for point, annotation in points_with_annotation:
            ax.add_artist(annotation)
            should_be_visible = (point.contains(event)[0] == True)

            if should_be_visible != annotation.get_visible():
                visibility_changed = True
                annotation.set_visible(should_be_visible)

        if visibility_changed:

            plt.draw()


    on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)


    plt.show()

if __name__ == '__main__':
    visualize()
