from pathlib import Path
from src.steeleye.parser import XMLParser
import zipfile

FAKE_XML_CONTENT_WITH_LINK = """
<response>
    <result name="response" numFound="2" start="0">
        <doc>
            <str name="file_type">FULINS</str>
            <str name="download_link">http://example.com/fulins.zip</str>
        </doc>
        <doc>
            <str name="file_type">DLTINS</str>
            <str name="download_link">http://example.com/correct_dltins.zip</str>
        </doc>
    </result>
</response>
"""

FAKE_XML_CONTENT_WITHOUT_LINK = """
<response>
    <result name="response" numFound="1" start="0">
        <doc>
            <str name="file_type">FULINS</str>
            <str name="download_link">http://example.com/fulins.zip</str>
        </doc>
    </result>
</response>
"""

def test_find_dltins_link_success(tmp_path: Path):
    """
    Test Success Case: DLTINS link exists.
    """
    xml_path = tmp_path / "test.xml"
    xml_path.write_text(FAKE_XML_CONTENT_WITH_LINK)

    parser = XMLParser()
    link = parser.find_dltins_link(xml_path)

    assert link == "http://example.com/correct_dltins.zip"


def test_find_dltins_link_not_found(tmp_path: Path):
    """
    Test Not Found Case: DLTINS link does not exist.
    """
    xml_path = tmp_path / "test.xml"
    xml_path.write_text(FAKE_XML_CONTENT_WITHOUT_LINK)

    parser = XMLParser()
    link = parser.find_dltins_link(xml_path)

    assert link is None

def test_extract_zip_file(tmp_path: Path):
    """
    Test Zip Extraction: Ensure the xml file is extracted correctly from the Zip File.
    """
    zip_path = tmp_path / "test.zip"
    xml_content = b"<data>This is a test file.</data>"
    xml_filename = "test.xml"

    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        zip_file.writestr(xml_filename, xml_content)

    parser = XMLParser()
    extracted_file_path = parser.extract_xml_from_zip(zip_path, tmp_path)

    assert extracted_file_path is not None
    assert extracted_file_path.exists()
    assert extracted_file_path.name == xml_filename
    assert extracted_file_path.read_bytes() == xml_content

def test_convert_xml_to_csv(tmp_path: Path):
    """
    Test XML to CSV Conversion: Ensure the XML content is converted to CSV format.
    """
