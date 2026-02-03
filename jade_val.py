import streamlit as st
import random
import time
import base64

# ---------------- SESSION STATE ----------------
if "predicted" not in st.session_state:
    st.session_state.predicted = False
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "letter_shown" not in st.session_state:
    st.session_state.letter_shown = False

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

    with col2:
        st.button("NO 😅")


# ---------------- LOVE LETTER ANIMATION ----------------
if st.session_state.letter_shown:
    st.success("🥰 Valentine confirmed!")
    st.balloons()
    st.snow()

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

    # ---------------- PDF CERTIFICATE ----------------
    st.subheader("📄 Valentine Certificate")

    certificate_text = f"""
    💖 Valentine Certificate 💖

    This certifies that

    JADESOLA

    has officially accepted to be my Valentine 💘

    Issued with ❤️ by Ayomide (Data Scientist Edition)
    """

    # Convert text to PDF-like download (as txt file for simplicity)
    certificate_bytes = certificate_text.encode("utf-8")
    b64 = base64.b64encode(certificate_bytes).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="Valentine_Certificate_Jadesola.txt">📄 Download Valentine Certificate</a>'
    st.markdown(href, unsafe_allow_html=True)
