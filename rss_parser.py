import feedparser
from utils import generate_article_id, is_article_posted

def get_latest_articles(rss_urls, max_count=5):
    articles = []
    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_count]:
            article_id = generate_article_id(entry.title, entry.link)
            if not is_article_posted(article_id):
                articles.append({
                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.summary,
                    "id": article_id
                })
    return articles
