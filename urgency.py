def classify_urgency(text, sentiment_label):
    text_lower = text.lower()

    high_keywords = ["no water", "emergency", "danger", "not safe"]
    medium_keywords = ["delay", "no response", "problem"]

    # HIGH
    if any(word in text_lower for word in high_keywords) or sentiment_label == "NEGATIVE":
        return "HIGH"

    # MEDIUM
    if any(word in text_lower for word in medium_keywords):
        return "MEDIUM"

    return "LOW"


def should_escalate(urgency, sentiment_label, score):
    if urgency == "HIGH":
        return True

    if sentiment_label == "NEGATIVE" and score > 0.85:
        return True

    return False