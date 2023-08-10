from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    # Gets sentiment polarity score (-1 to 1)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return sentiment, polarity
