import random

def predict_risk(description: str):
    text = description.lower()
    risk = "Low"
    confidence = random.randint(60, 75)
    features = ["token degree", "syntactic edges", "TF-IDF"]

    if any(keyword in text for keyword in ["remote code", "exec", "rce"]):
        risk = "High"
        confidence = random.randint(90, 97)
        features = ["function graph", "call graph", "API node embeddings"]

    elif any(keyword in text for keyword in ["xss", "script", "html injection"]):
        risk = "Medium"
        confidence = random.randint(80, 88)
        features = ["DOM graph", "input-output edge", "token node degree"]

    return {
        "risk": risk,
        "confidence": confidence,
        "features": features
    }
