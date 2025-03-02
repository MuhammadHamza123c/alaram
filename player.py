import streamlit as st
import time
import datetime
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Streamlit UI
st.title("⏰ Automatic Alarm System with Streamlit 🎵")
st.write("Enter a time (HH:MM format) and the alarm will automatically play when it matches system time.")

# User input for alarm time
alarm_time = st.text_input("Write down time here (24-hour format, e.g., 14:30):")

# Function to check time continuously
def check_alarm():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            st.warning("🔔 Alarm ringing! Playing audio...")
            pygame.mixer.music.load("D:\\Code\\Main Hoon na.mp3")  # Change to your file path
            pygame.mixer.music.play()
            break
        time.sleep(10)  # Check every 10 seconds

# Run the function automatically when the user inputs a time
if alarm_time:
    st.write(f"⏳ Alarm set for {alarm_time}. Waiting for the time...")
    check_alarm()  # Starts checking the time automatically
