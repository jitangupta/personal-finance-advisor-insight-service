import pandas as pd

def load_data(file_path: str):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Example preprocessing: Handle missing values, encode categorical data
    data.fillna(0, inplace=True)
    return data