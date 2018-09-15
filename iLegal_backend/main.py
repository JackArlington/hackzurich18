from flask import Flask
from flask import request, jsonify
from preprocess import extract_nouns
app = Flask(__name__)

@app.route("/")
def hello():
    return "iLegal backend V0.2.1"

@app.route('/ai', methods=['POST'])
def parse_request():
    data = request.get_json(force=True)
    text = data['DisplayText']
    nouns = extract_nouns(text)

    app.logger.info(nouns)
    return jsonify(nouns)
 