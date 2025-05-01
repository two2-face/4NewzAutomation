import requests
import config
from requests.auth import HTTPBasicAuth

def create_or_get_tag_id(tag_name):
    """
    Erstellt oder holt eine Tag-ID anhand des Namens.
    """
    url = f"{config.WORDPRESS_URL}/wp-json/wp/v2/tags"
    auth = HTTPBasicAuth(config.WP_USERNAME, config.WP_APP_PASSWORD)

    # Suche Tag
    params = {"search": tag_name}
    res = requests.get(url, params=params, auth=auth)

    if res.status_code == 200 and res.json():
        return res.json()[0]["id"]

    # Falls nicht vorhanden, erstelle neuen Tag
    res = requests.post(url, json={"name": tag_name}, auth=auth)
    if res.status_code == 201:
        return res.json()["id"]
    else:
        print(f"⚠️ Tag konnte nicht erstellt werden: {tag_name}")
        return None

def post_to_wordpress(post_data):
    endpoint = f"{config.WORDPRESS_URL}/wp-json/wp/v2/posts"
    headers = {"Content-Type": "application/json"}
    auth = HTTPBasicAuth(config.WP_USERNAME, config.WP_APP_PASSWORD)

    # Tags verarbeiten (Namen → IDs)
    tag_ids = []
    for tag in post_data["tags"]:
        tag_id = create_or_get_tag_id(tag)
        if tag_id:
            tag_ids.append(tag_id)

    data = {
        "title": post_data["title"],
        "content": post_data["content"],
        "status": "publish",
        "slug": post_data["slug"],
        "tags": tag_ids
    }

    response = requests.post(endpoint, json=data, headers=headers, auth=auth)
    return response
