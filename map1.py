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
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(iframe), radius=8 ,fill_color=color_producer(el), color='grey', fill_opacity=0.7))
#folium.Circlemaker = gives circle icon, radius = size of circle, fill_color = inside the circle, color = circle border, opacity = to show the fill_color

#add a child that creates a polygon around country and reads json file.
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if
10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fg)

map.save("Map1.html")
