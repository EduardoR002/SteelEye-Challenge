import logging
from pathlib import Path
from lxml import etree
import zipfile

class XMLParser:
    """
    Class responsible for parsing XML files.
    """
    def find_dltins_link(self, xml_path: Path) -> str | None:
        """
        Analyze the XML file to find the DLTINS link.
        """
        logging.info(f"Parsing XML file: {xml_path}")
        try:
            tree = etree.parse(str(xml_path))
            root = tree.getroot()
            xpath_query = ".//doc[str[@name='file_type']='DLTINS']/str[@name='download_link']"
            found_elements = root.xpath(xpath_query)

            if found_elements:
                link = found_elements[0].text
                logging.info(f"Found DLTINS link: {link}")
                return link
            else:
                logging.warning("No DLTINS link found in the XML file.")
                return None
        except etree.XMLSyntaxError as e:
            logging.error(f"XML syntax error while parsing {xml_path}: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while parsing {xml_path}: {e}")
            raise 
        
    def extract_xml_from_zip(self, zip_path: Path, extract_to: Path) -> Path | None:
        """
        Extract XML file from a ZIP archive.
        """
        logging.info(f"Extracting XML from ZIP file: {zip_path}")
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                xml_files = [f for f in zip_ref.namelist() if f.endswith('.xml')]
                if not xml_files:
                    logging.warning("No XML files found in the ZIP archive.")
                    return None
                xml_file = xml_files[0]
                zip_ref.extract(xml_file, extract_to)
                extracted_path = extract_to / xml_file
                logging.info(f"Extracted XML file to: {extracted_path}")
                return extracted_path
        except zipfile.BadZipFile as e:
            logging.error(f"Bad ZIP file: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while extracting from ZIP: {e}")
            raise