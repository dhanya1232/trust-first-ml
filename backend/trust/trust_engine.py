def trust_decision(quality_score: int):
    if quality_score >= 80:
        return "ALLOW"
    elif quality_score >= 60:
        return "REVIEW"
    else:
        return "BLOCK"
