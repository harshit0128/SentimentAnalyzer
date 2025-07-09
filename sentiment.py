from textblob import TextBlob

text = input("Enter your sentence: ")
blob = TextBlob(text)
polarity = blob.sentiment.polarity

if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😟")
else:
    print("Sentiment: Neutral 😐")
