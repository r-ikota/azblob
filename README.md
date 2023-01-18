# azblob -- a simple tool for Azure Blob storage

## Requirements

[Azure Storage Blobs client library for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/storage-blob-readme?view=azure-python) is required.
To install it, type:

```bash
$ pip install azure-storage-blob
```

**An Azure Storage account and a container must be created in advance.**

## Install & Uninstall
### For unix

    python setup.py install --record files.txt
    cat files.txt | xargs rm -rf

### For Windows (not supported)

    python setup.py install --record files.txt
    Get-Content files.txt | ForEach-Object {Remove-Item $_ -Recurse -Force}


## Default values

Default values are assumed to be stored in the following environment variables:
- AZURE_STORAGE_ACCOUNT
- AZURE_STORAGE_KEY
- AZURE_BLOB_CONTAINER
- AZURE_STORAGE_SAS_TOKEN

## Example

```bash
$ export AZURE_STORAGE_SAS_TOKEN=`azb get_sas`
$ azb list_blobs
$ azb upload_blob <blob_name> <file_name>
```    


## References

- Azure Storage Blobs client library for Python
    - [Documents](https://learn.microsoft.com/en-us/python/api/overview/azure/storage-blob-readme?view=azure-python)
    - [github repository](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.14.1/sdk/storage/azure-storage-blob)
- [blob Package - generate_account_sas](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob?view=azure-python#azure-storage-blob-generate-container-sas)
- [ResourceTypes Class](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.resourcetypes?view=azure-python)
- [AccountSasPermissions Class](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.accountsaspermissions?view=azure-python)
- [ContainerClient Class](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient?view=azure-python)
- [Choose how to authorize access to blob data with Azure CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-data-operations-cli)
