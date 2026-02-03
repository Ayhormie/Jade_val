import streamlit as st
import random
import time

st.set_page_config(
    page_title="Jadesola Valentine Model 💖",
    page_icon="💘",
    layout="centered"
)

st.title("💘 Jadesola Valentine Acceptance Model")
st.caption("Built by a Data Scientist who already knows the answer 😌")

st.write("""
Welcome, **Jadesola** 👋  
This predictive model was trained on:
- Emotional intelligence  
- Shared laughs 😂  
- Unmatched vibes ✨  
- Romantic consistency 💕  
""")

st.divider()

st.subheader("📊 Input Features")

affection = st.slider("Affection Level", 0, 100, 97)
laughter = st.slider("Laughs at my jokes (%)", 0, 100, 99)
trust = st.slider("Trust Level", 0, 100, 100)
vibes = st.selectbox(
    "Overall Relationship Vibe",
    ["Immaculate ✨", "Perfect 💕", "Unmatched 🔥"]
)

st.divider()

if st.button("Run Valentine Prediction 🚀"):
    with st.spinner("Training deep emotional neural network..."):
        time.sleep(2)

    probability = round(random.uniform(0.97, 0.995), 3)

    st.success("🎉 MODEL OUTPUT")
    st.metric("Prediction", "YES 💖")
    st.metric("Confidence Score", f"{probability * 100}%")

    st.balloons()

    st.markdown(
        """
        ### 🧠 Model Explanation (SHAP-ish 😏)
        - High affection level ➜ strong positive weight  
        - Constant laughter ➜ overfitting to happiness 😂  
        - Trust score ➜ 100% reliable  
        - Vibes ➜ off the charts 🔥  

        **Conclusion:**  
        The model refuses to consider any other outcome.
        """
    )

    st.divider()

    st.markdown(
        """
        ## 💌 Final Question
        **Jadesola, will you be my Valentine? 💖**
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💘"):
            st.success("🥰 Valentine confirmed! Model accuracy = 100%")
            st.markdown("💍 *Future version upgrade scheduled…*")

    with col2:
        if st.button("NO 😅"):
            st.error("⚠️ Model anomaly detected")
            st.info("🔁 Retraining model until YES is returned 😌")
