"""Risk scoring models for readmission and chronic disease prediction.

Uses simple rule-based scoring for demonstration. In production, these
would be ML models trained on historical patient data.
"""


def compute_readmission_risk(data: dict) -> dict:
    """Compute 30-day readmission risk score.

    Simplified LACE-inspired model:
    - L: Length of stay
    - A: Acuity of admission
    - C: Comorbidities
    - E: Emergency department visits
    """
    score = 0.0
    factors = []

    # Age factor
    if data["age"] >= 75:
        score += 15
        factors.append({"factor": "age_75_plus", "points": 15, "detail": f"Age {data['age']} >= 75"})
    elif data["age"] >= 65:
        score += 10
        factors.append({"factor": "age_65_74", "points": 10, "detail": f"Age {data['age']} 65-74"})

    # Length of stay
    los = data["length_of_stay_days"]
    if los >= 14:
        score += 20
        factors.append({"factor": "long_stay", "points": 20, "detail": f"LOS {los} days >= 14"})
    elif los >= 7:
        score += 12
        factors.append({"factor": "moderate_stay", "points": 12, "detail": f"LOS {los} days 7-13"})
    elif los >= 4:
        score += 5
        factors.append({"factor": "short_stay", "points": 5, "detail": f"LOS {los} days 4-6"})

    # Prior admissions
    prior = data["num_prior_admissions"]
    if prior >= 3:
        score += 20
        factors.append({"factor": "frequent_admissions", "points": 20, "detail": f"{prior} prior admissions"})
    elif prior >= 1:
        score += 10
        factors.append({"factor": "prior_admissions", "points": 10, "detail": f"{prior} prior admission(s)"})

    # Chronic conditions
    chronic = data["num_chronic_conditions"]
    score += min(chronic * 5, 20)
    if chronic > 0:
        factors.append({"factor": "chronic_conditions", "points": min(chronic * 5, 20), "detail": f"{chronic} chronic conditions"})

    # Specific conditions
    if data.get("has_diabetes"):
        score += 8
        factors.append({"factor": "diabetes", "points": 8, "detail": "Diabetes present"})
    if data.get("has_heart_failure"):
        score += 12
        factors.append({"factor": "heart_failure", "points": 12, "detail": "Heart failure present"})

    # Discharge disposition
    if data["discharge_disposition"] != "home":
        score += 5
        factors.append({"factor": "non_home_discharge", "points": 5, "detail": f"Discharged to {data['discharge_disposition']}"})

    # Normalize to 0-100
    risk_pct = min(score, 100)
    risk_level = "low" if risk_pct < 25 else "moderate" if risk_pct < 50 else "high" if risk_pct < 75 else "very_high"

    return {
        "risk_score": risk_pct,
        "risk_level": risk_level,
        "risk_factors": factors,
        "recommendation": _readmission_recommendation(risk_level),
    }


def compute_chronic_risk(data: dict) -> dict:
    """Assess risk for chronic conditions (diabetes, cardiovascular)."""
    risks = []

    # Cardiovascular risk (simplified Framingham-inspired)
    cv_score = 0.0
    cv_factors = []

    if data["age"] >= 55:
        cv_score += 15
        cv_factors.append("age >= 55")
    elif data["age"] >= 45:
        cv_score += 8
        cv_factors.append("age 45-54")

    if data["systolic_bp"] >= 140:
        cv_score += 20
        cv_factors.append(f"high systolic BP ({data['systolic_bp']})")
    elif data["systolic_bp"] >= 130:
        cv_score += 10
        cv_factors.append(f"elevated systolic BP ({data['systolic_bp']})")

    if data["total_cholesterol"] >= 240:
        cv_score += 15
        cv_factors.append(f"high cholesterol ({data['total_cholesterol']})")
    elif data["total_cholesterol"] >= 200:
        cv_score += 8
        cv_factors.append(f"borderline cholesterol ({data['total_cholesterol']})")

    if data["hdl_cholesterol"] < 40:
        cv_score += 10
        cv_factors.append(f"low HDL ({data['hdl_cholesterol']})")

    if data["smoker"]:
        cv_score += 15
        cv_factors.append("current smoker")

    if data["family_history"]:
        cv_score += 10
        cv_factors.append("family history of CVD")

    risks.append({
        "condition": "cardiovascular_disease",
        "risk_score": min(cv_score, 100),
        "risk_level": _risk_level(cv_score),
        "factors": cv_factors,
    })

    # Diabetes risk
    dm_score = 0.0
    dm_factors = []

    if data["bmi"] >= 30:
        dm_score += 20
        dm_factors.append(f"obese (BMI {data['bmi']})")
    elif data["bmi"] >= 25:
        dm_score += 10
        dm_factors.append(f"overweight (BMI {data['bmi']})")

    if data["fasting_glucose"] >= 126:
        dm_score += 30
        dm_factors.append(f"diabetic range glucose ({data['fasting_glucose']})")
    elif data["fasting_glucose"] >= 100:
        dm_score += 15
        dm_factors.append(f"pre-diabetic glucose ({data['fasting_glucose']})")

    if data["age"] >= 45:
        dm_score += 10
        dm_factors.append("age >= 45")

    if data["family_history"]:
        dm_score += 10
        dm_factors.append("family history")

    risks.append({
        "condition": "type_2_diabetes",
        "risk_score": min(dm_score, 100),
        "risk_level": _risk_level(dm_score),
        "factors": dm_factors,
    })

    return {"assessments": risks}


def _risk_level(score: float) -> str:
    if score < 20:
        return "low"
    if score < 40:
        return "moderate"
    if score < 60:
        return "high"
    return "very_high"


def _readmission_recommendation(level: str) -> str:
    recs = {
        "low": "Standard discharge planning. Follow-up in 2-4 weeks.",
        "moderate": "Enhanced discharge planning. Schedule follow-up within 7-14 days. Consider transitional care.",
        "high": "Intensive transitional care. Follow-up within 48-72 hours. Home health referral recommended.",
        "very_high": "High-intensity intervention required. Same-day follow-up call. Home health + care coordination. Consider post-acute facility.",
    }
    return recs.get(level, "")
