# Clinical Analytics Service

A **population health analytics** and **risk scoring** microservice built with Python, FastAPI, and pandas. This service provides clinical quality metrics (CQMs), readmission risk prediction, chronic disease risk assessment, and population health dashboards.

## Features

- **Clinical Quality Metrics** — CMS quality measures (HbA1c control, BP control, cancer screenings, tobacco screening)
- **Readmission Risk Scoring** — LACE-inspired 30-day readmission risk prediction with actionable recommendations
- **Chronic Disease Risk** — Cardiovascular and Type 2 diabetes risk assessment based on clinical indicators
- **Population Health** — Demographics, condition prevalence, healthcare utilization, and preventive care metrics
- **REST API** — FastAPI with auto-generated OpenAPI docs

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 3002

# API docs at http://localhost:3002/docs
```

## API Endpoints

### Clinical Quality Metrics
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/metrics/quality` | All quality metrics with benchmarks |
| `GET` | `/api/v1/metrics/quality/{id}` | Single metric detail (e.g., CMS122) |

### Risk Scoring
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/risk/readmission` | 30-day readmission risk prediction |
| `POST` | `/api/v1/risk/chronic-disease` | Chronic disease risk assessment |

### Population Health
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/population/summary` | Population overview stats |
| `GET` | `/api/v1/population/age-distribution` | Age demographics |
| `GET` | `/api/v1/population/conditions` | Chronic condition prevalence |
| `GET` | `/api/v1/population/utilization` | Healthcare utilization stats |

### Example: Readmission Risk

```bash
curl -X POST http://localhost:3002/api/v1/risk/readmission \
  -H "Content-Type: application/json" \
  -d '{
    "age": 72,
    "length_of_stay_days": 8,
    "num_prior_admissions": 2,
    "num_chronic_conditions": 3,
    "has_diabetes": true,
    "has_heart_failure": false,
    "discharge_disposition": "home"
  }'
```

## Project Structure

```
clinical-analytics/
├── app/
│   ├── main.py                    # FastAPI app
│   ├── routers/
│   │   ├── metrics.py             # Quality metrics endpoints
│   │   ├── risk.py                # Risk scoring endpoints
│   │   └── population.py          # Population health endpoints
│   └── services/
│       ├── metrics_service.py     # CQM computation
│       ├── risk_service.py        # Risk models
│       └── population_service.py  # Population analytics
├── tests/
│   └── test_risk.py
└── requirements.txt
```

## Related Repos

- [healthcare-modernization](https://github.com/zolfran/healthcare-modernization) — Full-stack healthcare platform
- [legacy-hl7-processor](https://github.com/zolfran/legacy-hl7-processor) — Legacy HL7v2 message parser
- [fhir-integration-service](https://github.com/zolfran/fhir-integration-service) — FHIR R4 integration microservice
- [patient-portal](https://github.com/zolfran/patient-portal) — Patient-facing web app

## License

MIT
