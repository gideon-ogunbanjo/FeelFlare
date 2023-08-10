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

# User Interactions

user_text = input("Enter a sentence: ")
sentiment, polarity = analyze_sentiment(user_text)

print("Sentiment:", sentiment)
print("Polarity Score:", polarity)

if sentiment == "positive":
    print("This is a positive statement!")
elif sentiment == "negative":
    print("This is a negative statement.")
else:
    print("The sentiment is neutral.")
