import logging
from pathlib import Path
import fsspec


class Storage:
    """
    This class provides a method to upload files from a local path to a specified remote URI.
    It uses the fsspec library to handle various storage backends.
    """

    def upload_file(self, local_path: Path, remote_uri: str) -> None:
        """
        Upload a file from local_path to remote_uri.

        Args:
            local_path (Path): The local file path to upload.
            remote_uri (str): The remote URI where the file should be uploaded.

        Raises:
            Exception: If the upload fails, an exception is raised with an error message.
        """
        logging.info(f"Uploading {local_path} to {remote_uri}")
        try:
            with fsspec.open(remote_uri, "wb") as remote_file:
                with open(local_path, "rb") as local_file:
                    remote_file.write(local_file.read())
            logging.info(f"Successfully uploaded {local_path} to {remote_uri}")
        except Exception as e:
            logging.error(f"Failed to upload {local_path} to {remote_uri}: {e}")
            raise
