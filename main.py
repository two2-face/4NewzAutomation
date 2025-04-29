from rss_parser import get_latest_articles
from text_generator import summarize_article
from image_fetcher import get_image_url
from wp_poster import post_to_wordpress
from utils import generate_slug, extract_keywords
import config

def main():
    print("🔄 Lade neue Artikel...")
    articles = get_latest_articles(config.RSS_FEEDS)

    for article in articles:
        title = article['title']
        link = article['link']
        summary = summarize_article(article['summary'])
        slug = generate_slug(title)
        keywords = extract_keywords(summary)
        tags = ', '.join(keywords)
        image_url, alt_text = get_image_url(title)

        post_data = {
            "title": title,
            "content": f"<img src='{image_url}' alt='{alt_text}'/><p>{summary}</p><p>Quelle: <a href='{link}'>{link}</a></p>",
            "slug": slug,
            "tags": keywords,
            "image_alt": alt_text,
        }

        print(f"📤 Veröffentliche: {title}")
        response = post_to_wordpress(post_data)

        if response.status_code == 201:
            print(f"✅ Erfolgreich veröffentlicht: {title}")
        else:
            print(f"❌ Fehler: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()
