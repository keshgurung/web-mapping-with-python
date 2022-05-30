# web-mapping-with-python

This is a python web application that shows population and volcanos from a given map.

### Procedures

- `npm3 install folium` : Folium is a Python library that makes it possible visualize data on an interactive Leaflet map.

- goto python3 in terminal
- > > > import folium
  > > > map = folium.Map(location=[80, -100])
  > > > map
  > > > <folium.folium.Map object at 0x10d686040>
  > > > map.save("Map1.html")
- This will save a file in our folder and we can view in the browser. to change simply do this,

  > > > map = folium.Map(location=[51.2, -0.76], zoom_start=6)
  > > > map.save("Map1.html")

- We have been given a .txt file with valcanos data in it. We will extract (lat, lon) data from the file using pandas. `pip3 install panda`

```
>>> import pandas
>>> data1= pandas.read-csv('Volcanoes.txt)
  # to view columns
>>> data.columns
>>> lat = list(data['LAT'])
>>> lat gives all latitude files

```
