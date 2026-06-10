"""Population health analytics with simulated data."""

import numpy as np


def get_population_summary() -> dict:
    """High-level population health summary."""
    return {
        "total_patients": 2450,
        "active_patients": 2180,
        "avg_age": 47.3,
        "gender_breakdown": {"male": 1175, "female": 1250, "other": 25},
        "payer_mix": {
            "commercial": 1100,
            "medicare": 625,
            "medicaid": 420,
            "self_pay": 180,
            "other": 125,
        },
        "risk_stratification": {
            "low_risk": 1350,
            "moderate_risk": 720,
            "high_risk": 310,
            "very_high_risk": 70,
        },
    }


def get_age_distribution() -> dict:
    """Age distribution across the population."""
    rng = np.random.default_rng(42)
    ages = rng.normal(loc=47, scale=18, size=2450).clip(0, 100).astype(int)

    bins = [(0, 17), (18, 34), (35, 49), (50, 64), (65, 79), (80, 100)]
    labels = ["0-17", "18-34", "35-49", "50-64", "65-79", "80+"]

    distribution = []
    for (lo, hi), label in zip(bins, labels):
        count = int(((ages >= lo) & (ages <= hi)).sum())
        distribution.append({"age_group": label, "count": count, "percentage": round(count / len(ages) * 100, 1)})

    return {"total": len(ages), "distribution": distribution}


def get_condition_prevalence() -> dict:
    """Chronic condition prevalence in the population."""
    conditions = [
        {"condition": "Hypertension", "icd10": "I10", "count": 680, "prevalence_pct": 27.8},
        {"condition": "Type 2 Diabetes", "icd10": "E11", "count": 385, "prevalence_pct": 15.7},
        {"condition": "Hyperlipidemia", "icd10": "E78.5", "count": 520, "prevalence_pct": 21.2},
        {"condition": "Obesity", "icd10": "E66", "count": 445, "prevalence_pct": 18.2},
        {"condition": "Depression", "icd10": "F32", "count": 310, "prevalence_pct": 12.7},
        {"condition": "Asthma", "icd10": "J45", "count": 215, "prevalence_pct": 8.8},
        {"condition": "COPD", "icd10": "J44", "count": 145, "prevalence_pct": 5.9},
        {"condition": "Heart Failure", "icd10": "I50", "count": 98, "prevalence_pct": 4.0},
        {"condition": "Chronic Kidney Disease", "icd10": "N18", "count": 115, "prevalence_pct": 4.7},
        {"condition": "Atrial Fibrillation", "icd10": "I48", "count": 78, "prevalence_pct": 3.2},
    ]

    return {
        "total_patients": 2450,
        "patients_with_chronic_conditions": 1520,
        "avg_conditions_per_patient": 2.1,
        "conditions": conditions,
    }


def get_utilization_stats() -> dict:
    """Healthcare utilization metrics."""
    return {
        "period": "Q1 2026",
        "ed_visits": {
            "total": 342,
            "per_1000_patients": 139.6,
            "avoidable_pct": 28.5,
            "top_reasons": [
                {"reason": "Chest pain", "count": 45},
                {"reason": "Abdominal pain", "count": 38},
                {"reason": "Respiratory distress", "count": 32},
                {"reason": "Falls/injuries", "count": 28},
                {"reason": "Mental health crisis", "count": 22},
            ],
        },
        "inpatient_admissions": {
            "total": 128,
            "per_1000_patients": 52.2,
            "avg_length_of_stay": 4.2,
            "readmission_rate_30day": 12.5,
        },
        "outpatient_visits": {
            "total": 4850,
            "per_1000_patients": 1979.6,
            "telehealth_pct": 22.3,
        },
        "preventive_care": {
            "annual_wellness_visit_pct": 68.2,
            "flu_vaccination_pct": 52.1,
            "covid_vaccination_pct": 71.8,
        },
    }
