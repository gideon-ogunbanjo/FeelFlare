import streamlit as st
from textblob import TextBlob
from autocorrect import Speller
import pyttsx3

# Page configuration
st.set_page_config(
    page_title="FeelFlare",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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

# Autocorrect function
def autocorrect_text(text):
    spell = Speller(lang='en')
    corrected_text = spell(text)
    return corrected_text

# # Function to speak the text
# def speak_text(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# Streamlit User Interface
st.title("FeelFlare - Sentiment Analysis App")
st.write("FeelFlare is a Sentiment Analysis model that determines whether a given text has a positive, negative, or neutral sentiment using natural language processing techniques.")

# User Input
user_text = st.text_input("Share how you feel: ")

# Autocorrect option
autocorrect_option = st.checkbox("Enable Autocorrect")

if autocorrect_option and user_text:
    user_text = autocorrect_text(user_text)

# Button to analyze
if st.button("Analyze"):
    if user_text:
        # Performs sentiment analysis on user's input
        sentiment, polarity = analyze_sentiment(user_text)

        # Displays sentiment and polarity score
        st.write("Sentiment:", sentiment)
        st.write("Polarity Score:", polarity)

        if sentiment == "positive":
            st.write("This is a positive statement!")
        elif sentiment == "negative":
            st.write("This is a negative statement.")
        else:
            st.write("The sentiment is neutral.")
        
        # # Speak the results
        # speak_text("The sentiment is " + sentiment)

link = 'Created by [Gideon Ogunbanjo](https://gideonogunbanjo.netlify.app)'
st.markdown(link, unsafe_allow_html=True)
