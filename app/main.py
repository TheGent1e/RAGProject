from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse
from app.agent import answer_question

app = FastAPI(title="RAGProject RAG/NL2SQL MVP", version="0.2.0")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    sql, results, explanation, contexts = answer_question(request.natural_language)
    return QueryResponse(
        sql=sql,
        results=results,
        explanation=explanation,
        retrieved_context=contexts,
    )
