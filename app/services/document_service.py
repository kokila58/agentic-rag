import json
import uuid
from datetime import datetime

STORE_PATH = "storage/document_store.json"

def load_documents():

    with open(STORE_PATH, "r") as f:
        
        return json.load(f)

def save_documents(docs):

    with open(STORE_PATH, "w") as f:
        json.dump(docs, f, indent=2)


def add_document(file_name, chunks):

    docs = load_documents()
    document = {
        "id": str(uuid.uuid4()),
        "file_name": file_name,
        "upload_time": str(datetime.now()),
        "chunks": chunks
    }
    docs.append(document)
    save_documents(docs)
    
    return document

def list_documents():
    
    return load_documents()

def delete_document(doc_id):
    docs = load_documents()
    docs = [doc for doc in docs if doc["id"] != doc_id]
    save_documents(docs)