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

    # Hidden message (revealed after prediction)
    with st.expander("🔐 View Model Insights (Restricted)"):
        st.markdown(
            """
            💌 **Hidden Insight Detected**

            Jadesola, beyond the data, models, and jokes…

            You make things feel lighter, happier, and more meaningful.
            This model was just an excuse to ask you properly 😌❤️

            **No algorithm beats how I feel about you.**
            """
        )

    st.markdown(
        """
        ## 💖 Final Question
        **Jadesola, will you be my Valentine?**
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💘"):
            st.success("🥰 Valentine confirmed! Model accuracy = 100%")

            # Celebration animations ONLY on YES
            st.balloons()
            st.snow()

            st.markdown(
                """
                ### 🎉 Model Update
                - Status: **SUCCESS**
                - Valentine secured 💖
                - Next phase: *Dinner & memories* 🍽️✨

                💍 *Future version upgrade scheduled…*
                """
            )

    with col2:
        if st.button("NO 😅"):
            st.error("⚠️ Model anomaly detected")
            st.info("🔁 Retraining model until YES is returned 😌")
