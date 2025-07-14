from pathlib import Path
from src.steeleye.downloader import Downloader

def test_download_success(mocker, tmp_path: Path):
    """
    Test successful download of a file.
    """
    fake_xml_content = b"<xml>Fake content</xml>"
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.content = fake_xml_content

    mocker.patch('requests.get', return_value=mock_response)

    output_file = tmp_path / "test_file.xml"
    test_url = "http://example.com/test_file.xml"
    downloader = Downloader(test_url)
    downloader.download(output_file)

    assert output_file.exists()
    assert output_file.read_bytes() == fake_xml_content