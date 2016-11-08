import folium
from folium.element import IFrame
import pandas as pd
import numpy as np
import branca
import os

def mapper(data):
#    df = pd.read_csv(data)

    #draft map an location pins
#    m = folium.Map()

#    for each in df.iterrows():
#        m.circle_marker(location = [each[1]['Lat'], each[1]['Lon']], popup=each[1]['City'])

#    m.create_map(path='map.html')

    m = folium.Map([43,-100], zoom_start=4)

    f = open('html_test.html','w')

    html="""
        <!DOCTYPE html>
        <html>
            <h1> Popup for site location</h1>
            <br>
            <div>
                <img id="RC51" src="plot44.0.png" alt="RVT" style="width:400px;height:200px;">
            </div>
        </html>
        """

#src="file:///Users/rogpaxton/Galvanize/SiteMetrics/RC51.jpg"
#                    <img id="RC51" src="RC51.jpg" alt="RVT" style="width:48px;height:49px;">

    f.write(html)
    f.close()

    iframe = folium.element.IFrame(html=html, width=800, height=400)
#    iframe = folium.element.HTML(html=html, width=800, height=500)
    popup = folium.Popup(iframe, max_width=2650)
    print iframe

#    f = branca.element.Figure('plot44.0.png')
    f = branca.element.Figure()
    folium.Map([-25, 150], zoom_start=3).add_to(f)
    iframe = branca.element.IFrame(width=500, height=300)
    f.add_to(iframe)

    popup = folium.Popup(iframe, max_width=2650)
    m = folium.Map([43, -100], zoom_start=4)
    folium.Marker([30, -100], popup=popup).add_to(m)
    m.save(os.path.join('map_popups.html'))
    m

#    folium.Marker([30,-100], popup=popup).add_to(m)

#    m.create_map(path='map.html')

if __name__ == '__main__':
    map1 = mapper('data/example.csv')
