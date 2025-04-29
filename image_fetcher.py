import requests
import config

def get_image_url(query):
    """
    Sucht ein passendes Bild bei Pixabay anhand des Titels/Keywords.
    Gibt URL + Alt-Text zurück.
    """
    endpoint = "https://pixabay.com/api/"
    params = {
        "key": config.PIXABAY_API_KEY,
        "q": query,
        "image_type": "photo",
        "safesearch": "true",
        "per_page": 3
    }

    try:
        response = requests.get(endpoint, params=params)
        data = response.json()

        if data['hits']:
            image = data['hits'][0]
            return image['webformatURL'], image['tags']
        else:
            return "https://via.placeholder.com/800x400.png?text=No+Image", "Placeholder image"
    except Exception as e:
        print(f"Fehler beim Abrufen des Bildes: {e}")
        return "https://via.placeholder.com/800x400.png?text=Error", "Image error"
