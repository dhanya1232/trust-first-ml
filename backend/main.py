# backend/main.py
from fastapi import FastAPI
from backend.schemas.dataset_summary import DatasetSummary
from backend.audit.statistical_checks import check_missing_values, check_outliers, check_correlation, check_bias

app = FastAPI()

@app.post("/audit")
def audit_dataset(summary: DatasetSummary):
    missing_issues = check_missing_values(summary.features)
    outlier_issues = check_outliers(summary.features)
    correlation_issues = check_correlation(summary.features)
    bias_issues = check_bias(summary.features)

    all_issues = missing_issues + outlier_issues + correlation_issues

    quality_score = 100 - 10 * len(all_issues)
    training_allowed = quality_score >= 75

    return {
        "audit_report": {
            "missing_values": missing_issues,
            "outlier_issues": outlier_issues,
            "correlation_issues": correlation_issues,
            "bias_risks": bias_issues,
        },
        "quality_score": quality_score,
        "training_allowed": training_allowed
    }
