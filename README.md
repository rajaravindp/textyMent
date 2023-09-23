# **textyMent**
**Sentiment Analysis using textBlob** 

TextBlob is a Python library for processing textual data. It provides a simple API for common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

**Key Concept** 
- In the context of TextBlob's sentiment analysis, "subjectivity" refers to a measure of how subjective or objective the text is. Subjectivity quantifies the extent to which the text expresses personal opinions, emotions, or feelings rather than objective information or facts. A subjectivity score of 0.0 typically indicates that the text is highly objective, meaning it contains primarily factual information without much personal opinion or emotional content. On the other hand, a higher subjectivity score would suggest that the text contains more subjective content, such as personal feelings, opinions, or expressions. Subjectivity  score typically ranges from 0.0 to 1.0, where:
  - 0.0: Represents high objectivity, meaning the text is very objective and contains mostly factual information without personal opinions or emotions.
  - 1.0: Represents high subjectivity, indicating that the text is very subjective, emotional, or opinionated.
Values between 0.0 and 1.0 represent varying degrees of subjectivity. A score closer to 0.0 suggests that the text is more objective, while a score closer to 1.0 suggests that the text is more subjective and contains personal opinions or emotions.

In the context of TextBlob's sentiment analysis, the "polarity" score is a numerical value that represents the overall sentiment or emotional tone of a piece of text. It measures whether the text is primarily positive, negative, or neutral.
Polarity score typically ranges from -1.0 to 1.0, where:
- 1.0: Represents a highly negative sentiment, indicating strong negativity in the text.
- 0.0: Represents a neutral sentiment, indicating that the text has neither a positive nor a negative sentiment.
- 1.0: Represents a highly positive sentiment, indicating strong positivity in the text.
Values between -1.0 and 0.0 represent varying degrees of negativity, with values closer to -1.0 indicating stronger negative sentiments. Values between 0.0 and 1.0 represent varying degrees of positivity, with values closer to 1.0 indicating stronger positive sentiments.

This code example shows how to use TextBlob to perform sentiment analysis on a sentence. It first prompts the user for input, then creates a TextBlob object from the input text. Next, it uses the TextBlob object's sentiment property to calculate the polarity and subjectivity of the text. Finally, it prints the sentiment to the console and categorizes it as positive, negative, or neutral.

Here is an example of how to use the code:

