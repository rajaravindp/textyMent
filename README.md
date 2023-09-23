# **textyMent**
**Sentiment Analysis using textBlob** 

TextBlob is a Python library for processing textual data. It provides a simple API for common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

**Key Concept** 
- In the context of TextBlob's sentiment analysis, "subjectivity" refers to a measure of how subjective or objective the text is. Subjectivity quantifies the extent to which the text expresses personal opinions, emotions, or feelings rather than objective information or facts. A subjectivity score of 0.0 typically indicates that the text is highly objective, meaning it contains primarily factual information without much personal opinion or emotional content. On the other hand, a higher subjectivity score would suggest that the text contains more subjective content, such as personal feelings, opinions, or expressions. Subjectivity  score typically ranges from 0.0 to 1.0, where:
  - 0.0: Represents high objectivity, meaning the text is very objective and contains mostly factual information without personal opinions or emotions.
  - 1.0: Represents high subjectivity, indicating that the text is very subjective, emotional, or opinionated.
Values between 0.0 and 1.0 represent varying degrees of subjectivity. A score closer to 0.0 suggests that the text is more objective, while a score closer to 1.0 suggests that the text is more subjective and contains personal opinions or emotions.

- In the context of TextBlob's sentiment analysis, the "polarity" score is a numerical value that represents the overall sentiment or emotional tone of a piece of text. It measures whether the text is primarily positive, negative, or neutral.
Polarity score typically ranges from -1.0 to 1.0, where:
  - 1.0: Represents a highly negative sentiment, indicating strong negativity in the text.
  - 0.0: Represents a neutral sentiment, indicating that the text has neither a positive nor a negative sentiment.
  - 1.0: Represents a highly positive sentiment, indicating strong positivity in the text.
Values between -1.0 and 0.0 represent varying degrees of negativity, with values closer to -1.0 indicating stronger negative sentiments. Values between 0.0 and 1.0 represent varying degrees of positivity, with values closer to 1.0 indicating stronger positive sentiments.

This code example shows how to use TextBlob to perform sentiment analysis on a sentence. It first prompts the user for input, then creates a TextBlob object from the input text. Next, it uses the TextBlob object's sentiment property to calculate the polarity and subjectivity of the text. Finally, it prints the sentiment to the console and categorizes it as positive, negative, or neutral.
Here is an example of how to use the code: <br>
- Prompt the user for input <br>
![image](https://github.com/rajaravindp/textyMent/assets/118573661/869e378d-03fa-4f85-bb7f-8fc12935dfd4) | ![image](https://github.com/rajaravindp/textyMent/assets/118573661/68ba1e1f-cd8a-4a8b-9930-fdef05f5e88d) <br>

- Derive sentiment metrics <br>
![image](https://github.com/rajaravindp/textyMent/assets/118573661/0a81545c-6e38-43e0-b317-953aef62f388) | ![image](https://github.com/rajaravindp/textyMent/assets/118573661/9837a607-24d5-4429-a4d9-938b3804bac0) <br>

- Categorize sentiment as +ve, -ve or neutral based on polarity <br>
![image](https://github.com/rajaravindp/textyMent/assets/118573661/589418c0-f13a-4904-960a-0e11bb0e25b3) | ![image](https://github.com/rajaravindp/textyMent/assets/118573661/07751490-320f-4f97-a8d6-e3e87c40832f) <br>

- Categorize sentiment as objective or subjective based on subjectivity <br>
![image](https://github.com/rajaravindp/textyMent/assets/118573661/45c4c363-cfee-4284-b650-c8290822c9da) | ![image](https://github.com/rajaravindp/textyMent/assets/118573661/a12ab28f-8ed5-4529-a330-179e211d67d7) <br>

The sets of images displayed above offer a striking visual representation of text sentiment analysis results. The image on the left-hand side, with its predominantly negative polarity and maximum objectivity, appears to mirror the tone of text that is primarily factual. On the other hand, the image on the right-hand side tells a completely different story. It exudes a highly positive polarity and maximum subjectivity, suggesting that the associated text is emotionally charged, opinionated, and expressive. <br>

Please keep in mind that this is a naive implementatioon. I have undertaken this project with the intent to kickstart my NLP journey. This project has many pitfallas. Beware!
For example: <br>
- Prompting user for input <br>
![image](https://github.com/rajaravindp/textyMent/assets/118573661/e13c57bb-cd4a-477b-b1c6-6d8c1abac2a5) <br>
- Even though the sentence conveys happiness, the polarity is classified as neutral <br><div style="display: flex;">
Derive sentiment metrics <br>
![image](https://github.com/rajaravindp/textyMent/assets/118573661/f1f4ee90-536c-4905-8b43-dbc52838bd4c) {align="left"} <br>
Categorize sentiment as +ve, -ve or neutral based on polarity <br>
![image](https://github.com/rajaravindp/textyMent/assets/118573661/e46b99bb-cdc0-4f69-b958-f358db49313f) {align="left"} <br>


