import requests
from config import OPENROUTER_API_KEY

def generate_article(title, summary, keywords):
    prompt = f"""
You are a professional SEO content writer.

Write a long-form blog article of at least **2200 words**. 
The article should be structured with:

- A compelling **title** (use the original title as inspiration).
- A clear **meta description** (under 160 characters).
- A **H1 headline**, and **multiple H2 and H3** subheadings.
- Include relevant **SEO keywords** naturally in the text: {", ".join(keywords)}.
- Write in a friendly, engaging tone.
- Add a short **conclusion** with a call to action.
- Use markdown format (for easy HTML conversion).
- Avoid repeating phrases.

Topic: {title}

Summary: {summary}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistral/mixtral-8x7b",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.8,
            "max_tokens": 7000
        }
    )
    data = response.json()
    return data["choices"][0]["message"]["content"]
