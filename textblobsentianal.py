# -*- coding: utf-8 -*-
"""textBlobSentiAnal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fUPtD2fVZjGo5yPvQrR6DoSWo7MrysK6
"""

# Install textblob
!pip install textblob

# Loading textblob module
from textblob import TextBlob

# Prompt user for input
sentence = input("Enter text: ")

# Create obj
senti = TextBlob(sentence)
# Sentiment analysis
print(senti.sentiment)

"""Polarity: Ranges from (-1, +1) -1 indicating sadness & +1 indicating happiness. <br>
subjectivity: Represents the degree to which a statement or text is opinion-based rather than factual, with a value of 1.0 indicating complete subjectivity.

"""

# Categorization of sentiment polarity
if senti.polarity > 0:
  print("Sentiment positive")
elif senti.polarity == 0:
  print("Sentiment neutral")
else:
  print("Sentiment negative")