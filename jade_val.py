import streamlit as st
import random
import time
from io import BytesIO
from reportlab.lib.pagesizes import LETTER   # ← Use uppercase LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# ---------------- SESSION STATE ----------------
if "predicted" not in st.session_state:
    st.session_state.predicted = False
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "letter_shown" not in st.session_state:
    st.session_state.letter_shown = False
if "music_triggered" not in st.session_state:
    st.session_state.music_triggered = False

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Jadesola Valentine Model 💖",
    page_icon="💘",
    layout="centered"
)

st.title("💘 Jadesola Valentine Acceptance Model")
st.caption("Built by a Data Scientist who already knows the answer 😌")
st.write("""
Welcome, **Jadesola** 👋  
This model was trained on laughter, trust, vibes, and a ridiculous amount of affection 💕
""")
st.divider()

# ---------------- INPUT FEATURES ----------------
st.subheader("📊 Input Features")

st.slider("Affection Level", 0, 100, 97)
st.slider("Laughs at my jokes (%)", 0, 100, 99)
st.slider("Trust Level", 0, 100, 100)
st.selectbox("Overall Relationship Vibe", ["Immaculate ✨", "Perfect 💕", "Unmatched 🔥"])

st.divider()

# ---------------- RUN MODEL ----------------
if st.button("Run Valentine Prediction 🚀"):
    with st.spinner("Training emotional neural network..."):
        time.sleep(2)
    st.session_state.predicted = True

# ---------------- MODEL OUTPUT ----------------
if st.session_state.predicted:
    probability = round(random.uniform(0.97, 0.995), 3)
    st.success("🎉 MODEL OUTPUT")
    st.metric("Prediction", "YES 💖")
    st.metric("Confidence Score", f"{probability * 100}%")

    st.markdown("""
    ### 🧠 Model Explanation
    - Affection ➜ dominant feature  
    - Laughter ➜ overfitting confirmed 😂  
    - Trust ➜ perfect signal  
    - Vibes ➜ unquantifiable but elite  

    **Conclusion:**  
    No alternative outcome was mathematically possible.
    """)

    st.divider()

    # ---------------- PRIVATE MESSAGE ----------------
    st.subheader("🔐 Private Message (Restricted Access)")
    secret = st.text_input("Enter the secret key to unlock 💖", type="password")

    if secret.lower() == "jadesola":
        st.success("Access granted 💘")
        st.markdown("""
        💌 **Private Message**  

        Jadesola, this isn’t about code, models, or predictions.  
        I genuinely enjoy you, admire you, and want to create beautiful memories with you.  
        This app is just my nerdy way of asking properly 😌❤️  

        **You matter to me.**
        """)
    elif secret:
        st.error("Access denied ❌ (Hint: your name 😉)")

    st.divider()

    # ---------------- FINAL QUESTION ----------------
    st.markdown("## 💖 Jadesola, will you be my Valentine?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES 💘"):
            st.session_state.accepted = True
            st.session_state.letter_shown = True
            st.session_state.music_triggered = True   # ← Trigger music after click
    with col2:
        st.button("NO 😅")

# ---------------- LOVE LETTER + CERTIFICATE + MUSIC ----------------
if st.session_state.letter_shown:
    st.success("🥰 Valentine confirmed!")
    st.balloons()
    st.snow()

    # ── Background Music ── (starts after user interaction = YES click)
    # Royalty-free soft romantic piano loop example from Pixabay
    # Replace URL with your own if you upload to GitHub repo or external host
    music_url = "https://cdn.pixabay.com/audio/2023/08/07/audio_3d0d6d6d1d.mp3"

    # Hidden autoplay (may work after interaction)
    if st.session_state.music_triggered:
        music_html = f"""
        <audio autoplay loop style="display: none;">
            <source src="{music_url}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        """
        st.markdown(music_html, unsafe_allow_html=True)

    # Visible fallback button (recommended – most reliable)
    st.caption("🎶 Romantic background music")
    if st.button("Play / Restart Music 🎵"):
        st.markdown(f"""
        <audio autoplay loop>
            <source src="{music_url}" type="audio/mpeg">
        </audio>
        """, unsafe_allow_html=True)
        st.session_state.music_triggered = True

    st.subheader("💌 A Letter For You")

    letter = (
        "Dear Jadesola,\n\n"
        "This message may look like plain text, but it’s actually a carefully structured signal originating from the heart layer.\n\n"
        "Your presence has a way of making everything feel lighter, brighter, and more meaningful. You bring joy effortlessly, "
        "and that is something I deeply admire.\n\n"
        "If permitted, I’d like to allocate Valentine’s Day to us — no unnecessary features, "
        "just meaningful execution and memories safely persisted.\n\n"
        "Consistently yours,\n"
        "Ayomide 💖"
    )

    placeholder = st.empty()
    displayed = ""
    for char in letter:
        displayed += char
        placeholder.markdown(f"```\n{displayed}\n```")
        time.sleep(0.035)

    st.divider()

    # ── REAL PDF CERTIFICATE ───────────────────────────────────────────────────────────────
    st.subheader("📄 Valentine Certificate")

    # Generate PDF in memory
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=LETTER)
    width, height = LETTER  # Safe: LETTER is (612.0, 792.0)

    # Light pink background
    c.setFillColorRGB(1.0, 0.96, 0.98)
    c.rect(0, 0, width, height, fill=1)

    # Title
    c.setFillColorRGB(0.8, 0.1, 0.3)  # rose red
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(width / 2, height - 1.5 * inch, "💖 Valentine Certificate 💖")

    # Content
    c.setFillColorRGB(0.4, 0.4, 0.6)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height - 3 * inch, "This certifies that")

    c.setFillColorRGB(0.9, 0.2, 0.4)
    c.setFont("Helvetica-Bold", 48)
    c.drawCentredString(width / 2, height - 4.3 * inch, "JADESOLA")

    c.setFillColorRGB(0.4, 0.4, 0.6)
    c.setFont("Helvetica", 24)
    c.drawCentredString(width / 2, height - 5.5 * inch, "has officially accepted to be")

    c.setFillColorRGB(0.9, 0.2, 0.4)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(width / 2, height - 6.6 * inch, "My Valentine 💘")

    c.setFillColorRGB(0.5, 0.5, 0.7)
    c.setFont("Helvetica-Oblique", 18)
    c.drawCentredString(width / 2, height - 8 * inch, "Issued with ❤️ by Ayomide")
    c.drawCentredString(width / 2, height - 8.7 * inch, f"Date: {time.strftime('%B %d, %Y')}")

    # Decorative border
    c.setStrokeColorRGB(0.9, 0.4, 0.6)
    c.setLineWidth(8)
    margin = 0.6 * inch
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin)

    c.showPage()
    c.save()

    pdf_bytes = buffer.getvalue()
    buffer.close()

    # Download button
    st.download_button(
        label="📄 Download Official Valentine Certificate (PDF)",
        data=pdf_bytes,
        file_name="Valentine_Certificate_Jadesola.pdf",
        mime="application/pdf"
    )

    st.caption("ℹ️ Open in any PDF viewer to see your beautiful certificate!")
