import logging
from pathlib import Path
from .config import ESMA_URL
from .downloader import Downloader
from .parser import XMLParser
from .storage import Storage

logging.basicConfig(level=logging.INFO)

class Steeleye:
    """
    Main class for Steeleye application.
    """
    def __init__(self, temp_dir: Path = Path("data")):
        self.temp_dir = temp_dir
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Temporary directory created at: {self.temp_dir}")

    def run(self) -> None:
        """
        Main method to run the Steeleye application.
        """
        logging.info("Starting Steeleye application...")
        
        # Step 1: Download the XML file
        xml_file_path = self.temp_dir / "esma_data.xml"
        downloader = Downloader(ESMA_URL)
        downloader.download(xml_file_path)

        # Step 2: Parse the XML file to find DLTINS link
        parser = XMLParser()
        dltins_link = parser.find_dltins_link(xml_file_path)

        if dltins_link:
            logging.info(f"DLTINS link found: {dltins_link}")
        else:
            logging.warning("No DLTINS link found in the XML file.")
            return
        
        zip_file_path = self.temp_dir / "dltins.zip"
        downloader = Downloader(dltins_link)
        downloader.download(zip_file_path)

        final_xml_path = parser.extract_xml_from_zip(zip_file_path, self.temp_dir)
        if final_xml_path:
            logging.info(f"Final XML file extracted to: {final_xml_path}")
        else:
            logging.error("No XML file found in the downloaded ZIP archive.")
            return
        
        csv_file_path = self.temp_dir / "dltins.csv"
        parser.convert_xml_to_csv(final_xml_path, csv_file_path)

        logging.info(f"CSV file created at: {csv_file_path}")

        storage = Storage()
        remote_uri = f"file:///{self.temp_dir.resolve()}/s3_bucket/output.csv"
        storage.upload_file(csv_file_path, remote_uri)
        
if __name__ == "__main__":
    steeleye = Steeleye()
    steeleye.run()
    logging.info("Steeleye application finished running.")
        