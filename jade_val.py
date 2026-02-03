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

    # Soft pinkish background
    c.setFillColor(HexColor('#FFF0F5'))  # Lavender blush
    c.rect(0, 0, width, height, fill=1)

    # ── Heart border image (transparent PNG overlay) ───────────────────────────────
    heart_border_url = "https://www.citypng.com/public/uploads/preview/-11594697082r1j2r0w0v0.png"
    # Download not needed — ReportLab can fetch remote images (works on Streamlit Cloud)
    try:
        c.drawImage(heart_border_url, x=0.5*inch, y=0.5*inch, width=width-1*inch, height=height-1*inch,
                    mask='auto', preserveAspectRatio=True)  # mask='auto' for transparency
    except:
        pass  # If URL fails, skip silently (fallback to no border)

    # Bigger margins
    left_margin = 1.5 * inch
    top_margin = height - 2.0 * inch
    line_height = 18  # More breathing room

    # Title with hearts
    c.setFillColor(HexColor('#C71585'))  # Deep pink
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width / 2, top_margin, f"💖 {title} 💖")

    # Content
    c.setFillColor(HexColor('#333333'))
    c.setFont("Helvetica", 13) if is_letter else c.setFont("Helvetica-Oblique", 13)

    y = top_margin - 1.2 * inch
    lines = content.split('\n')

    for line in lines:
        if y < 1.2 * inch:
            c.showPage()
            y = height - 1.5 * inch
            # Re-apply light bg & border if new page (optional)
            c.setFillColor(HexColor('#FFF0F5'))
            c.rect(0, 0, width, height, fill=1)
            try:
                c.drawImage(heart_border_url, 0.5*inch, 0.5*inch, width-1*inch, height-1*inch, mask='auto')
            except:
                pass

        # Simple word-wrap for long lines
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
            y -= line_height + 4  # extra space between paragraphs

        y -= line_height // 2  # paragraph spacing

    # Signature / closing heart
    if is_letter:
        c.setFont("Helvetica-Oblique", 14)
        c.setFillColor(HexColor('#FF69B4'))
        c.drawString(left_margin, y - 40, "Consistently yours,")
        c.drawString(left_margin + 1.2*inch, y - 60, "Ayomide 💖")

    c.save()
    buffer.seek(0)
    return buffer.getvalue(), filename


# ---------------- SESSION STATE ----------------
if "predicted" not in st.session_state:
    st.session_state.predicted = False
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "letter_shown" not in st.session_state:
    st.session_state.letter_shown = False
if "music_playing" not in st.session_state:
    st.session_state.music_playing = False

# ---------------- PAGE CONFIG & MAIN APP (unchanged except PDF calls) ----------------
st.set_page_config(page_title="Jadesola Valentine Model 💖", page_icon="💘", layout="centered")

st.title("💘 Jadesola Valentine Acceptance Model")
st.caption("Built by a Data Scientist who already knows the answer 😌")
st.write("Welcome, **Jadesola** 👋  \nThis model was trained on laughter, trust, vibes, and a ridiculous amount of affection 💕")
st.divider()

# Input features (unchanged)
st.subheader("📊 Input Features")
st.slider("Affection Level", 0, 100, 97)
st.slider("Laughs at my jokes (%)", 0, 100, 99)
st.slider("Trust Level", 0, 100, 100)
st.selectbox("Overall Relationship Vibe", ["Immaculate ✨", "Perfect 💕", "Unmatched 🔥"])
st.divider()

# Run model (unchanged)
if st.button("Run Valentine Prediction 🚀"):
    with st.spinner("Training emotional neural network..."):
        time.sleep(2)
    st.session_state.predicted = True

if st.session_state.predicted:
    # ... (model output, private message section unchanged except PDF call below)

    # PRIVATE MESSAGE PDF download (inside if secret.lower() == "jadesola")
    # ...
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

    # ... (final question unchanged)

# Letter shown section
if st.session_state.letter_shown:
    # ... (success, balloons, music unchanged)

    # Letter PDF
    pdf_data_let, fname_let = text_to_pdf(
        "A Letter For You",
        letter,
        "Love_Letter_To_Jadesola.pdf",
        is_letter=True
    )
    st.download_button(
        label="📥 Download Letter as PDF",
        data=pdf_data_let,
        file_name=fname_let,
        mime="application/pdf"
    )

    # Certificate PDF (you can apply similar prettifying: background, hearts, etc.)
    # For now keeping original but with larger margins if you want — or copy style from text_to_pdf

    # ... rest of certificate code (optionally refactor it to use similar styling)
