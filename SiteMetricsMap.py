import folium

#Color
#map_osm = folium.Map(location=[45.5236, -122.6750])
#map_osm.save('osm.html')

#B&W
#stamen = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner', zoom_start=13)
#stamen.save('stamen_toner.html')

#Pin Marker
#map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12,
#                   tiles='Stamen Terrain')
#folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows').add_to(map_1)
#folium.Marker([45.3311, -121.7113], popup='Timberline Lodge').add_to(map_1)
#map_1.save('mthood.html')

#Circle Marker
#map_2 = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner',
#                   zoom_start=13)
#folium.Marker(location=[45.5244, -122.6699], popup='The Waterfront').add_to(map_2)
#folium.CircleMarker(location=[45.5215, -122.6261], radius=50,
#                    popup='Laurelhurst Park', color='#3186cc',
#                    fill_color='#3186cc').add_to(map_2)
#map_2.save('portland.html')

#Vincent Visualization Marker
#Vis1, 2, and 3 are figures to pop up when site is clicked
import json

buoy_map = folium.Map(
    [46.3014, -123.7390],
    zoom_start=7,
    tiles='Stamen Terrain'
    )

#folium.RegularPolygonMarker(
    [47.3489, -124.708],
    fill_color='#43d9de',
    radius=12,
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open('vis1.json')), width=450, height=250))
    ).add_to(buoy_map)

folium.RegularPolygonMarker(
    [44.639, -124.5339],
    fill_color='#43d9de',
    radius=12,
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open('vis2.json')), width=450, height=250))
    ).add_to(buoy_map)

folium.RegularPolygonMarker(
    [46.216, -124.1280],
    fill_color='#43d9de',
    radius=12,
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open('vis3.json')), width=450, height=250))
    ).add_to(buoy_map)


buoy_map = folium.Map(location=[46.3014, -123.7390], zoom_start=7,
                      tiles='Stamen Terrain')
popup1 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(vis1, width=500, height=250))
folium.RegularPolygonMarker([47.3489, -124.708],
                     fill_color='#43d9de', radius=12, popup=popup1).add_to(buoy_map)
popup2 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(vis2, width=500, height=250))
folium.RegularPolygonMarker([44.639, -124.5339],
                     fill_color='#43d9de', radius=12, popup=popup2).add_to(buoy_map)
popup3 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(vis3, width=500, height=250))
folium.RegularPolygonMarker([46.216, -124.1280],
                     fill_color='#43d9de', radius=12, popup=popup3).add_to(buoy_map)
buoy_map.save('buoys.html')
