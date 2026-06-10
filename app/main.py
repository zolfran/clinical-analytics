from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import metrics, risk, population

app = FastAPI(
    title="Clinical Analytics Service",
    version="1.0.0",
    description="Population health analytics, clinical quality metrics, and risk scoring for healthcare modernization",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(metrics.router, prefix="/api/v1")
app.include_router(risk.router, prefix="/api/v1")
app.include_router(population.router, prefix="/api/v1")


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy", "service": "clinical-analytics", "version": "1.0.0"}
