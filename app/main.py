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

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=443,  # HTTPS runs on port 443
        ssl_certfile="local-dev-certificate.pem",  # Path to the .pem file
        ssl_keyfile="local-dev-certificate.pem",  # Same .pem file if it contains both
    )