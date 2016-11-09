import folium
from folium.element import IFrame
import pandas as pd
import numpy as np

def mapper(data):

    m = folium.Map([43,-100], zoom_start=4)

    f = open('html_test.html','w')

    html="""
        <!DOCTYPE html>
        <html>
            <h1> Site Metrics</h1>
            <br>
            <div style="width:400px;height:200px;background: url(plot44.0.png) center center no-repeat">
            </div>
        </html>
        """

    f.write(html)
    f.close()

    iframe = folium.element.IFrame(html=html, width=800, height=400)

    popup = folium.Popup(iframe, max_width=2650)
    print iframe

    folium.Marker([30,-100], popup=popup).add_to(m)

    m.create_map(path='map.html')

if __name__ == '__main__':
    map1 = mapper('data/example.csv')
