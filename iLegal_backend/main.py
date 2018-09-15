from flask import Flask
from flask import request, jsonify
from preprocess import extract_nouns
from contact import getContactDetails
import pickle
app = Flask(__name__)

id2MetaData = pickle.load(open('id2MetaData.pkl','r'))
nound2Ids = pickle.load(open('noun2Ids.pkl','r'))
noun2Id = pickle.load(open('noun2Id.pkl','r'))
allNouns = pickle.load(open('allNouns.pkl','r'))


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
        # greeting case
        app.logger.info(hello_name)
        return jsonify(getContactDetails(hello_name))
    else:
        # todo: do something smart, jaccard similarity of documents etc
        return jsonify(res)



if __name__ == "__main__":
     app.run(debug=True)
