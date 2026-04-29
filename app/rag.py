from pathlib import Path


DATA_DIR = Path(__file__).parent.parent / "data"


def load_knowledge_base() -> list[str]:
    docs = []

    schema_dir = DATA_DIR / "schema_docs"
    if schema_dir.exists():
        for path in sorted(schema_dir.glob("*.md")):
            docs.append(path.read_text(encoding="utf-8"))

    glossary = DATA_DIR / "glossary.md"
    if glossary.exists():
        docs.append(glossary.read_text(encoding="utf-8"))

    return docs


def retrieve_context(question: str) -> list[str]:
    """
    Simple keyword-based retrieval for MVP.
    Replace with embeddings + vector DB later.
    """
    docs = load_knowledge_base()
    q = question.replace("？", "").replace("?", "").lower()
    keywords = [w for w in q.split() if w]

    matched = []
    for doc in docs:
        low = doc.lower()
        if any(k in low for k in keywords):
            matched.append(doc)

    if matched:
        return matched[:3]

    return docs[:1] if docs else ["No knowledge base documents found."]
