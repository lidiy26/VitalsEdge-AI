from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title="VitalsEdge AI", version="0.1.0", docs_url="/api/docs")

# CORS middleware ekle
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "version": "0.1.0"}

@app.get("/api/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/api/data/ingest")
def ingest(data: dict):
    return {"status": "success", "data": data}

@app.post("/api/analysis/predict-attack")
def predict(user_id: str):
    return {
        "user_id": user_id,
        "attack_probability": 0.78,
        "risk_level": "HIGH",
        "lead_time_hours": 12
    }

@app.get("/api/xai/explain/{user_id}")
def explain(user_id: str):
    return {
        "user_id": user_id,
        "explanation": "Uyku ve nabız korelasyonu yüksek risk gösteriyor.",
        "top_features": [
            {"name": "Gece Uyku Süresi", "importance": 0.35},
            {"name": "Nabız Varyasyonu", "importance": 0.28},
            {"name": "Aktivite Düşüşü", "importance": 0.22},
            {"name": "Stres Seviyesi", "importance": 0.15}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)