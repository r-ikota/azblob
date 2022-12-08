"""
processing azure blob
"""

from datetime import datetime, timedelta
from azure.storage.blob import (
    BlobServiceClient,
    generate_account_sas,
    ResourceTypes,
    AccountSasPermissions,
)


def get_sas(storage_account_name, storage_account_key, ttl=1):
    """
    get sas to create, delete, and list blobs

    Parameters
    ----------

    storage_account_name: str
        Storage account name.

    storage_account_key: str
        Storage account key.

    ttl: int
        Time to live for SAS.
    """

    sas_token = generate_account_sas(
        account_name=storage_account_name,
        account_key=storage_account_key,
        resource_types=ResourceTypes(service=True, container=True, object=True),
        permission=AccountSasPermissions(
            read=True, list=True, create=True, delete=True
        ),
        expiry=datetime.utcnow() + timedelta(hours=ttl),
    )

    return sas_token


class AZCONTAINER:
    """
    A class for managing blobs

    Parameters
    ----------
    storage_account_name: str
        The account name for an Azure Storage Account.

    container_name: str
        A container name.

    sas_token: str
        SAS token
    """

    def __init__(self, storage_account_name, container_name, sas_token):
        account_url = f"https://{storage_account_name:s}.blob.core.windows.net"
        self._blob_service_client = BlobServiceClient(
            account_url=account_url, credential=sas_token
        )
        self._container_client = self._blob_service_client.get_container_client(
            container_name
        )

    def list_blobs(self):
        return list(self._container_client.list_blob_names())

    def upload_blob(self, blob_name, file_name):
        blob_client = self._container_client.get_blob_client(blob_name)
        with open(file_name, "rb") as data:
            blob_client.upload_blob(data, blob_type="BlockBlob")

    def download_blob(self, blob_name, file_name):
        blob_client = self._container_client.get_blob_client(blob_name)
        with open(file_name, "wb") as fh:
            download_stream = blob_client.download_blob()
            fh.write(download_stream.readall())

    def delete_blob(self, blob_name):
        blob_client = self._container_client.get_blob_client(blob_name)
        blob_client.delete_blob()
