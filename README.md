# az-fn-for-fun

## Azurite

Install Azure Storage Emulator using Docker:

```
docker run \
    -p 10000:10000 -p 10001:10001 -p 10002:10002 \
    mcr.microsoft.com/azure-storage/azurite
```

## Azure Data Explorer

Use [Azure Data Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer) to initialize the Queue, nd fetche the connection string.
