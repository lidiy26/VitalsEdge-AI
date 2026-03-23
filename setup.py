#!/usr/bin/env python3
from pathlib import Path

print("VitalsEdge AI Setup baslaniyor...")

# Dizinler
dirs = [
    "phase-1/1-1-scope",
    "phase-1/1-2-security",
    "phase-1/1-3-fusion",
    "phase-2/2-1-anomaly",
    "phase-2/2-2-xai",
    "phase-2/2-3-api",
    "phase-2/2-4-5-eval",
    "phase-3",
    "tests",
    "docs",
    "models",
    "logs"
]

for d in dirs:
    Path(d).mkdir(parents=True, exist_ok=True)
    print(f"OK: {d}")

# Dosyalar
Path("requirements.txt").write_text("numpy==1.24.3\npandas==2.0.3\nscikit-learn==1.3.0\ntensorflow==2.13.0\nfastapi==0.104.1\nuvicorn==0.24.0\npydantic==2.4.2\npydantic-settings==2.0.3\nsqlalchemy==2.0.23\npsycopg2-binary==2.9.9\ncryptography==41.0.7\npython-dotenv==1.0.0\nshap==0.42.1\npytest==7.4.3\npytest-cov==4.1.0\n")
print("OK: requirements.txt")

Path(".env.example").write_text("HOST=0.0.0.0\nPORT=8000\nDEBUG=True\nDATABASE_URL=postgresql://vitals_user:password@localhost:5432/vitalsedge_dev\nSECRET_KEY=dev-secret\n")
print("OK: .env.example")

Path(".gitignore").write_text("__pycache__/\n*.py[cod]\nvenv/\nenv/\n.env\nlogs/\n*.log\nmodels/\n.pytest_cache/\n")
print("OK: .gitignore")

main_py = """from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="VitalsEdge AI", version="0.1.0", docs_url="/api/docs")

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
    return {"user_id": user_id, "probability": 0.78, "risk": "HIGH"}

@app.get("/api/xai/explain/{user_id}")
def explain(user_id: str):
    return {"user_id": user_id, "explanation": "Uyku ve nabiz korelasyonu"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
"""

Path("main.py").write_text(main_py)
print("OK: main.py")

Path("tests/__init__.py").write_text("")
print("OK: tests/__init__.py")

Path("pytest.ini").write_text("[pytest]\ntestpaths = tests\n")
print("OK: pytest.ini")

Path("README.md").write_text("# VitalsEdge AI\n\n## Basla\n\n1. python -m venv venv\n2. venv\\Scripts\\activate\n3. pip install -r requirements.txt\n4. python main.py\n5. http://localhost:8000/api/docs\n")
print("OK: README.md")

Path("phase-1/1-1-scope/kpi-tracking.json").parent.mkdir(parents=True, exist_ok=True)
Path("phase-1/1-1-scope/kpi-tracking.json").write_text('{"project": "VitalsEdge AI"}')
print("OK: phase-1/1-1-scope/kpi-tracking.json")

Path("phase-2/2-3-api/__init__.py").parent.mkdir(parents=True, exist_ok=True)
Path("phase-2/2-3-api/__init__.py").write_text('__version__ = "0.1.0"')
print("OK: phase-2/2-3-api/__init__.py")

print("\nSETUP TAMAMLANDI!\n")
print("1. python -m venv venv")
print("2. venv\\Scripts\\activate")
print("3. pip install -r requirements.txt")
print("4. python main.py")
