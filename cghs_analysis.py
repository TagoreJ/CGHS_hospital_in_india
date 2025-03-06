import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df_cluster = df_uploaded.groupby("cityName")["count"].sum().reset_index()
scaler = StandardScaler()
df_cluster["count_scaled"] = scaler.fit_transform(df_cluster[["count"]])

kmeans = KMeans(n_clusters=3, random_state=42)
df_cluster["Cluster"] = kmeans.fit_predict(df_cluster[["count_scaled"]])

print(df_cluster.head())




# Define the file path again
file_path = "cghs.csv"

# Read the uploaded CSV file
df_uploaded = pd.read_csv(file_path)


plt.figure(figsize=(10,5))
sns.barplot(x="card_type", y="count", data=df_uploaded, estimator=sum, ci=None)
plt.xticks(rotation=45)
plt.title("Number of Beneficiaries by Card Type")
plt.show()
# Display Graph of the comparsion mentioned above
plt.savefig("cghs_beneficiaries_card_type.png")
print("Graph saved! Open 'cghs_beneficiaries_card_type.png' to view.")