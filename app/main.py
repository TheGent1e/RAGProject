from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse
from app.agent import run_query

app = FastAPI(title="RAGProject MVP", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    sql, results, suggestions = run_query(request.natural_language)
    return QueryResponse(sql=sql, results=results, suggestions=suggestions)
