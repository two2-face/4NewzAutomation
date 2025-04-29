import requests
import config
from requests.auth import HTTPBasicAuth

def post_to_wordpress(post_data):
    """
    Sendet den Beitrag an die WordPress REST API
    """
    endpoint = f"{config.WORDPRESS_URL}/wp-json/wp/v2/posts"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    auth = HTTPBasicAuth(config.WP_USERNAME, config.WP_APP_PASSWORD)
    
    data = {
        "title": post_data["title"],
        "content": post_data["content"],
        "status": "publish",  # Der Beitrag wird sofort veröffentlicht
        "slug": post_data["slug"],
        "tags": post_data["tags"],
        "featured_media": post_data.get("featured_media", None),
    }

    response = requests.post(endpoint, json=data, headers=headers, auth=auth)
    
    return response
