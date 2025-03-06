
import pandas as pd
import folium
from geopy.geocoders import Nominatim
# Define the file path again
file_path = "cghs.csv"

# Read the uploaded CSV file
df_uploaded = pd.read_csv(file_path)

# Display the first few rows of the dataset
l=df_uploaded.head()
#print(l)

# Display the end few rows of the dataset
l=df_uploaded.tail()
#print(l)


m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India

geolocator = Nominatim(user_agent="geoapi")

for city in df_uploaded["cityName"].unique():
    location = geolocator.geocode(city + ", India")
    if location:
        folium.CircleMarker(
            location=[location.latitude, location.longitude],
            radius=5,
            popup=city,
            color="blue",
            fill=True
        ).add_to(m)

m.save("cghs_hospitals_map.html")
print("Map saved! Open 'cghs_hospitals_map.html' to view.")

