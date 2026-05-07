def summarize_text(text):
    if not text or len(text.strip()) == 0:
        return "No valid input provided."

    # Simple clean summary logic
    sentences = text.split(".")
    main_sentence = sentences[0].strip()

    if len(main_sentence) < 10 and len(sentences) > 1:
        main_sentence = sentences[1].strip()

    return f"Citizen reports: {main_sentence}"