from textblob import TextBlob
import matplotlib.pyplot as plt

positive = 0
negative = 0
neutral = 0

print("Enter sentences to analyze (type 'exit' to finish):")

while True:
    text = input("> ")
    if text.lower() == 'exit':
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        print("Positive 😊")
        positive += 1
    elif polarity < 0:
        print("Negative 😟")
        negative += 1
    else:
        print("Neutral 😐")
        neutral += 1

# 📊 Visualize the results
labels = ['Positive', 'Negative', 'Neutral']
values = [positive, negative, neutral]

plt.bar(labels, values, color=['green', 'red', 'gray'])
plt.title('Sentiment Analysis Report')
plt.ylabel('Number of Sentences')
plt.xlabel('Sentiment')
plt.show()

