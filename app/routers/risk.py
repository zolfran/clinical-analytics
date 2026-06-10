"""Risk scoring endpoints — readmission risk, chronic disease risk."""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.risk_service import compute_readmission_risk, compute_chronic_risk

router = APIRouter(prefix="/risk", tags=["Risk Scoring"])


class ReadmissionInput(BaseModel):
    age: int
    length_of_stay_days: int
    num_prior_admissions: int
    num_chronic_conditions: int
    has_diabetes: bool = False
    has_heart_failure: bool = False
    discharge_disposition: str = "home"


class ChronicRiskInput(BaseModel):
    age: int
    bmi: float
    systolic_bp: float
    diastolic_bp: float
    fasting_glucose: float
    total_cholesterol: float
    hdl_cholesterol: float
    smoker: bool = False
    family_history: bool = False


@router.post("/readmission")
def predict_readmission(body: ReadmissionInput) -> dict:
    """Predict 30-day hospital readmission risk."""
    return compute_readmission_risk(body.model_dump())


@router.post("/chronic-disease")
def predict_chronic_disease(body: ChronicRiskInput) -> dict:
    """Assess chronic disease risk based on clinical indicators."""
    return compute_chronic_risk(body.model_dump())
