import folium
from folium.element import IFrame
import pandas as pd
import numpy as np
import branca
import os

f = branca.element.Figure()
folium.Map([-25, 150], zoom_start=3).add_to(f)

# Let's put the figure into an IFrame.
iframe = branca.element.IFrame(width=500, height=300)
f.add_to(iframe)

# Let's put the IFrame in a Popup
popup = folium.Popup(iframe, max_width=2650)

# Let's create another map.
m = folium.Map([43, -100], zoom_start=4)

# Let's put the Popup on a marker, in the second map.
folium.Marker([30, -100], popup=popup).add_to(m)

# We get a map in a Popup. Not really useful, but powerful.
m.save(os.path.join('map_popups.html'))

m
