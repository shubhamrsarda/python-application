import folium
import pandas

#data=pandas.read_csv("airports.csv")
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elv=list(data["ELEV"])

map=folium.Map(location=[38.08,-99.09],zoom_start=6,tiles="Mapbox Bright")
def colour(elv):
    if elv<1000:
        return 'green'
    elif 1000<= elv <3000:
        return 'orange'
    else:
        return 'red'

fg=folium.FeatureGroup(name="My Map")
for la,lo,ti in zip(lat,lon,elv):
    #fg.add_child(folium.Marker(location=[la,lo],popup=str(ti)+"m",icon=folium.Icon(color=colour(ti))))
    fg.add_child(folium.CircleMarker(location=[la,lo],radius=6,popup=str(ti)+"m",fill_color=colour(ti),color='grey',fill_opacity=0.7))
map.add_child(fg)


map.save("Map1.html")
