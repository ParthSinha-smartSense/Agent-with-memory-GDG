# 🚀 Neo4j + Graphiti Agent Setup

This guide walks you through setting up a local development environment for working with Neo4j, Graphiti MCP Server, and a custom agent script.

---

## 📦 Prerequisites

- Install [Docker](https://www.docker.com/get-started/)
- Python 3.10 or above (for agent)
- [`uv`](https://lance.rs/uv/install/) for running async Python scripts

---

## 🧠 Step 1: Set Up Neo4j with Docker

### 🔹 Option 1: Use Docker Compose

```bash
docker compose up --build
```

Ensure you have a valid `docker-compose.yml` in your project root.

---

### 🔹 Option 2: Run with Persistent Volume and Custom Password

```bash
docker run \
  --publish=7474:7474 --publish=7687:7687 \
  --env NEO4J_AUTH=neo4j/your_password \
  --volume=/path/to/your/data:/data \
  neo4j:ubi9
```

> ✅ Replace `/path/to/your/data` with your local directory.  
> 🔐 Replace `your_password` with a secure password of your choice.

---

### 🌐 Access Neo4j

Visit [http://localhost:7474](http://localhost:7474) in your browser.

- **Username:** `neo4j`  
- **Password:** The one you set in `NEO4J_AUTH`

---

## 🕸️ Step 2: Clone & Run Graphiti MCP Server

```bash
git clone https://github.com/getzep/graphiti.git
cd graphiti/mcp_server
cp .env.example .env
uv run graphiti_mcp_server.py --model gpt-4o-mini --transport sse --group-id my-project
```

---

## 🤖 Step 3: Clone & Run This Agent Project

```bash
git clone https://github.com/ParthSinha-smartSense/Agent-with-memory-GDG.git
cp .env.example .env
python run agent.py
```

---

## ✅ Final Checklist

- [ ] Docker is installed and running  
- [ ] Neo4j container is up  
- [ ] Password is securely set and accessible  
- [ ] Graphiti MCP Server is running  
- [ ] Agent script is running and connected to MCP  

---

## 🧩 Notes

- Ensure all `.env` files are properly configured.
- If using volumes, make sure the data directory exists to avoid mount errors.
- Use `docker ps` to check running containers.

---

## 📬 Support

For issues related to Graphiti, visit [Graphiti GitHub Issues](https://github.com/getzep/graphiti/issues).

For this project, open an issue in this repo.
