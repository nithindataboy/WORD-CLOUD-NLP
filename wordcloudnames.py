# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 22:40:25 2024

@author: Appala nithin
"""

import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Downloading stopwords
nltk.download('stopwords')
# Input Text (Example Paragraph)
Names = """NITHIN SAHITH RAJUKUMAR RAJKUMAR SATHISH RAKESH MUKESH NIKHIL PRADEEP AKSHAY VISHNU SAIVARDHAN RAJU KRISHNAVAMSHI AKHIL AJAY VAMSHI MUTHYAMRAJU  """

# Remove stopwords from the text
stop_words = set(stopwords.words('english'))


# Generate the Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='rainbow').generate(Names)

# Display the Word Cloud
plt.figure(figsize=(12,6))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.title("SSC-2018-19", fontsize=20, color='darkblue')
plt.show()
