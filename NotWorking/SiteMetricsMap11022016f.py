import folium
from folium.element import IFrame
import pandas as pd
import numpy as np

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
                <img src="plot44.0.png" id="RC51" alt="RVT" style="width:400px;height:200px;">
            </div>
        </html>
        """

#src="file:///Users/rogpaxton/Galvanize/SiteMetrics/RC51.jpg"
#                    <img id="RC51" src="RC51.jpg" alt="RVT" style="width:48px;height:49px;">

    f.write(html)
    f.close()

    html2="""
    <iframe frameborder="0" scrolling="no" width="100%" height="100%"
   src="../images/eightball.gif" name="imgbox" id="imgbox">
   <p>iframes are not supported by your browser.</p>
   </iframe><br />
   """

    iframe = folium.element.IFrame(html=html2, width=800, height=400)
#    iframe = folium.element.HTML(html=html, width=800, height=500)
    popup = folium.Popup(iframe, max_width=2650)

    folium.Marker([30,-100], popup=popup).add_to(m)

    m.create_map(path='map.html')

if __name__ == '__main__':
    map1 = mapper('data/example.csv')
