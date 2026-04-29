# RAGProject

基于 FastAPI 的 RAG + NL2SQL 智能数据查询 MVP。用户通过自然语言提问，系统自动检索本地 Schema/词典，生成并执行 SQL，返回查询结果与解释说明。

## 目录结构

```
RAGProject/
├── app/
│   ├── __init__.py
│   ├── main.py       # FastAPI 入口
│   ├── agent.py      # NL2SQL 逻辑（可接 LLM）
│   ├── rag.py        # RAG 检索模块（可接向量数据库）
│   ├── db.py         # 数据库执行层（可接真实 DB）
│   └── schemas.py    # Pydantic 请求/响应模型
├── data/
│   ├── schema_docs/
│   │   └── demo_schema.md   # 表结构说明
│   └── glossary.md          # 业务词典
├── requirements.txt
└── README.md
```

## 安装

```bash
pip install -r requirements.txt
```

## 启动

```bash
uvicorn app.main:app --reload
```

## 接口说明

### GET /health
健康检查。

```bash
curl http://127.0.0.1:8000/health
```

### POST /query
接收自然语言问题，返回生成的 SQL、查询结果、解释说明、知识片段。

```bash
curl -X POST "http://127.0.0.1:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"natural_language":"昨天华南区销售额为什么下降了？"}'
```

**响应示例：**
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

## 后续扩展方向

1. 将 `app/db.py` 中的 `execute_sql` 替换为真实数据库连接（SQLite / PostgreSQL 等）
2. 将 `app/agent.py` 中的 `generate_sql` 替换为 LLM 调用（OpenAI / 本地模型等）
3. 将 `app/rag.py` 中的关键词检索替换为 Embedding + 向量数据库检索
4. 扩展成多 Agent 归因分析工作流

