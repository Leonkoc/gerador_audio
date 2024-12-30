from flask import Flask, request, send_file, render_template
from urllib.parse import quote  # Remove a importação do werkzeug.urls
import edge_tts  # type: ignore
import asyncio

app = Flask(__name__)

# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para gerar o áudio
@app.route("/generate-audio", methods=["POST"])
def generate_audio():
    text = request.form.get("text")
    if not text:
        return "Erro: Nenhum texto fornecido.", 400

    # Gerar o nome do arquivo com a primeira palavra
    primeira_palavra = text.split()[0] if text.strip() else "audio"
    audio_file = f"{primeira_palavra}.mp3"

    # Função assíncrona para gerar o áudio
    async def create_audio():
        tts = edge_tts.Communicate(text, "pt-BR-AntonioNeural")
        await tts.save(audio_file)

    asyncio.run(create_audio())

    # Retornar o arquivo como download
    return send_file(audio_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
