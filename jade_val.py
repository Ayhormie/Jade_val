import streamlit as st
import random
import time

# Initialize session state
if "predicted" not in st.session_state:
    st.session_state.predicted = False

if "accepted" not in st.session_state:
    st.session_state.accepted = False


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

st.slider("Affection Level", 0, 100, 97)
st.slider("Laughs at my jokes (%)", 0, 100, 99)
st.slider("Trust Level", 0, 100, 100)
st.selectbox(
    "Overall Relationship Vibe",
    ["Immaculate ✨", "Perfect 💕", "Unmatched 🔥"]
)

st.divider()

# Run prediction
if st.button("Run Valentine Prediction 🚀"):
    with st.spinner("Training deep emotional neural network..."):
        time.sleep(2)

    st.session_state.predicted = True


# Show prediction results
if st.session_state.predicted:
    probability = round(random.uniform(0.97, 0.995), 3)

    st.success("🎉 MODEL OUTPUT")
    st.metric("Prediction", "YES 💖")
    st.metric("Confidence Score", f"{probability * 100}%")

    st.markdown(
        """
        ### 🧠 Model Explanation (SHAP-ish 😏)
        - High affection ➜ strong positive weight  
        - Laughter ➜ overfitting to happiness 😂  
        - Trust ➜ 100% reliable  
        - Vibes ➜ off the charts 🔥  

        **Conclusion:**  
        The model refuses to consider any other outcome.
        """
    )

    # Hidden message
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

    st.divider()

    st.markdown(
        """
        ## 💖 Final Question  
        **Jadesola, will you be my Valentine?**
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💘"):
            st.session_state.accepted = True

    with col2:
        st.button("NO 😅")


# Celebration ONLY after YES
if st.session_state.accepted:
    st.success("🥰 Valentine confirmed! Model accuracy = 100%")
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
