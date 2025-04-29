import feedparser

def get_latest_articles(feed_urls, limit_per_feed=2):
    articles = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit_per_feed]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary if 'summary' in entry else entry.description
            })
    return articles
