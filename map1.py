import folium
map = folium.Map(location=[51.1, -0.9], zoom_start=6, tiles="Stamen Terrain") 

fg = folium.FeatureGroup(name="my map")

for coordinates in [[50.2, -0.8],[55.1,-0.33],[51.5,-0.4],[56.6,-0.6]]:
    fg.add_child(folium.Marker(location=coordinates, popup="hi, i am a marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
