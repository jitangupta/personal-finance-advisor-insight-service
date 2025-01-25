from fastapi import FastAPI
from app.services.data_loader import load_data, preprocess_data
from app.models.clustering import train_kmeans

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/train-clustering/")
async def train_clustering(file_path: str, n_clusters: int = 3):
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    model = train_kmeans(processed_data, n_clusters)
    return {"message": "Clustering model trained successfully"}