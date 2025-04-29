import re

def summarize_article(text, max_sentences=3):
    """
    Einfache Zusammenfassung: Nimmt die ersten n Sätze des Artikels.
    Optional: Hier kannst du spaCy oder GPT einbauen.
    """
    sentences = re.split(r'(?<=[.!?]) +', text)
    summary = ' '.join(sentences[:max_sentences])
    return summary.strip()
