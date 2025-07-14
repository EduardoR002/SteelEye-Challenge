import logging
from pathlib import Path
import fsspec

class Storage:
    """
    Upload files to a remote storage system using fsspec.
    """
    def upload_file(self, local_path: Path, remote_uri: str) -> None:
        """
        Upload a file from local_path to remote_uri.
        
        :param local_path: Path to the local file to upload.
        :param remote_uri: URI of the remote storage location.
        """
        logging.info(f"Uploading {local_path} to {remote_uri}")
        try:
            with fsspec.open(remote_uri, 'wb') as remote_file:
                with open(local_path, 'rb') as local_file:
                    remote_file.write(local_file.read())
            logging.info(f"Successfully uploaded {local_path} to {remote_uri}")
        except Exception as e:
            logging.error(f"Failed to upload {local_path} to {remote_uri}: {e}")
            raise