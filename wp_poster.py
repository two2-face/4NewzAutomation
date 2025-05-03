import requests
from config import WP_URL, WP_USER, WP_PASSWORD
from utils import generate_slug

def post_to_wordpress(title, content, keywords, image_url, alt_text):
    # Upload Image
    image_response = requests.get(image_url)
    image_data = image_response.content
    media = requests.post(
        f"{WP_URL}/wp-json/wp/v2/media",
        headers={
            "Content-Disposition": f'attachment; filename="{generate_slug(title)}.jpg"',
        },
        auth=(WP_USER, WP_PASSWORD),
        files={"file": image_data},
        data={"alt_text": alt_text}
    )
    
    if media.status_code != 201:
        print("Bild konnte nicht hochgeladen werden:", media.text)
        return

    media_id = media.json()["id"]

    # Post Article
    post_data = {
        "title": title,
        "content": content,
        "status": "publish",
        "featured_media": media_id,
        "tags": [],  # Optional: ID-basierte Tags
    }

    post = requests.post(
        f"{WP_URL}/wp-json/wp/v2/posts",
        auth=(WP_USER, WP_PASSWORD),
        json=post_data
    )

    if post.status_code != 201:
        print("❌ Fehler beim Posten:", post.text)
    else:
        print(f"✅ Artikel veröffentlicht: {post.json()['link']}")
