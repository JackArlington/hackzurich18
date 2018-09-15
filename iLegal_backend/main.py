from flask import Flask
from flask import request, jsonify
from preprocess import extract_nouns
app = Flask(__name__)

@app.route("/")
def hello():
    return "iLegal backend V1.1.2"

@app.route('/ai', methods=['POST'])
def parse_request():
    data = request.get_json(force=True)
    text = data['DisplayText']
    hello_name, nouns = extract_nouns(text.lower())
    app.logger.info(nouns)
    res = {'nouns': nouns, 'hello_name':hello_name}
    if hello_name is not "":
        # todo: do something smart, jaccard similarity of documents etc
        return jsonify(res)
    else:
        # greeting case
        # todo: call greeting method 
        return jsonify(res)
 

if __name__ == "__main__":
     app.run(debug=True)
