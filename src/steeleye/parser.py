import logging
from pathlib import Path
from lxml import etree
import zipfile
import pandas as pd


class XMLParser:
    """
    Class responsible for parsing XML files.

    Methods:
        find_dltins_link(xml_path: Path) -> str | None
        extract_xml_from_zip(zip_path: Path, extract_to: Path) -> Path | None
        convert_xml_to_csv(xml_path: Path, csv_path: Path) -> None
    """

    def find_dltins_link(self, xml_path: Path) -> str | None:
        """
        Analyze the XML file to find the DLTINS link.

        Args:
            xml_path (Path): Path to the XML file to parse.

        Returns:
            str | None: The DLTINS link if found, otherwise None.

        Raises:
            etree.XMLSyntaxError: If the XML file is not well-formed.
            Exception: For any other errors encountered during parsing.
        """
        logging.info(f"Parsing XML file: {xml_path}")
        try:
            tree = etree.parse(str(xml_path))
            root = tree.getroot()
            xpath_query = (
                ".//doc[str[@name='file_type']='DLTINS']/str[@name='download_link']"
            )
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

        Args:
            zip_path (Path): Path to the ZIP file.
            extract_to (Path): Directory to extract the XML file to.

        Returns:
            Path | None: The path to the extracted XML file if successful, otherwise None.

        Raises:
            zipfile.BadZipFile: If the ZIP file is not valid.
            Exception: For any other errors encountered during extraction.
        """
        logging.info(f"Extracting XML from ZIP file: {zip_path}")
        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                xml_files = [f for f in zip_ref.namelist() if f.endswith(".xml")]
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

    def convert_xml_to_csv(self, xml_path: Path, csv_path: Path) -> None:
        """
        Convert the wanted fields from XML to CSV format.

        Args:
            xml_path (Path): Path to the XML file to convert.
            csv_path (Path): Path where the CSV file will be saved.

        Returns:
            None

        Raises:
            etree.XMLSyntaxError: If the XML file is not well-formed.
            Exception: For any other errors encountered during conversion.
        """
        logging.info(f"Converting XML file to CSV: {xml_path}")

        # Define the headers for the CSV file
        headers = [
            "FinInstrmGnlAttrbts.Id",
            "FinInstrmGnlAttrbts.FullNm",
            "FinInstrmGnlAttrbts.ClssfctnTp",
            "FinInstrmGnlAttrbts.CmmdtyDerivInd",
            "FinInstrmGnlAttrbts.NtnlCcy",
            "Issr",
        ]

        # Initialize a list to hold the data rows
        data_rows = []

        # Use iterparse to handle large XML files efficiently, instead of loading the entire file into memory with etree.parse (Ram usage optimization)
        # The events parameter is set to 'end' to process elements after they are fully parsed
        # The tag parameter is set to the specific element we are interested in, # which is 'TermntdRcrd' in this case that contains the complete record
        # The namespace is specified to match the XML structure
        context = etree.iterparse(
            str(xml_path),
            events=("end",),
            tag="{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}TermntdRcrd",
        )

        for _, elem in context:
            ns = {"esma": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.02"}

            # Extract the relevant fields from the XML element
            # Using findtext with the namespace to get the text content of each field
            # The findtext method is used to retrieve the text content of the specified elements
            # If the element is not found, it returns None, which is handled by the default value of the dictionary
            row = {
                "FinInstrmGnlAttrbts.Id": elem.findtext(
                    ".//esma:FinInstrmGnlAttrbts/esma:Id", namespaces=ns
                ),
                "FinInstrmGnlAttrbts.FullNm": elem.findtext(
                    ".//esma:FinInstrmGnlAttrbts/esma:FullNm", namespaces=ns
                ),
                "FinInstrmGnlAttrbts.ClssfctnTp": elem.findtext(
                    ".//esma:FinInstrmGnlAttrbts/esma:ClssfctnTp", namespaces=ns
                ),
                "FinInstrmGnlAttrbts.CmmdtyDerivInd": elem.findtext(
                    ".//esma:FinInstrmGnlAttrbts/esma:CmmdtyDerivInd", namespaces=ns
                ),
                "FinInstrmGnlAttrbts.NtnlCcy": elem.findtext(
                    ".//esma:FinInstrmGnlAttrbts/esma:NtnlCcy", namespaces=ns
                ),
                "Issr": elem.findtext(".//esma:Issr", namespaces=ns),
            }
            data_rows.append(row)

            elem.clear()  # Clear the element to free memory
            while elem.getprevious() is not None:
                del elem.getparent()[0]

        if not data_rows:
            logging.warning("No data rows found in the XML file.")
            return

        # Create a DataFrame from the collected data rows
        df = pd.DataFrame(data_rows, columns=headers)

        # Add a new column 'a_count' that counts occurrences of 'a' in 'FullNm'
        df["a_count"] = (
            df["FinInstrmGnlAttrbts.FullNm"].str.count("a").fillna(0).astype(int)
        )

        # Add a new column 'contains_a' that indicates if 'a_count' is greater than 0
        df["contains_a"] = df["a_count"].apply(
            lambda count: "YES" if count > 0 else "NO"
        )

        df.to_csv(csv_path, index=False, encoding="utf-8")
        logging.info(f"CSV file created at: {csv_path}")
