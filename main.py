from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

USAR_API = True  # True = Gemini | False = Ollama

# LOCAL (Ollama)
MODEL_LOCAL = "mistral"

# API (Gemini)
GEMINI_API_KEY = "Tua key aqui!"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

app = Flask(__name__)
CORS(app)

with open("TextoSite.txt", "r", encoding="utf-8") as f:
    CONTEXTO = f.read()

def gerar_resposta(pergunta):
    if USAR_API:
        return gerar_resposta_api(pergunta)
    else:
        return gerar_resposta_local(pergunta)

def gerar_resposta_api(pergunta):
    prompt = f"""
Responda em português do Brasil.

Você é um atendente de uma empresa de energia sustentável.

Responda de forma clara, direta e profissional.

IMPORTANTE:
- Responda em no máximo 2 frases
- Seja objetivo
- Não repita a pergunta
- Não repita instruções

Use apenas as informações abaixo:

{CONTEXTO}

Pergunta: {pergunta}

Resposta:
"""

    try:
        response = requests.post(
            GEMINI_URL,
            json={
                "contents": [
                    {
                        "parts": [
                            {"text": prompt}
                        ]
                    }
                ]
            },
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        print("ERRO DETALHADO:", e)
        return "Erro ao conectar com a API."

def gerar_resposta_local(pergunta):
    prompt = f"""
Responda em português do Brasil.

Você é um atendente de uma empresa de energia sustentável.

Responda de forma clara, direta e profissional.

IMPORTANTE:
- Responda em no máximo 2 frases
- Seja objetivo
- Não repita a pergunta
- Não repita instruções

Use apenas as informações abaixo:

{CONTEXTO}

Pergunta: {pergunta}

Resposta:
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL_LOCAL,
                "prompt": prompt,
                "options": {
                    "num_predict": 120,
                    "temperature": 0.2
                },
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "Erro ao gerar resposta.")

    except requests.exceptions.RequestException:
        return "Erro ao conectar com a IA local."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    if not data or "pergunta" not in data:
        return jsonify({"erro": "Pergunta não fornecida"}), 400

    pergunta = data.get("pergunta")

    resposta = gerar_resposta(pergunta)

    return jsonify({"resposta": resposta})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)