from gtts import gTTS
import tempfile
import os


def generate_voice_response(text, lang="en"):
    try:
        tts = gTTS(text=text, lang=lang)

        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_path = temp_audio.name

        tts.save(temp_path)

        return temp_path

    except Exception:
        return None