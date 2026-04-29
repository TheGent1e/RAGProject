from app.rag import retrieve_context
from app.db import execute_sql

# Max characters of retrieved context to embed in a fallback SQL comment
MAX_CONTEXT_PREVIEW_LENGTH = 500


def generate_sql(question: str, contexts: list[str]) -> str:
    """
    Placeholder NL2SQL logic.
    In production, send question + retrieved schema context to an LLM.
    Uses SQLite date syntax; adjust for other SQL dialects when swapping in a real DB.
    """
    q = question.lower()

    if "销售额" in question or "sales" in q:
        return (
            "SELECT date, region, sales_amount "
            "FROM sales_summary "
            "WHERE date >= DATE('now', '-7 day') "
            "ORDER BY date DESC;"
        )

    if "日活" in question or "dau" in q:
        return (
            "SELECT date, dau "
            "FROM user_metrics "
            "WHERE date >= DATE('now', '-7 day') "
            "ORDER BY date DESC;"
        )

    context_text = "\n\n".join(contexts)
    return (
        "-- Could not infer exact SQL from question.\n"
        "-- Retrieved context:\n"
        f"-- {context_text[:MAX_CONTEXT_PREVIEW_LENGTH]}"
    )


def answer_question(question: str):
    contexts = retrieve_context(question)
    sql = generate_sql(question, contexts)
    results = execute_sql(sql)

    explanation = (
        "系统先通过 RAG 检索到表结构和业务词典，再根据上下文生成 SQL，"
        "并执行查询返回结果。"
    )

    return sql, results, explanation, contexts

