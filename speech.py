import whisper
import tempfile
import os

# Load model once
model = whisper.load_model("base")

def transcribe_audio(audio_file):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_file.read())
            tmp_path = tmp.name

        result = model.transcribe(tmp_path)
        os.remove(tmp_path)

        return result["text"]

    except Exception as e:
        return None