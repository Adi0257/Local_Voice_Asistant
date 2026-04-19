from fastapi import APIRouter
from pydantic import BaseModel
from app.core.pipeline import run_pipeline
from app.ingestion.ingest import ingest_docs

router = APIRouter()


class QueryRequest(BaseModel):
    query: str
    chat_history: list
    session_id: str


@router.post("/query")
def query(req: QueryRequest):
    return run_pipeline(
        req.query,
        req.chat_history,
        req.session_id
    )


@router.post("/ingest")
def ingest(session_id: str):
    ingest_docs(session_id)
    return {"status": "done"}
