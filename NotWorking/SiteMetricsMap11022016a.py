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
            <h1> Popup for site location</h1>
            <br>
            <div>
                <img src="plot44.0.png" alt="RVT" style="width:400px;height:200px;">
            </div>
        </html>
        """

    f.write(html)
    f.close()

    html2="""
        <body>
        <div>
            <iframe src="html_test.html" name="targetframe" allowTransparency="true" scrolling="no" frameborder="0" >
            </iframe>
        </div>
        </body>
        """

    iframe = folium.element.IFrame(html=html2, width=800, height=400)

    popup = folium.Popup(iframe, max_width=2650)

    html3 = folium.element.Html('plot44.0.png')

    popup = folium.Popup(html3)

    folium.Marker([30,-100], popup=popup).add_to(m)

    m.create_map(path='map.html')

if __name__ == '__main__':
    map1 = mapper('data/example.csv')
