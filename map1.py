import folium
import pandas #gettting values from txt file

data = pandas.read_csv('Volcanoes.txt')
# getting values from colums of data i.e lat and lon,
lat = list(data['LAT'])
lan = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

#changing the color ddependi gupon elevatio value
def color_producer(elevation):
    if elevation < 1000:
      return 'green'
    elif 1000 <= elevation < 3000:
      return 'orange'
    else:
      return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain") 

fg = folium.FeatureGroup(name="my map")

# we need to iterate 1 to 1 corresponding from lat and lon, we use zip() in our looop

for lt, ln, el, name in zip(lat, lan, elev, name):
    iframe = folium.IFrame(html=html % (name,name,el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html")
