from config import RSS_FEEDS
from rss_parser import get_latest_articles
from text_generator import generate_article
from image_fetcher import fetch_featured_image
from wp_poster import post_to_wordpress
from utils import mark_article_as_posted

def main():
    print("🔄 Lade neue Artikel...")
    articles = get_latest_articles(RSS_FEEDS)

    for article in articles:
        print(f"📤 Verarbeite: {article['title']}")
        
        # Keywords grob aus Titel (ersetzbar durch NLP später)
        keywords = article["title"].lower().split()[:5]

        # SEO-gerechter Artikel erzeugen
        content = generate_article(article["title"], article["summary"], keywords)

        # Bild suchen + Alt-Text
        image_url, alt_text = fetch_featured_image(article["title"])
        if image_url:
            post_to_wordpress(article["title"], content, keywords, image_url, alt_text)
            mark_article_as_posted(article["id"])
        else:
            print("⚠️ Kein passendes Bild gefunden. Artikel wird übersprungen.")
