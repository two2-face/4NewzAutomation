import requests
from config import PIXABAY_API_KEY

def fetch_featured_image(query):
    response = requests.get(
        "https://pixabay.com/api/",
        params={
            "key": config.PIXABAY_API_KEY,
            "q": query,
            "image_type": "photo",
            "safesearch": "true",
            "per_page": 3
        }
    )
    data = response.json()
    if data["hits"]:
        top_result = data["hits"][0]
        return top_result["largeImageURL"], top_result["tags"]
    return None, None
