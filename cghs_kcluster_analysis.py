import pandas as pd
import folium
from geopy.geocoders import Nominatim
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# Define the file path again
file_path = "cghs.csv"

# Read the uploaded CSV file
df_uploaded = pd.read_csv(file_path)

# Group by city and sum the count of beneficiaries
df_cluster = df_uploaded.groupby("cityName")["count"].sum().reset_index()

# Normalize the hospital count data
scaler = StandardScaler()
df_cluster["count_scaled"] = scaler.fit_transform(df_cluster[["count"]])

# Apply K-Means Clustering (3 groups: Low, Medium, High coverage)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_cluster["Cluster"] = kmeans.fit_predict(df_cluster[["count_scaled"]])

# Mapping Clusters to Labels
cluster_labels = {0: "Low Coverage", 1: "Medium Coverage", 2: "High Coverage"}
df_cluster["Coverage_Level"] = df_cluster["Cluster"].map(cluster_labels)

# Initialize Map
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India
geolocator = Nominatim(user_agent="geoapi")

# Define cluster colors
cluster_colors = {
    "Low Coverage": "red",
    "Medium Coverage": "orange",
    "High Coverage": "green"
}

# Add markers to the map
for _, row in df_cluster.iterrows():
    city = row["cityName"]
    coverage = row["Coverage_Level"]

    # Get latitude and longitude
    location = geolocator.geocode(city + ", India")
    if location:
        folium.CircleMarker(
            location=[location.latitude, location.longitude],
            radius=5,
            popup=f"{city} - {coverage}",
            color=cluster_colors[coverage],
            fill=True,
            fill_color=cluster_colors[coverage],
            fill_opacity=0.7
        ).add_to(m)

# Save and show map
m.save("cghs_coverage_map.html")
print("Map saved! Open 'cghs_coverage_map.html' to view.")
