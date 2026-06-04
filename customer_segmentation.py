# ==========================================
# CUSTOMER SEGMENTATION ANALYSIS PROJECT
# ==========================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("data/Mall_Customers.csv")

print("\n===== First 5 Rows =====")
print(df.head())

print("\n===== Dataset Info =====")
print(df.info())

print("\n===== Missing Values =====")
print(df.isnull().sum())

# ==========================================
# DATA CLEANING
# ==========================================

df.dropna(inplace=True)

# ==========================================
# FEATURE SELECTION
# ==========================================

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# ==========================================
# FEATURE SCALING
# ==========================================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# ELBOW METHOD
# ==========================================

wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.grid(True)

plt.savefig("elbow_method.png")
plt.close()

print("\nElbow Method graph saved as 'elbow_method.png'")

# ==========================================
# K-MEANS CLUSTERING
# ==========================================

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

# ==========================================
# CLUSTER NAMES
# ==========================================

cluster_names = {
    0: "Premium Customers",
    1: "Budget Customers",
    2: "Potential Customers",
    3: "Young Shoppers",
    4: "Regular Customers"
}

df["Cluster_Name"] = df["Cluster"].map(cluster_names)

# ==========================================
# VISUALIZE CLUSTERS
# ==========================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    palette='Set1',
    s=100
)

plt.title("Customer Segmentation")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")

plt.savefig("customer_segmentation.png")
plt.close()

print("Customer Segmentation graph saved as 'customer_segmentation.png'")

# ==========================================
# CLUSTER SUMMARY
# ==========================================

cluster_summary = df.groupby("Cluster").agg({
    "CustomerID": "count",
    "Age": "mean",
    "Annual Income (k$)": "mean",
    "Spending Score (1-100)": "mean"
}).round(2)

print("\n===== Cluster Summary =====")
print(cluster_summary)

# ==========================================
# CHECK CLUSTERS
# ==========================================

print("\n===== Cluster Preview =====")
print(df[['CustomerID', 'Cluster', 'Cluster_Name']].head(10))

# ==========================================
# EXPORT CSV
# ==========================================

df.to_csv(
    "data/Customer_Segment.csv",
    index=False
)

print("\nCustomer_Segment.csv saved successfully!")

# ==========================================
# FINAL DATA PREVIEW
# ==========================================

print("\n===== Final Dataset =====")
print(df.head())