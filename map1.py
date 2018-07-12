import folium
import pandas
map=folium.Map(location=[30.58,-99.09],zoom_start=0,tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="volcanoes")
#adding marker
#fg.add_child(folium.Marker(location=[30.58,-99.09],popup="hi i am a marker",icon=folium.Icon(color='green')))

#add multiple AwesomeMarkers
#for coordinates in [[30.58,-78],[30,-93]]:
#    fg.add_child(folium.Marker(location=coordinates,popup="hi i am a marker",icon=folium.Icon(color='green')))

#adding data fro data files
data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def color_produce(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'


#for lt,ln,el in zip(lat,lon,elev):
#    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+'m',icon=folium.Icon(color=color_produce(el))))
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+'m',fill_color=color_produce(el),fill=True,color='grey',fill_opacity=0.7))
#adding third layer -- polygon layer best to represent area
#represent world population by country
fgp = folium.FeatureGroup(name="Population")
#adding population
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("m1.html")
