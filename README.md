# RAGProject

A FastAPI-based MVP for a RAG + NL2SQL assistant. The system retrieves schema
docs and a business glossary from a local knowledge base, uses that context to
generate SQL from natural-language questions, and returns the SQL, query
results, an explanation, and the retrieved context snippets.

## Project Structure

```
RAGProject/
├─ app/
│  ├─ __init__.py     # package marker
│  ├─ main.py         # FastAPI app & endpoints
│  ├─ schemas.py      # Pydantic request/response models
│  ├─ rag.py          # knowledge-base loading & retrieval
│  ├─ agent.py        # NL2SQL logic (wires RAG + DB)
│  └─ db.py           # SQL execution layer (placeholder)
├─ data/
│  ├─ schema_docs/
│  │  └─ demo_schema.md   # table/column definitions
│  └─ glossary.md         # business term mappings
├─ requirements.txt
└─ README.md
```

## Features

- `GET /health` — health check
- `POST /query` — accept a natural-language question and return:
  - generated SQL
  - query results (placeholder rows today, real DB later)
  - short explanation of the reasoning
  - retrieved context snippets from the knowledge base

## Installation

```bash
pip install -r requirements.txt
```

## Running the App

```bash
uvicorn app.main:app --reload
```

The interactive API docs are available at <http://127.0.0.1:8000/docs>.

## Example Requests

```bash
# Health check
curl http://127.0.0.1:8000/health

# Natural-language query
curl -X POST "http://127.0.0.1:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"natural_language": "昨天华南区销售额为什么下降了？"}'
```

Example response:

```json
{
  "sql": "SELECT date, region, sales_amount FROM sales_summary WHERE date >= DATE('now', '-7 day') ORDER BY date DESC;",
  "results": [
    {"date": "2026-04-28", "region": "华南", "sales_amount": 1200},
    {"date": "2026-04-27", "region": "华南", "sales_amount": 1350},
    {"date": "2026-04-26", "region": "华南", "sales_amount": 1280}
  ],
  "explanation": "系统先通过 RAG 检索到表结构和业务词典，再根据上下文生成 SQL，并执行查询返回结果。",
  "retrieved_context": ["# Demo Schema\n\n## sales_summary\n..."]
}
```

## Extending the Project

| Area | How to extend |
|---|---|
| Real database | Replace `app/db.py → execute_sql()` with an actual DB connection |
| LLM-based SQL | Replace `app/agent.py → generate_sql()` with an LLM call that receives the retrieved context |
| Vector retrieval | Replace `app/rag.py → retrieve_context()` with embeddings + a vector DB |
| More knowledge | Add `.md` files under `data/schema_docs/` or expand `data/glossary.md` |

