def classify_text(text: str) -> str:
    """
    Classify input text as positive, negative, or neutral.
    """

    if not text or not text.strip():
        return "neutral"

    text = text.lower()

    positive_words = ["good", "great", "excellent", "happy", "love", "awesome"]
    negative_words = ["bad", "poor", "sad", "angry", "hate", "terrible"]

    for word in positive_words:
        if word in text:
            return "positive"

    for word in negative_words:
        if word in text:
            return "negative"

    return "neutral"