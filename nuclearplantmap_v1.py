from os import closerange
import folium
import pandas

data = pandas.read_csv("files\-nuclear-power-stations.csv")
data_json = pandas.read_json("files\world.json")

latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
name = list(data["Name"])
gross_capacity = list(data["Gross Capacity /MW"])

gross_cap_removed_commas = [i.replace(",", "") for i in gross_capacity]

gross_cap = [int(i) for i in gross_cap_removed_commas]

def color_producer(gc):
    if gc < 700:
        return "lightblue"
    elif 700 <= gc < 1200:
        return "blue"
    else:
        return "darkblue"

map = folium.Map(location = [50.78837912727776, 14.320049151545614], zoom_start=5, tiles= "CartoDB positron")    

fg = folium.FeatureGroup(name = "My nuclear map")

#here the zip function iterate the first item from both list, and creates a tuple with those two items. 

html = """
<h3><i>Nuclear Plant:</i><b></h3>
<h3><a href="https://www.google.com/search?q=nuclearplant%%22%s%%22" target="_blank">%s</a><b>.</h3>
"""

for lt, ln, nm, gc in zip(latitude, longitude, name, gross_cap):
    iframe = folium.IFrame(html=html % (nm, nm), width=150, height=100)
    fg.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon = folium.Icon(color = color_producer(gc))))

map.add_child(fg)
map.save("Nuclear Plants in the world.html")