from pydantic import BaseModel, Field
from typing import List, Dict, Any


class QueryRequest(BaseModel):
    natural_language: str = Field(..., description="User's natural language question")


class QueryResponse(BaseModel):
    sql: str
    results: List[Dict[str, Any]]
    suggestions: List[str]
