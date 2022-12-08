# azblob -- operating Azure Blob storage

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

Default values are assumed to be stored in the environmental variables:
- AZ_STORAGE_ACCOUNT_NAME
- AZ_STORAGE_ACCOUNT_KEY
- AZ_BLOB_CONTAINER_NAME
- AZ_SAS_TOKEN


## Example

```bash
$ export AZ_SAS_TOKEN=`azb get_sas`
```    


## References

- Azure Storage Blobs client library for Python
    - [Documents](https://learn.microsoft.com/en-us/python/api/overview/azure/storage-blob-readme?view=azure-python)
    - [github repository](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.14.1/sdk/storage/azure-storage-blob)
- [blob Package - generate_account_sas](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob?view=azure-python#azure-storage-blob-generate-container-sas)
- [ResourceTypes Class](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.resourcetypes?view=azure-python)
- [AccountSasPermissions Class](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.accountsaspermissions?view=azure-python)
- [ContainerClient Class](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient?view=azure-python)