def generate_sql(natural_language: str) -> str:
    """
    Placeholder NL2SQL logic for MVP.
    Replace with real RAG / LLM logic later.
    """
    safe_question = natural_language.replace("'", "''")
    return f"SELECT * FROM demo_table WHERE question LIKE '%{safe_question}%'"


def run_query(natural_language: str):
    sql = generate_sql(natural_language)

    results = [
        {
            "question": natural_language,
            "answer": "This is a placeholder response from the MVP agent.",
        }
    ]

    suggestions = [
        "Connect a real database",
        "Replace placeholder SQL generation with LLM/RAG",
        "Add schema retrieval and SQL validation",
    ]

    return sql, results, suggestions
