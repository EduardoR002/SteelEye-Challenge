from pathlib import Path
import pytest
from src.steeleye.parser import XMLParser

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
    link = parser.find_dtlins_link(xml_path)

    assert link == "http://example.com/correct_dltins.zip"


def test_find_dltins_link_not_found(tmp_path: Path):
    """
    Test Not Found Case: DLTINS link does not exist.
    """
    xml_path = tmp_path / "test.xml"
    xml_path.write_text(FAKE_XML_CONTENT_WITHOUT_LINK)

    parser = XMLParser()
    link = parser.find_dtlins_link(xml_path)

    assert link is None