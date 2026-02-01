def compute_quality_score(stats, bias, leakage):
    score = 100
    score -= 10 * len(stats) # each statistical issue deducts 10 points
    score -= 15 * len(bias) # each bias issue deducts 15 points
    score -= 20 * len(leakage) # each data leakage issue deducts 20 points
    return max(score, 0) # ensure score doesn't go below 0

def allow_training(score, threshold=75):
    return score >= threshold
