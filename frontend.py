"""
frontend.py
- Contains the basic frontend of the application, ft. Streamlit, which calls the main functions
"""
from consumer import process_kafka_messages
import streamlit as st

st.title("Discord channel Moderation App")
st.write("This Streamlit app processes Kafka messages.")

if st.button("Start Processing Kafka Messages"):
    st.write("Processing Kafka Messages...")
    process_kafka_messages()