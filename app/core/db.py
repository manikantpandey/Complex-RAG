from pathlib import Path
from app.core.models import DocumentMetadata

BASE_VECTOR_DIR = Path("vectorstore")
BASE_VECTOR_DIR.mkdir(parents=True, exist_ok=True)

def get_vector_path(doc_id: str) -> Path:
    return BASE_VECTOR_DIR / f"{doc_id}.faiss"

DOCUMENT_DB: dict[str, DocumentMetadata] = {}

def save_metadata(metadata: DocumentMetadata):
    DOCUMENT_DB[metadata.id]= metadata

def get_metadata(doc_id: str) -> DocumentMetadata:
    return DOCUMENT_DB.get(doc_id)
