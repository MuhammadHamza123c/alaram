import streamlit as st
import time
import datetime

# Streamlit UI
st.title("⏰ Automatic Alarm System with Streamlit 🎵")
st.write("Enter a time (HH:MM format) and the alarm will automatically play when it matches system time.")

# User input for alarm time
alarm_time = st.text_input("Write down time here (24-hour format, e.g., 14:30):")

# Path to the audio file
audio_file = "Main Hoon na.mp3"  # Upload this file in the same directory

# Function to check time continuously
def check_alarm():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            st.warning("🔔 Alarm ringing! Playing audio...")
            
            # Display hidden audio player
            st.markdown(
                f"""
                <audio id="alarmAudio" src="{audio_file}" autoplay></audio>
                <script>
                    document.getElementById("alarmAudio").play();
                </script>
                """,
                unsafe_allow_html=True,
            )
            break
        time.sleep(10)  # Check every 10 seconds

# Automatically check alarm when user inputs time
if alarm_time:
    st.write(f"⏳ Alarm set for {alarm_time}. Waiting for the time...")
    check_alarm()  # Starts checking the time automatically
