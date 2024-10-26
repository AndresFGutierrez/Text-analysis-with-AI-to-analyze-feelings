import requests


def emotion_detector(text_to_analyse):
    """
    Detecta emociones usando la API de Hugging Face.
    """
    url = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
    headers = {
        "Authorization": "Bearer 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"
    }  # Token de Hugging Face
    payload = {"inputs": text_to_analyse}

    # Realiza la solicitud a la API
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        return {
            "error": "No se pudo analizar el texto. Verifica el servicio o tu token."
        }

    emotions = response.json()[0]
    dominant_emotion = max(emotions, key=lambda x: x["score"])

    # Devolver emociones con la dominante
    return {emotion["label"]: emotion["score"] for emotion in emotions} | {
        "dominant_emotion": dominant_emotion["label"]
    }
