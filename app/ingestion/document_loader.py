from pypdf import PdfReader

from app.ingestion.chunker import chunk_text
from app.services.embedding_service import embedding_service
from app.services.qdrant_service import store_embeddings


def load_pdf(file_path: str):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    chunks = chunk_text(text)

    if not chunks:
        return 0

    vectors = []
    payloads = []

    for chunk in chunks:

        embedding = embedding_service.create_embedding(chunk)

        vectors.append(embedding)

        payloads.append({
            "text": chunk,
            "source": file_path
        })

    store_embeddings(vectors, payloads)

    return len(chunks)