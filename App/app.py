# importing Libraries
import streamlit as st
from textblob import TextBlob

# Function to perform Sentiment Analysis

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return sentiment, polarity

# Streamlit User Interface
st.title("FeelFlare - Sentiment Analysis App")

# User Input

user_text = st.text_input("Enter a sentence: ")
