import folium
import pandas #gettting values from txt file

data = pandas.read_csv('Volcanoes.txt')
# getting values from colums of data i.e lat and lon,
lat = list(data['LAT'])
lan = list(data['LON'])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain") 

fg = folium.FeatureGroup(name="my map")

# we need to iterate 1 to 1 corresponding from lat and lon, we use zip() in our looop

for lt, ln in zip(lat, lan):
    fg.add_child(folium.Marker(location=[lt,ln], popup="hi, i am a marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
