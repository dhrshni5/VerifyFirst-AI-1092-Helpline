from transformers import pipeline

# Load once
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    try:
        result = sentiment_pipeline(text)[0]
        return result["label"], float(result["score"])
    except Exception:
        return "UNKNOWN", 0.0