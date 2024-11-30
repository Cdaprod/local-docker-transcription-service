from flask import Flask, request, jsonify
import whisper
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

app = Flask(__name__)

# Load Whisper model
model = whisper.load_model("base")

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@app.route('/transcribe', methods=['POST'])
def transcribe():
    """
    Transcribes an audio file.
    """
    try:
        audio_file = request.files['audio']
        result = model.transcribe(audio_file)
        return jsonify({"transcript": result['text']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/summarize', methods=['POST'])
def summarize():
    """
    Summarizes a transcript.
    """
    try:
        transcript = request.json.get('transcript')
        if not transcript:
            return jsonify({"error": "No transcript provided"}), 400

        prompt = PromptTemplate(template="Summarize this transcript: {transcript}")
        llm = OpenAI(api_key=OPENAI_API_KEY)
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        summary = llm_chain.run(transcript=transcript)
        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)