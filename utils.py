import json
import hashlib
import os

POSTED_FILE = "posted_articles.json"

def generate_slug(text):
    return text.lower().replace(" ", "-")

def generate_article_id(title, link):
    return hashlib.md5(f"{title}-{link}".encode("utf-8")).hexdigest()

def is_article_posted(article_id):
    if not os.path.exists(POSTED_FILE):
        return False
    with open(POSTED_FILE, "r") as f:
        posted = json.load(f)
    return article_id in posted

def mark_article_as_posted(article_id):
    if not os.path.exists(POSTED_FILE):
        posted = []
    else:
        with open(POSTED_FILE, "r") as f:
            posted = json.load(f)
    posted.append(article_id)
    with open(POSTED_FILE, "w") as f:
        json.dump(posted, f)
