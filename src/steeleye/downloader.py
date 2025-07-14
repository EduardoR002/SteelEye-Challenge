import logging # Regist what happens
import requests # Tool for making HTTP requests
from pathlib import Path # For handling file paths
from .config import ESMA_URL # Importing the ESMA_URL from the config module

class Downloader:
    """
    Class responsible for downloading files from the ESMA website.
    """ 
    def __init__(self, url: str):
        """
        Everytime we create an instance of Downloader, we set the download path.
        """
        self.url = url
        logging.info(f"Downloader initialized with URL: {self.url}")

    def download(self, output_path: Path) -> None:
        """
        Downloads the file from the specified URL and saves it to the file.
        """
        try:
            logging.info(f"Starting download from {self.url} to {output_path}")
            response = requests.get(self.url, timeout=30)
            response.raise_for_status()  # Raise an error for bad responses
            with open(output_path, 'wb') as file:
                file.write(response.content)
            logging.info(f"Download completed successfully and stored in {output_path}")
        except requests.RequestException as e:
            logging.error(f"Failed to download file: {e}")
            raise