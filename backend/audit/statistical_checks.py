# backend/audit/statistical_checks.py

def check_missing_values(features):
    issues = []
    for name, info in features.items():
        if info.missing.endswith('%') and float(info.missing[:-1]) > 5:
            issues.append(f"{name} has high missing rate ({info.missing})")
    return issues

def check_outliers(features):
    issues = []
    for name, info in features.items():
        if info.type == "numeric" and info.range:
            min_val, max_val = map(float, info.range.split('-'))
            if (max_val - min_val) > 1000:  # arbitrary threshold for demo
                issues.append(f"{name} may have outliers (range {info.range})")
    return issues

def check_correlation(features):
    return []  # placeholder

def check_bias(features):
    issues = []
    for name, info in features.items():
        if name.lower() in ["gender", "age", "race"]:
            issues.append(f"{name} may introduce bias")
    return issues
