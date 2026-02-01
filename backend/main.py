from fastapi import FastAPI
from backend.schemas.dataset_summary import DatasetSummary
from backend.audit.statistical_checks import (
    check_missing_values,
    check_outliers,
    check_correlation,
    check_bias
)
from backend.trust.trust_engine import trust_decision

# NEW imports for training
from backend.data.load_dataset import load_dataset
from backend.training.data_preprocessing import prepare_data
from backend.training.train_model import train_model

app = FastAPI() #initialize FastAPI app

DATASET_PATH = "backend/data/Loan Dataset.csv"
TARGET_COLUMN = "Loan_Approval_Status"

@app.post("/audit")
def audit_dataset(summary: DatasetSummary):
    # 1️ Run audit checks
    missing_issues = check_missing_values(summary.features)
    outlier_issues = check_outliers(summary.features)
    correlation_issues = check_correlation(summary.features)
    bias_issues = check_bias(summary.features)

    all_issues = (
        missing_issues
        + outlier_issues
        + correlation_issues
        + bias_issues
    )

    # 2️ Compute quality score
    BASE_SCORE = 100
    PENALTY_PER_ISSUE = 10
    quality_score = max(0, BASE_SCORE - PENALTY_PER_ISSUE * len(all_issues))

    # 3 Trust decision
    trust = trust_decision(quality_score)
    training_allowed = trust == "ALLOW"

    response = {
        "audit_report": {
            "missing_values": missing_issues,
            "outliers": outlier_issues,
            "correlation_issues": correlation_issues,
            "bias_risks": bias_issues
        },
        "quality_score": quality_score,
        "trust_decision": trust,
        "training_allowed": training_allowed
    }

    # 4️ Train model ONLY if allowed
    if training_allowed:
        df = load_dataset(DATASET_PATH)

        print("DATASET LOADED SUCCESSFULLY")
        print(df.head())

        X_train, X_test, y_train, y_test = prepare_data(df, TARGET_COLUMN)
        model, accuracy = train_model(X_train, X_test, y_train, y_test)

        response["model_accuracy"] = accuracy

    return response
