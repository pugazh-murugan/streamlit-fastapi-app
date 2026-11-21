# Streamlit + FastAPI Sample

```
streamlit-fastapi-app/
├── backend/                 # FastAPI service
│   ├── app/
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── routers/items.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── frontend/                # Streamlit UI
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── docker-compose.yml
├── .env.example
└── .gitignore
```

## Run with Docker

```bash
cp .env.example .env
docker compose up --build
```

- Frontend: http://localhost:8501
- Backend docs: http://localhost:8000/docs

## Run locally (without Docker)

```bash
# backend
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# frontend (new terminal)
cd frontend && pip install -r requirements.txt
BACKEND_URL=http://localhost:8000 streamlit run app.py
```
