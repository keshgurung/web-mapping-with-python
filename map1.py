import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain") 

fg = folium.FeatureGroup(name="my map")

fg.add_child(folium.Marker(location=[51.2,-0.76], popup="hi, i am a marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
