import streamlit as st
import datetime

# Initialize session state
if 'start_date' not in st.session_state:
    st.session_state['start_date'] = datetime.date.today()
if 'streak' not in st.session_state:
    st.session_state['streak'] = 0
if 'leaderboard' not in st.session_state:
    st.session_state['leaderboard'] = {}

# Title and Header
st.title("🌱 Growth Mindset Challenge")
st.write("Believe in your ability to grow! Accept challenges and improve every day.")

# Inspirational Quote
st.subheader("💡 Inspirational Quote of the Day")
st.write("Believe you can and you're halfway there. - Theodore Roosevelt")

# Growth Challenge
st.subheader("🔥 Today's Growth Challenge")
st.write("Step out of your comfort zone and try something new.")

# Learning Input
st.subheader("📝 Your Growth Journey")
learning = st.text_area("What did you learn today?")

# Progress Slider
st.subheader("📊 Your Progress")
progress = st.slider("How much did you push yourself today?", 0, 100, 50)

# Streak Tracking
st.session_state['streak'] += 1
st.write(f"🔥 Streak: {st.session_state['streak']} days in a row!")

# Leaderboard Update
st.session_state['leaderboard']["You"] = st.session_state['streak']
sorted_leaderboard = sorted(st.session_state['leaderboard'].items(), key=lambda x: x[1], reverse=True)[:5]
st.subheader("🏆 Leaderboard")
for i, (user, streak) in enumerate(sorted_leaderboard, start=1):
    st.write(f"{i}. {user}: {streak} days")

# Personalized Challenges
st.subheader("💡 Suggest a Personalized Challenge")
new_challenge = st.text_input("Suggest a new challenge for others!")
if st.button("Submit Challenge"):
    st.write("✅ Challenge submitted!")

st.write("Developed with ❤️ to encourage a Growth Mindset.\nDeveloped by Nasir")
