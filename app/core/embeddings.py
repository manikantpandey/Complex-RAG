from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from app.core.config import settings
from app.core.db import get_vector_path

embedding_model= OpenAIEmbeddings(
    model= settings.embedding_model,
    openai_api_key= settings.openai_api_key
)

def create_vector_store_from_chunks(chunks: list[str], doc_id: str) -> None:
    vectorstore = FAISS.from_texts(chunks, embedding_model)
    vectorstore.save_local(folder_path=get_vector_path(doc_id).with_suffix("").as_posix())

def load_vectorstore(doc_id: str) -> FAISS:
    path= get_vector_path(doc_id).with_suffix("").as_posix()
    return FAISS.load_local(folder_path=path, embeddings=embedding_model)