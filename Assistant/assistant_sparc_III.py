from newspaper import Article
import random
import string
import numpy as np
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')
nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)
article= Article('https://simple.wikipedia.org/wiki/')
article.download()
article.parse()
article.nlp()
corpus=article.text
print(corpus)