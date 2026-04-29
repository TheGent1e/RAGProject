# RAG Project

This project implements a FastAPI MVP for a Retrieval-Augmented Generation (RAG) application.

## Requirements

- FastAPI
- uvicorn
- pydantic

## Installation

Run the following command to install dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

Use the following command to start the FastAPI server:

```bash
uvicorn app.main:app --reload
```
# RAGProject MVP

这是一个最小可运行的 FastAPI 项目骨架，用于后续扩展为 RAG / NL2SQL / Agent 系统。

## 功能

- `GET /health`：健康检查
- `POST /query`：接收自然语言问题，返回占位 SQL、模拟结果和后续建议

## 安装

```bash
pip install -r requirements.txt
