from app.services.risk_service import compute_readmission_risk, compute_chronic_risk


def test_low_readmission_risk() -> None:
    result = compute_readmission_risk({
        "age": 35, "length_of_stay_days": 2, "num_prior_admissions": 0,
        "num_chronic_conditions": 0, "has_diabetes": False,
        "has_heart_failure": False, "discharge_disposition": "home",
    })
    assert result["risk_level"] == "low"
    assert result["risk_score"] < 25


def test_high_readmission_risk() -> None:
    result = compute_readmission_risk({
        "age": 78, "length_of_stay_days": 10, "num_prior_admissions": 3,
        "num_chronic_conditions": 4, "has_diabetes": True,
        "has_heart_failure": True, "discharge_disposition": "snf",
    })
    assert result["risk_level"] in ("high", "very_high")
    assert result["risk_score"] >= 50


def test_chronic_risk_assessment() -> None:
    result = compute_chronic_risk({
        "age": 55, "bmi": 32, "systolic_bp": 145, "diastolic_bp": 92,
        "fasting_glucose": 115, "total_cholesterol": 245,
        "hdl_cholesterol": 38, "smoker": True, "family_history": True,
    })
    assert len(result["assessments"]) == 2
    cv = result["assessments"][0]
    assert cv["condition"] == "cardiovascular_disease"
    assert cv["risk_level"] in ("high", "very_high")
