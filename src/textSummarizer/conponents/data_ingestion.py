import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig
import requests
import zipfile



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
     file_path = Path(self.config.local_data_file)

     if not file_path.exists():

        response = requests.get(self.config.source_URL, stream=True)
        response.raise_for_status()

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        
    
    def extract_zip_file(self):
     unzip_path = self.config.unzip_dir

     if not zipfile.is_zipfile(self.config.local_data_file):
        raise Exception("Downloaded file is NOT a valid ZIP. Check source URL.")

     with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
        zip_ref.extractall(unzip_path)

