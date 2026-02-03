def validate_action(weight_grams: float):
    if weight_grams <= 0:
        return {"validated": False, "confidence": 0.0}

    confidence = min(0.95, 0.7 + (weight_grams / 1000))
    return {
        "validated": True,
        "confidence": round(confidence, 2)
    }
