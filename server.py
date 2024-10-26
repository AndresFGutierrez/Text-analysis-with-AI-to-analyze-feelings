"""
Este modulo proporciona la logica para el servidor de deteccion de emociones.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint para analizar la emoción del texto ingresado.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if "error" in response:
        return response["error"]

    result_text = (
        f"Anger: {response.get('anger', 0)}, "
        f"Disgust: {response.get('disgust', 0)}, "
        f"Fear: {response.get('fear', 0)}, "
        f"Joy: {response.get('joy', 0)}, "
        f"Sadness: {response.get('sadness', 0)}.<br>"
        f"Dominant emotion: {response['dominant_emotion']}."
    )

    return result_text


@app.route("/")
def index():
    """
    Renderiza la página de inicio.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
