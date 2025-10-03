import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dest_path="data/skindiseasedataset"):
    api = KaggleApi()
    api.authenticate()  # Requires kaggle.json setup
    api.dataset_download_files(
        "pacificrm/skindiseasedataset", 
        path=dest_path, 
        unzip=True
    )
    print(f"Dataset downloaded to {dest_path}")

if __name__ == "__main__":
    os.makedirs("data/skindiseasedataset", exist_ok=True)
    download_dataset()
