import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

def generate_slug(title):
    """
    Erzeugt einen URL-freundlichen Slug aus dem Titel.
    """
    slug = re.sub(r'\W+', '-', title.lower())
    return slug

def extract_keywords(text):
    """
    Einfacher Keyword-Extractor ohne NLTK-Tokenizer-Bug.
    """
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    return list(set(keywords))[:10]  # max 10 Keywords
