import logging # Regist what happens
import requests # Tool for making HTTP requests
from pathlib import Path # For handling file paths
from .config import ESMA_URL # Importing the ESMA_URL from the config module

class Downloader:
    """
    Class responsible for downloading files from the ESMA website.

    Atributes:
        url (str): The URL of the file to be downloaded.
    """ 
    def __init__(self, url: str):
        """
        Initializes the Downloader with a URL.

        Args:
            url (str): The URL of the file to be downloaded.
        """
        self.url = url
        
        logging.info(f"Downloader initialized with URL: {self.url}")

    def download(self, output_path: Path) -> None:
        """
        Downloads the file from the specified URL and saves it to the file.

        Args:
            output_path (Path): The path where the downloaded file will be saved.

        Returns:
            None
        
        Raises:
            requests.RequestException: If the download fails due to network issues or invalid URL.
            OSError: If there is an issue writing to the file system.
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