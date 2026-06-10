"""Clinical Quality Metrics (CQMs) endpoints."""

from fastapi import APIRouter

from app.services.metrics_service import compute_quality_metrics

router = APIRouter(prefix="/metrics", tags=["Clinical Quality Metrics"])


@router.get("/quality")
def get_quality_metrics() -> dict:
    """Compute clinical quality metrics across the patient population."""
    return compute_quality_metrics()


@router.get("/quality/{metric_id}")
def get_metric_detail(metric_id: str) -> dict:
    """Get detail for a specific quality metric."""
    all_metrics = compute_quality_metrics()
    for m in all_metrics.get("metrics", []):
        if m["id"] == metric_id:
            return m
    return {"error": f"Metric {metric_id} not found"}
