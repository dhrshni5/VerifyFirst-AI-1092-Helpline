# VerifyFirst – AI Voice-to-Voice Assistant for 1092 Helpline

## Overview

VerifyFirst is a multilingual AI-powered Voice-to-Voice Assistant designed for the 1092 Government Helpline system.

The project helps automate citizen complaint handling using speech recognition, AI-based analysis, urgency detection, human escalation, and AI-generated voice responses.

This prototype was developed as a hackathon solution focused on smart governance and public safety.

---

# Features

- 🎤 Voice Complaint Input
- ⌨️ Text-Based Complaint Input
- 🌍 Multilingual Support
  - English
  - Hindi
  - Kannada
- 🧠 AI Speech-to-Text using Whisper
- 📝 Complaint Summarization
- 😊 Sentiment Analysis
- 🚨 Urgency Classification
- 👨‍💼 Human Escalation System
- 🔊 AI Voice Response
- ✔️ Verification & Confirmation Workflow
- 🛡️ Error Handling & Fallback Support

---

# Problem Statement

Government helplines often face:
- Delayed complaint processing
- Manual workload
- Misclassification of urgent complaints
- Language accessibility barriers

VerifyFirst aims to improve complaint handling through AI-assisted automation and multilingual accessibility.

---

# Workflow

Citizen Voice Input  
↓  
Speech-to-Text (Whisper)  
↓  
Complaint Summarization  
↓  
Sentiment Analysis  
↓  
Urgency Classification  
↓  
Human Escalation (if required)  
↓  
AI Voice Response

---

# Tech Stack

- Python
- Streamlit
- OpenAI Whisper
- Transformers
- gTTS
- FFmpeg

---

# Project Structure

```bash
ai-1092-prototype/
│
├── app.py
├── requirements.txt
└── utils/
    ├── speech.py
    ├── summarizer.py
    ├── sentiment.py
    ├── urgency.py
    └── voice.py
