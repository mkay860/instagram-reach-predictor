import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="ReachIns | The Super Model", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .title-text { font-size: 40px; font-weight: 800; text-align: center; color: #4B0082; }
    .metric-card { background-color: #f0f2f6; padding: 20px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

try:
    model = pickle.load(open('model.pkl', 'rb'))
except:
    st.error("⚠️ Model not found. Run 'train_model.py' first!")
    st.stop()

#st.markdown('<p class="title-text">ReachIns 🔮</p>', unsafe_allow_html=True)
st.header("ReachIns 🔮")
st.write("Predict Reach with **Extreme Accuracy** using Follower & Engagement data.")

st.divider()

# INPUTS
st.subheader("1️⃣ Account Stats")
c1, c2 = st.columns(2)
followers = c1.number_input("Followers", value=1000)
likes = c2.number_input("Target Likes", value=50)

st.subheader("2️⃣ Post Details")
c3, c4, c5 = st.columns(3)
comments = c3.number_input("Target Comments", value=5)
hour = c4.slider("Post Hour (24h)", 0, 23, 12)
day = c5.selectbox("Day of Week", options=[1,2,3,4,5,6,7], format_func=lambda x: f"Day {x}")

# PREDICT
if st.button("Predict Reach 🚀"):
    
    features = np.array([[followers, likes, comments, hour, day]])
    prediction = model.predict(features)[0]
    
    st.divider()
    st.metric("Predicted Reach", f"{int(prediction):,}")
    
    
    engagement_rate = ((likes + comments) / followers) * 100
    st.info(f"💡 This assumes an engagement rate of **{engagement_rate:.2f}%**")