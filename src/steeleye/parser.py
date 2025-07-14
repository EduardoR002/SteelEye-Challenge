import logging
from pathlib import Path
from lxml import etree

class XMLParser:
    """
    Class responsible for parsing XML files.
    """
    def find_dtlins_link(self, xml_path: Path) -> str | None:
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
        