from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    document_id: str
    question: str

class EvidenceItem(BaseModel):
    text: str
    page: int
    score: float

class QueryResponse(BaseModel):
    query_id: str
    answer: str
    status: str
    confidence: float
    evidence: List[EvidenceItem]
    explanation: str
    latency_ms: int