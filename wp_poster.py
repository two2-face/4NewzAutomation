import requests
import config
from requests.auth import HTTPBasicAuth

def create_or_get_tag_id(tag_name):
    """
    Holt die ID eines bestehenden Tags oder erstellt einen neuen.
    """
    url = f"{config.WORDPRESS_URL}/wp-json/wp/v2/tags"
    auth = HTTPBasicAuth(config.WP_USERNAME, config.WP_APP_PASSWORD)

    # Suche nach Tag
    response = requests.get(url, params={"search": tag_name}, auth=auth)
    if response.status_code == 200 and response.json():
        return response.json()[0]["id"]

    # Tag existiert nicht – erstelle
    response = requests.post(url, json={"name": tag_name}, auth=auth)
    if response.status_code == 201:
        return response.json()["id"]

    print(f"⚠️ Fehler beim Erstellen des Tags '{tag_name}': {response.text}")
    return None

def post_to_wordpress(post_data):
    """
    Veröffentlicht einen Beitrag auf WordPress mit Tag-IDs.
    """
    endpoint = f"{config.WORDPRESS_URL}/wp-json/wp/v2/posts"
    headers = {"Content-Type": "application/json"}
    auth = HTTPBasicAuth(config.WP_USERNAME, config.WP_APP_PASSWORD)

    # Wandle Tags in IDs um
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
