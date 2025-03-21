import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Example dataset
data = pd.read_csv('dataset_for_assignment_2.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Select features for clustering
X_clustering = df[["Age", "App Sessions", "Distance Travelled (km)", "Calories Burned"]]

# Apply KMeans Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_clustering)

# Visualize the clusters
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Age", y="App Sessions", hue="Cluster", data=df, palette="viridis", s=100)
plt.title("Clustering of Users Based on Age and App Sessions")
plt.xlabel("Age")
plt.ylabel("App Sessions")
plt.legend(title='Cluster')
plt.show()
