from os import closerange
import folium
import pandas

###Read the csv and json that contains all the information that I need. 
data = pandas.read_csv("files\-nuclear-power-stations.csv")



#Create a list of the columns latitude, longitude, name and gross capacity (this is the capacity of the reactor)
latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
name = list(data["Name"])
gross_capacity = list(data["Gross Capacity /MW"])



#Here I must to clean the list, because it contains a "," in some values.
gross_cap_removed_commas = [i.replace(",", "") for i in gross_capacity]
gross_cap = [int(i) for i in gross_cap_removed_commas]



#With a function, I am producing the color which the pop ups will have. It will variate by the gross capacity for each nuclear power plant. 
def color_producer(gc):
    if gc < 700:
        return "lightblue"
    elif 700 <= gc < 1200:
        return "blue"
    else:
        return "darkblue"
    

    
#Creating the folium map and giving it a name. Passing the latitude and longitude that we will start visualizating.   
map = folium.Map(location = [50.78837912727776, 14.320049151545614], zoom_start=5, tiles= "CartoDB positron")    
fg = folium.FeatureGroup(name = "My nuclear map")



#here the zip function iterate the first item from both list, and creates a tuple with those two items. 
html = """
<h3><i>Nuclear Plant:</i><b></h3>
<h3><a href="https://www.google.com/search?q=nuclearplant%%22%s%%22" target="_blank">%s</a><b>.</h3>
"""



#The for loop iterates all the files and create a "Marker" for each, which contains the "html" and the function color_producer.
# Here the zip function iterate the first item from both list, and creates a tuple with those two items. 
for lt, ln, nm, gc in zip(latitude, longitude, name, gross_cap):
    iframe = folium.IFrame(html=html % (nm, nm), width=150, height=100)
    fg.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon = folium.Icon(color = color_producer(gc))))
    

map.add_child(fg)
map.save("Nuclear Plants in the world.html")
