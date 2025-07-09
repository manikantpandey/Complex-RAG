from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
from datetime import datetime

class DocumentMetadata(BaseModel):
    id: str
    filename: str
    upload_time: datetime
    summary: Optional[str] = None

    @staticmethod
    def create(filename: str) -> "DocumentMetadata":
        return DocumentMetadata(
            id=str(uuid4()), 
            filename=filename,
            upload_time=datetime.now()
        )