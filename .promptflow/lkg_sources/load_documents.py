import json
import urllib.parse

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from promptflow import tool

@tool
def load_transcription(
    account_uri: str,
    container_name: str,
    config: str
    ) -> dict:

    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(account_url=account_uri, credential=credential)

    config = urllib.parse.unquote(config)
    config_client = blob_service_client.get_blob_client(container=container_name, blob=config)
    config_downloader = config_client.download_blob(max_concurrency=1, encoding='UTF-8')
    config_dict = config_downloader.readall()
    config_dict = json.loads(config_dict)


    documents = {}

    for key in config_dict.keys():
        doc = urllib.parse.unquote(config_dict[key])
        doc_client = blob_service_client.get_blob_client(container=container_name, blob=doc)
        doc_downloader = doc_client.download_blob(max_concurrency=1, encoding='UTF-8')
        doc_text = doc_downloader.readall()

        print("Load Documents completed.")
        documents[key] = doc_text

    return documents
