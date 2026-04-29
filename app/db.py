from typing import List, Dict, Any


def execute_sql(sql: str) -> List[Dict[str, Any]]:
    """
    Placeholder DB execution layer.
    Replace with a real database connection later, e.g.:

        import sqlite3
        conn = sqlite3.connect("warehouse.db")
        cursor = conn.execute(sql)
        columns = [d[0] for d in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    """
    return [
        {"date": "2026-04-28", "region": "华南", "sales_amount": 1200},
        {"date": "2026-04-27", "region": "华南", "sales_amount": 1350},
        {"date": "2026-04-26", "region": "华南", "sales_amount": 1280},
    ]
