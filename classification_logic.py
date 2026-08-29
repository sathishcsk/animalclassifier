import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:0.5b"


def classify_creature(name):

    prompt = f"""
You are an animal classification system.

Classify the following creature into exactly one of these categories:

Animal
Bird
Sea Creature
Unknown

Creature: {name}

Rules:
- Mammals and land animals -> Animal
- Birds -> Bird
- Creatures primarily living in the sea/ocean -> Sea Creature
- If the input is not a creature -> Unknown

Return ONLY the category name.
Do not explain your answer.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    response.raise_for_status()

    result = response.json()["response"].strip()

    allowed_categories = [
        "Animal",
        "Bird",
        "Sea Creature",
        "Unknown"
    ]

    for category in allowed_categories:
        if result.lower() == category.lower():
            return category

    return "Unknown"