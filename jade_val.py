import streamlit as st
import random
import time
from io import BytesIO
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor

# ── Helper: Create pretty PDF from text ──────────────────────────────────────────────
def text_to_pdf(title: str, content: str, filename: str, is_letter=True):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=LETTER)
    width, height = LETTER

    # Soft background
    c.setFillColor(HexColor('#FFF0F5'))  # very light pink
    c.rect(0, 0, width, height, fill=1)

    # Margins & spacing
    left_margin = 1.5 * inch
    top_margin = height - 2.0 * inch
    line_height = 18

    # Title with hearts
    c.setFillColor(HexColor('#C71585'))  # medium violet red
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width / 2, top_margin, f"💖 {title} 💖")

    # Content text
    c.setFillColor(HexColor('#333333'))
    c.setFont("Helvetica", 13) if is_letter else c.setFont("Helvetica-Oblique", 13)

    y = top_margin - 1.2 * inch
    lines = content.split('\n')

    for line in lines:
        if y < 1.2 * inch:
            c.showPage()
            y = height - 1.5 * inch
            c.setFillColor(HexColor('#FFF0F5'))
            c.rect(0, 0, width, height, fill=1)

        words = line.split()
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if c.stringWidth(test_line) < (width - 2 * left_margin):
                current_line = test_line
            else:
                c.drawString(left_margin, y, current_line.strip())
                y -= line_height
                current_line = word + " "
        if current_line:
            c.drawString(left_margin, y, current_line.strip())
            y -= line_height + 4  # paragraph spacing

        y -= line_height // 2

    # Signature for letter
    if is_letter:
        c.setFont("Helvetica-Oblique", 14)
        c.setFillColor(HexColor('#FF69B4'))
        c.drawString(left_margin, y - 40, "Consistently yours,")
        c.drawString(left_margin + 1.2*inch, y - 60, "Ayomide 💖")

    c.save()
    buffer.seek(0)
    return buffer.getvalue(), filename


# ── SESSION STATE ────────────────────────────────────────────────────────────────
if "predicted" not in st.session_state:
    st.session_state.predicted = False
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "letter_shown" not in st.session_state:
    st.session_state.letter_shown = False
if "music_playing" not in st.session_state:
    st.session_state.music_playing = False


# ── PAGE CONFIG ──────────────────────────────────────────────────────────────────
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


# ── INPUT FEATURES ───────────────────────────────────────────────────────────────
st.subheader("📊 Input Features")

st.slider("Affection Level", 0, 100, 97)
st.slider("Laughs at my jokes (%)", 0, 100, 99)
st.slider("Trust Level", 0, 100, 100)
st.selectbox("Overall Relationship Vibe", ["Immaculate ✨", "Perfect 💕", "Unmatched 🔥"])

st.divider()


# ── RUN MODEL ────────────────────────────────────────────────────────────────────
if st.button("Run Valentine Prediction 🚀"):
    with st.spinner("Training emotional neural network..."):
        time.sleep(2)
    st.session_state.predicted = True


# ── MODEL OUTPUT ─────────────────────────────────────────────────────────────────
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

    # ── PRIVATE MESSAGE ──────────────────────────────────────────────────────────
    st.subheader("🔐 Private Message (Restricted Access)")
    secret = st.text_input("Enter the secret key to unlock 💖", type="password", key="secret_input")

    # Define message BEFORE the if block (fixes NameError)
    private_message = """
Jadesola, this isn’t about code, models, or predictions.
I genuinely enjoy you, admire you, and want to create beautiful memories with you.
This app is just my nerdy way of asking properly 😌❤️

You matter to me.
    """.strip()

    if secret.lower() == "jadesola":
        st.success("Access granted 💘")
        st.markdown("💌 **Private Message**  \n" + private_message.replace("\n", "  \n"))

        # Download as PDF
        pdf_data_priv, fname_priv = text_to_pdf(
            "Private Message",
            private_message,
            "Private_Message_To_Jadesola.pdf",
            is_letter=False
        )
        st.download_button(
            label="📥 Download Private Message (PDF)",
            data=pdf_data_priv,
            file_name=fname_priv,
            mime="application/pdf"
        )
    elif secret:
        st.error("Access denied ❌ (Hint: your name 😉)")

    st.divider()

    # ── FINAL QUESTION ───────────────────────────────────────────────────────────
    st.markdown("## 💖 Jadesola, will you be my Valentine?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES 💘"):
            st.session_state.accepted = True
            st.session_state.letter_shown = True
            st.session_state.music_playing = True
    with col2:
        st.button("NO 😅")


# ── LOVE LETTER + MUSIC + CERTIFICATE ────────────────────────────────────────────
if st.session_state.letter_shown:
    st.success("🥰 Valentine confirmed!")
    st.balloons()
    st.snow()

    # ── Music Player ──
    st.caption("🎶 Soft romantic background music (click play if needed)")

    # Royalty-free romantic piano example
    music_url = "https://www.fesliyanstudios.com/play-mp3/341"

    if st.session_state.music_playing:
        st.audio(music_url, format="audio/mp3", autoplay=False, loop=True)

    # ── Letter ────────────────────────────────────────────────────────────────
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

    st.subheader("💌 A Letter For You")

    placeholder = st.empty()
    displayed = ""
    for char in letter:
        displayed += char
        placeholder.markdown(f"```\n{displayed}\n```")
        time.sleep(0.035)

    # Download letter as PDF
    pdf_data_letter, fname_letter = text_to_pdf(
        "A Letter For You",
        letter,
        "Love_Letter_To_Jadesola.pdf",
        is_letter=True
    )
    st.download_button(
        label="📥 Download Letter as PDF",
        data=pdf_data_letter,
        file_name=fname_letter,
        mime="application/pdf"
    )

    st.divider()

    # ── Valentine Certificate ────────────────────────────────────────────────────
    st.subheader("📄 Valentine Certificate")

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=LETTER)
    width, height = LETTER

    # Background
    c.setFillColorRGB(1.0, 0.96, 0.98)
    c.rect(0, 0, width, height, fill=1)

    # Title
    c.setFillColorRGB(0.8, 0.1, 0.3)
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
    

    # Border
    c.setStrokeColorRGB(0.9, 0.4, 0.6)
    c.setLineWidth(8)
    margin = 0.6 * inch
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin)

    c.showPage()
    c.save()

    pdf_bytes = buffer.getvalue()
    buffer.close()

    st.download_button(
        label="📄 Download Official Valentine Certificate (PDF)",
        data=pdf_bytes,
        file_name="Valentine_Certificate_Jadesola.pdf",
        mime="application/pdf"
    )

    st.caption("ℹ️ Open in any PDF viewer to see your beautiful certificate!")
