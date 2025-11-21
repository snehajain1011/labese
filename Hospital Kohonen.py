import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

patients = pd.DataFrame({
    "Diabetes":      [1, 1, 0, 0, 0, 1, 0, 1],
    "Hypertension":  [1, 0, 1, 1, 0, 1, 0, 1],
    "Asthma":        [0, 0, 1, 1, 0, 0, 1, 0],
    "HeartDisease":  [1, 0, 0, 1, 0, 1, 0, 1]
})

data = patients.values
n_samples, n_features = data.shape

grid_size = 3
lr = 0.4
epochs = 50

np.random.seed(42)
weights = np.random.rand(grid_size, grid_size, n_features)

for epoch in range(epochs):
    for x in data:
        diff = weights - x
        dist = np.sqrt(np.sum(diff**2, axis=2))
        bmu_idx = np.unravel_index(np.argmin(dist), dist.shape)

        for i in range(grid_size):
            for j in range(grid_size):
                dist_to_bmu = np.sqrt((i - bmu_idx[0])**2 + (j - bmu_idx[1])**2)
                influence = np.exp(-dist_to_bmu / (epoch + 1))
                weights[i, j] += lr * influence * (x - weights[i, j])

cluster_map = []
for idx, x in enumerate(data):
    diff = weights - x
    dist = np.sqrt(np.sum(diff**2, axis=2))
    bmu_idx = np.unravel_index(np.argmin(dist), dist.shape)
    cluster_map.append((idx, bmu_idx))

cluster_map = pd.DataFrame(cluster_map, columns=["Patient", "Cluster"])

print("\nCluster Assignments:\n", cluster_map)

plt.figure(figsize=(6,6))
for patient, (cx, cy) in cluster_map.values:
    plt.scatter(cx, cy, s=300)
    plt.text(cx, cy, f"P{patient}", ha="center", va="center")

plt.title("Kohonen SOM - Patient Clusters")
plt.grid(True)
plt.show()
