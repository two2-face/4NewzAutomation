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
    Extrahiert Schlüsselwörter aus einem Text (z. B. durch Entfernen von Stopwörtern).
    """
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    keywords = [word for word in words if word.isalnum() and word not in stop_words]
    return keywords
