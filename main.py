from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

# MODEL = "tinyllama"
MODEL = "mistral"

app = Flask(__name__)
CORS(app)

with open("TextoSite.txt", "r", encoding="utf-8") as f:
    CONTEXTO = f.read()


def gerar_resposta(pergunta):
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
                "model": MODEL,
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
        return "Erro ao conectar com a IA."


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