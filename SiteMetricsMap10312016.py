import folium
import pandas as pd
import numpy as np

def mapper(data):
    df = pd.read_csv(data)

    #draft map an location pins
    map = folium.Map()

    for each in df.iterrows():
        map.simple_marker(
            location = [each[1]['Lat'], each[1]['Lon']], popup=each[1]['Classification'])

    #user input to pop up information

#    import branca
#    import os

#    html = """
#        <h1> This is a big popup</h1><br>
#        With a few lines of code...
#        <p>
#        <code>
#            from numpy import *<br>
#            exp(-2*pi)
#        </code>
#        </p>
#        """

#    iframe = branca.element.IFrame(html=html, width=500, height=300)
#    popup = folium.Popup(iframe, max_width=2650)

#    for each in df.iterrows():
#        map.simple_marker(
#            location = [each[1]['Lat'], each[1]['Lon']], popup=each[1]['Classification'])

#    folium.Marker([30, -100], popup=popup).add_to(map)

#    map.save(os.path.join('results', 'html_popups.html'))

#    args = sys.argv






    map.create_map(path='map.html')

if __name__ == '__main__':
    map1 = mapper('data/example.csv')
