import streamlit as st

from utils.speech import transcribe_audio
from utils.summarizer import summarize_text
from utils.sentiment import analyze_sentiment
from utils.urgency import classify_urgency, should_escalate
from utils.voice import generate_voice_response
st.set_page_config(page_title="AI 1092 Assistant", layout="wide")

st.markdown(
    """
    <style>
        /* Main app background */
        .stApp {
            background-color: #f5f7fa;
            color: #111111 !important;
        }

        /* ALL NORMAL TEXT */
        html, body, p, span, label, div {
            color: #111111 !important;
        }

        /* HEADERS */
        h1, h2, h3, h4 {
            color: #111111 !important;
        }

        /* DARK HEADER SECTION */
        .header-box {
            background-color: #0b1f3a;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }

        /* TEXT INSIDE DARK HEADER */
        .header-box h1,
        .header-box h3,
        .header-box p,
        .header-box span {
            color: #ffffff !important;
        }

        /* SIDEBAR */
        section[data-testid="stSidebar"] {
            background-color: #0b1f3a;
        }

        /* SIDEBAR TEXT */
        section[data-testid="stSidebar"] * {
            color: #ffffff !important;
        }

        /* WHITE CARDS */
        .card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #dcdcdc;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
            color: #111111 !important;
        }

        /* INPUT BOX TEXT */
        textarea,
        input,
        .stTextInput input,
        .stTextArea textarea {
            color: #111111 !important;
            background-color: #ffffff !important;
        }

        /* PLACEHOLDER TEXT */
        textarea::placeholder,
        input::placeholder {
            color: #555555 !important;
        }

        /* RADIO BUTTON LABELS */
        .stRadio label {
            color: #111111 !important;
        }

        /* FILE UPLOADER */
        [data-testid="stFileUploader"] * {
            color: #111111 !important;
        }
        [data-testid="stFileUploaderDropzoneInstructions"] *,
        [data-testid="stFileUploaderDropzone"] small,
        [data-testid="stFileUploaderDropzone"] button,
        [data-testid="stFileUploaderDropzone"] button * {
            color: #f5f7fa !important;
        }

        /* BUTTONS */
        .stButton button {
            background-color: #ff9933;
            color: #ffffff !important;
            border-radius: 10px;
            border: none;
            font-weight: bold;
        }

        /* HIGH ALERT */
        .high-alert {
            background-color: #d62828;
            color: #ffffff !important;
            padding: 15px;
            border-radius: 10px;
        }

        /* MEDIUM ALERT */
        .medium-alert {
            background-color: #ff9933;
            color: #ffffff !important;
            padding: 15px;
            border-radius: 10px;
        }

        /* LOW ALERT */
        .low-alert {
            background-color: #138808;
            color: #ffffff !important;
            padding: 15px;
            border-radius: 10px;
        }

        /* FOOTER */
        .footer {
            text-align: center;
            color: #111111 !important;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="header-box">
        <div style="font-size:1.7rem;">🚨</div>
        <h1>AI Voice Assistant for 1092 Helpline</h1>
        <h3>Multilingual Citizen Complaint Analysis System</h3>
        <p>Supports English • Hindi • Kannada</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## About Project")
    st.write(
        "This AI prototype assists government helplines by analyzing citizen complaints using speech and NLP."
    )
    st.markdown("---")
    st.markdown("### Supported Languages")
    st.markdown("- English\n- Hindi\n- Kannada")
    st.markdown("### Features")
    st.markdown(
        "- Speech-to-Text\n- Sentiment Detection\n- Urgency Classification\n- Escalation Detection\n- AI Verification"
    )
    st.markdown("### Emergency Note")
    st.warning("High urgency complaints are flagged for escalation.")

# ---------------- INPUT ---------------- #
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 1) Input Section")
input_mode = st.radio("Choose Input Method", ["Upload Audio", "Type Text"], horizontal=True)

user_text = ""

if input_mode == "Upload Audio":
    audio_file = st.file_uploader(
        "Upload Audio File",
        type=["wav", "mp3", "m4a"],
        help="Supported formats: WAV, MP3, M4A",
    )
    st.caption("Supported formats: WAV, MP3, M4A")

    if audio_file is not None:
        with st.spinner("Analyzing citizen complaint..."):
            st.info("Processing uploaded audio for transcription...")
            transcript = transcribe_audio(audio_file)

            if transcript:
                st.success("Transcription successful.")
                st.write("📝 Transcription:", transcript)
                user_text = transcript
            else:
                st.error("Audio processing failed. Please type your issue below.")
                user_text = st.text_area("Enter your issue:")

else:
    user_text = st.text_area("Describe your issue:")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PROCESS ---------------- #
if st.button("Analyze", use_container_width=True):

    if not user_text or len(user_text.strip()) == 0:
        st.warning("Please provide input.")
    else:
        with st.spinner("Analyzing citizen complaint..."):
            st.info("Running AI analysis modules...")
            # Summary
            summary = summarize_text(user_text)

            # Sentiment
            sentiment_label, sentiment_score = analyze_sentiment(user_text)

            # Urgency
            urgency = classify_urgency(user_text, sentiment_label)

            # Escalation
            escalation = should_escalate(urgency, sentiment_label, sentiment_score)

        # ---------------- OUTPUT ---------------- #
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 2) AI Analysis Section")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""
                <div class="card">
                    <div><strong>Transcription</strong></div>
                    <div>{user_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="card">
                    <div><strong>Sentiment</strong></div>
                    <div>{sentiment_label} ({sentiment_score:.2f})</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="card">
                    <div><strong>Escalation Status</strong></div>
                    <div>{"YES" if escalation else "NO"}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ---------------- AI VOICE RESPONSE ---------------- #

        st.subheader("🎤 AI Voice Response")

        voice_message = ""

        if urgency == "HIGH":
            voice_message = "High priority complaint detected. Human review has been initiated."

        elif escalation:
            voice_message = "Your complaint requires escalation to a human officer."

        else:
            voice_message = "Your complaint has been registered successfully."

        # Language Selection
        voice_language = st.selectbox(
            "Select Voice Language",
            ["English", "Hindi", "Kannada"]
        )

        lang_code = "en"

        if voice_language == "Hindi":
            lang_code = "hi"

        elif voice_language == "Kannada":
            lang_code = "kn"

        audio_path = generate_voice_response(
            voice_message,
            lang=lang_code
        )

        if audio_path:
            st.audio(audio_path)
        else:
            st.warning("Voice response could not be generated.")

        with col2:
            st.markdown(
                f"""
                <div class="card">
                    <div><strong>Summary</strong></div>
                    <div>{summary}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="card">
                    <div><strong>Urgency</strong></div>
                    <div>{urgency}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            urgency_level = urgency.strip().upper()
            if urgency_level == "HIGH":
                st.markdown(
                    '<div class="high-alert">🚨 HIGH URGENCY: Immediate attention required.</div>',
                    unsafe_allow_html=True,
                )
            elif urgency_level == "MEDIUM":
                st.markdown(
                    '<div class="medium-alert">⚠️ MEDIUM URGENCY: Prompt review recommended.</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    '<div class="low-alert">✅ LOW URGENCY: Standard processing is sufficient.</div>',
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- VERIFICATION ---------------- #
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 3) Verification Section")
        st.markdown("**Is this understanding correct?**")

        feedback = st.radio(
            "Verification Options",
            ["✅ Correct", "⚠️ Partially Correct", "❌ Incorrect"],
            label_visibility="collapsed",
            horizontal=True,
        )

        if feedback == "✅ Correct":
            st.markdown(
                '<div class="low-alert"><strong>✅ Complaint verified successfully.</strong></div>',
                unsafe_allow_html=True,
            )

        elif feedback == "⚠️ Partially Correct":
            corrected_text = st.text_area("Please provide the corrected complaint details:")
            st.markdown(
                '<div class="medium-alert"><strong>⚠️ Minor clarification required before processing.</strong></div>',
                unsafe_allow_html=True,
            )
            if corrected_text:
                st.success("Updated Input Saved")
                st.write(corrected_text)

        elif feedback == "❌ Incorrect":
            st.markdown(
                '<div class="high-alert"><strong>🚨 AI understanding mismatch detected.<br>This complaint has been escalated to a human officer for safety verification.</strong></div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="high-alert"><strong>Manual review recommended to avoid misclassification of critical complaints.</strong></div>',
                unsafe_allow_html=True,
            )
            corrected_text = st.text_area("Please correct the issue:")
            if corrected_text:
                st.success("Updated Input Saved")
                st.write(corrected_text)

        if urgency_level == "HIGH":
            st.markdown(
                '<div class="high-alert"><strong>🚨 High priority complaint detected.<br>Human monitoring recommended.</strong></div>',
                unsafe_allow_html=True,
            )
            if feedback == "❌ Incorrect":
                st.markdown(
                    '<div class="high-alert"><strong>🚨 Immediate human intervention required.</strong></div>',
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    '<div class="footer">Built for Smart Governance & Public Safety</div>',
    unsafe_allow_html=True,
)