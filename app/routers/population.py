"""Population health analytics endpoints."""

from fastapi import APIRouter

from app.services.population_service import (
    get_population_summary,
    get_age_distribution,
    get_condition_prevalence,
    get_utilization_stats,
)

router = APIRouter(prefix="/population", tags=["Population Health"])


@router.get("/summary")
def population_summary() -> dict:
    """Overview statistics for the patient population."""
    return get_population_summary()


@router.get("/age-distribution")
def age_distribution() -> dict:
    """Age distribution of the patient population."""
    return get_age_distribution()


@router.get("/conditions")
def condition_prevalence() -> dict:
    """Prevalence of chronic conditions in the population."""
    return get_condition_prevalence()


@router.get("/utilization")
def utilization() -> dict:
    """Healthcare utilization statistics."""
    return get_utilization_stats()
