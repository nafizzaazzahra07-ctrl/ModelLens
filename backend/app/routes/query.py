from fastapi import APIRouter
from app.schemas import QueryRequest, QueryResponse, EvidenceItem

router = APIRouter(prefix="/api/v1", tags=["Query"])

@router.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    return QueryResponse(
        query_id="q_123",
        answer="The refund period is 30 days.",
        status="SUPPORTED",
        confidence=0.94,
        evidence=[
            EvidenceItem(
                text="Customers may request a refund within 30 days.",
                page=2,
                score=0.91
            )
        ],
        explanation="The answer is directly supported by the retrieved document evidence.",
        latency_ms=1200
    )