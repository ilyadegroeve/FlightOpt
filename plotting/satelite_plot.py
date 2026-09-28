# THIS CODE PLOTS FIELD COORDINATES ON A SATTELITE MAP

import folium

# Coordinates data
coordinates_data = {
    "VUB": (50.9407045, 4.2108946),
    "Edith Cavell": (50.9406812, 4.2104519),
    "Cliniques de l'Europe": (50.9405649, 4.2105543),
    "Epsylon ASBL": (50.9403610, 4.2105000),
    "Hôpital Etterbeek-Ixelles": (50.9407687, 4.2107004),
    "Clinique Saint-Jean": (50.9411201, 4.2105495),
    "Hôpitaux iris Ziekenhuizen": (50.9408986, 4.2104647),
}


# Calculate the center of the coordinates for map centering
latitudes = [coord[0] for coord in coordinates_data.values()]
longitudes = [coord[1] for coord in coordinates_data.values()]
center_latitude = sum(latitudes) / len(latitudes)
center_longitude = sum(longitudes) / len(longitudes)

# Create a Folium map centered around the coordinates
m = folium.Map(location=[center_latitude, center_longitude], zoom_start=17, tiles="Esri World Imagery")
# You can change tiles to different providers, e.g., "OpenStreetMap", "Stamen Terrain", etc.
# "Esri World Imagery" is a good choice for satellite images.

# Add markers for each location
for name, coord in coordinates_data.items():
    folium.Marker(
        location=coord,
        popup=name,
        icon=folium.Icon(color="red") # You can customize the marker icon
    ).add_to(m)

# Save the map to an HTML file
m.save("coordinates_map.html")

print("Map saved to coordinates_map.html")
print("Open coordinates_map.html in your web browser to view the map.")