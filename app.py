import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import datetime


# Download the VADER sentiment analysis lexicon (do this once)
nltk.download('vader_lexicon')

# Create a function to transcribe audio to text


# Create a function to analyze the sentiment of a text using NLTK
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    
    if sentiment_scores['compound'] >= 0.05:
        return "positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

# Create a function to track mood trends over time
def track_mood_trends(mood_entries):
    mood_trends = {}

    for entry in mood_entries:
        date = entry[0]
        mood = entry[1]

        if date not in mood_trends:
            mood_trends[date] = []

        mood_trends[date].append(mood)

    average_mood_trends = {}

    for day in mood_trends:
        average_mood = sum(mood_trends[day]) / len(mood_trends[day])
        average_mood_trends[day] = average_mood

    return average_mood_trends

# Create a Streamlit app
st.title("Mood Tracker")

# Display a text input and an audio uploader
text_input = st.text_input("Text input")


# If the user entered text or transcribed audio, analyze the sentiment
if text_input or audio_text:
    mood_sentiment = analyze_sentiment(text_input or audio_text)
else:
    mood_sentiment = None

# Add the user's input to the database
mood_entries = []

if mood_sentiment:
    mood_entries.append((datetime.datetime.now(), mood_sentiment))

# Track mood trends over time
average_mood_trends = track_mood_trends(mood_entries)

# Display the user's mood trends
st.line_chart(average_mood_trends)
