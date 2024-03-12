from fastapi import File, Form, UploadFile

from models.models import (
    Document,
    DocumentMetadataFilter,
    Query,
    QueryResult,
)
from pydantic import BaseModel
from typing import List, Optional, Dict

class NamespaceModel(BaseModel):
    vector_count: int
    
class StatsResponse(BaseModel):
    index_fullness: float
    # namespaces: Dict[str, NamespaceModel]
    total_vector_count: int


class UpsertRequest(BaseModel):
    documents: List[Document]
    namespace: str

class UpsertFileRequest(BaseModel):
    file: UploadFile = File(...),
    metadata: Optional[str] = Form(None),
    namespace: str = Form(None)


class UpsertResponse(BaseModel):
    ids: List[str]


class QueryRequest(BaseModel):
    queries: List[Query]
    namespace: str


class QueryResponse(BaseModel):
    results: List[QueryResult]
    

class DeleteRequest(BaseModel):
    ids: Optional[List[str]] = None
    filter: Optional[DocumentMetadataFilter] = None
    delete_all: Optional[bool] = False
    namespace: str


class DeleteResponse(BaseModel):
    success: bool
    
