from sklearn.cluster import KMeans

def train_kmeans(data, n_clusters=3):
    model = KMeans(n_clusters=n_clusters)
    model.fit(data)
    return model