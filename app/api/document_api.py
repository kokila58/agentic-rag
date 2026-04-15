from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.ingestion.document_loader import load_pdf

from app.services.document_service import add_document, list_documents
from app.services.document_service import delete_document


router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    upload_dir = "uploaded_docs"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = load_pdf(file_path)

    document = add_document(file.filename, chunks)

    return {
        "message": "Document uploaded",
        "document": document
    }

@router.get("/")
def get_documents():

    docs = list_documents()

    return {
        "documents": docs
    }

@router.delete("/{doc_id}")
def remove_document(doc_id: str):

    delete_document(doc_id)

    return {
        "message": "Document deleted"
    }

