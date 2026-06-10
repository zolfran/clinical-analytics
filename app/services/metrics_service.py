"""Clinical quality metrics computation.

Implements simplified versions of CMS quality measures:
- Diabetes HbA1c control
- Hypertension BP control
- Preventive care screening rates
"""


def compute_quality_metrics() -> dict:
    """Compute population-level quality metrics with simulated data."""
    metrics = [
        {
            "id": "CMS122",
            "name": "Diabetes: Hemoglobin A1c Poor Control (>9%)",
            "description": "Percentage of patients 18-75 with diabetes whose HbA1c was >9.0%",
            "numerator": 12,
            "denominator": 85,
            "rate": round(12 / 85 * 100, 1),
            "benchmark": 15.0,
            "status": "meeting",
            "trend": [18.2, 16.5, 15.1, 14.1],
        },
        {
            "id": "CMS165",
            "name": "Controlling High Blood Pressure",
            "description": "Percentage of patients 18-85 with hypertension whose BP was <140/90",
            "numerator": 198,
            "denominator": 260,
            "rate": round(198 / 260 * 100, 1),
            "benchmark": 72.0,
            "status": "meeting",
            "trend": [68.5, 71.2, 74.0, 76.2],
        },
        {
            "id": "CMS125",
            "name": "Breast Cancer Screening",
            "description": "Women 50-74 who had a mammogram in the past 27 months",
            "numerator": 142,
            "denominator": 195,
            "rate": round(142 / 195 * 100, 1),
            "benchmark": 75.0,
            "status": "needs_improvement",
            "trend": [65.3, 68.1, 70.5, 72.8],
        },
        {
            "id": "CMS130",
            "name": "Colorectal Cancer Screening",
            "description": "Patients 45-75 appropriately screened for colorectal cancer",
            "numerator": 180,
            "denominator": 310,
            "rate": round(180 / 310 * 100, 1),
            "benchmark": 65.0,
            "status": "needs_improvement",
            "trend": [52.1, 55.8, 57.2, 58.1],
        },
        {
            "id": "CMS138",
            "name": "Preventive Care: Tobacco Screening",
            "description": "Patients 18+ screened for tobacco use and received cessation intervention",
            "numerator": 412,
            "denominator": 450,
            "rate": round(412 / 450 * 100, 1),
            "benchmark": 85.0,
            "status": "meeting",
            "trend": [82.5, 86.1, 89.3, 91.6],
        },
    ]

    meeting = sum(1 for m in metrics if m["status"] == "meeting")

    return {
        "reporting_period": "Q1 2026",
        "total_metrics": len(metrics),
        "meeting_benchmark": meeting,
        "needs_improvement": len(metrics) - meeting,
        "metrics": metrics,
    }
