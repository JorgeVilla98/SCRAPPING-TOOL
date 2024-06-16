import nltk
import sys
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')  # Download the VADER lexicon for sentiment analysis

filename = sys.argv[1]

comments_df = pd.read_csv(filename, sep='|')

#funcion para analizar el sentimiento clasificandolo en 3 clases: positivo, negativo y neutro
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral' #entre -0.05 y 0.05

#creamos una nueva columna con el sentimiento
comments_df['Sentiment'] = comments_df['Comment'].apply(analyze_sentiment)

comments_df.to_csv(filename, sep='|', index=False)

print(f'Sentiment analyzed')
