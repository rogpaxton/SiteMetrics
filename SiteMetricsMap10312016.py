import folium
import pandas as pd
import numpy as np

def mapper(data):
    df = pd.read_csv(data)

    #draft map an location pins
    m = folium.Map()

    for each in df.iterrows():
        m.circle_marker(location = [each[1]['Lat'], each[1]['Lon']], popup=each[1]['City'])

    m.create_map(path='map.html')

    m = folium.Map([43,-100], zoom_start=4)

    html="""
        <!DOCTYPE html>
        <html>
        <body>
        <h1> This is a big popup</h1><br>
        <div>
        <img id="RC51" src="/Users/rogpaxton/Galvanize/SiteMetrics/small_jpeg.jpg" alt="RVT" style="width:48px;height:49px;">
        </div>
        </body>
        </html>
        """
    iframe = folium.element.IFrame(html=html, width=500, height=300)
#    iframe = folium.element.HTML(html=html, width=800, height=500)
    popup = folium.Popup(iframe, max_width=2650)

    folium.Marker([30,-100], popup=popup).add_to(m)

    m.create_map(path='map.html')

if __name__ == '__main__':
    map1 = mapper('data/example.csv')
