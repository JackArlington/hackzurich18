from flask import Flask
from flask import request, jsonify
from preprocess import extract_nouns
from contact import getContactDetails
import pickle
app = Flask(__name__)

id2MetaData = pickle.load(open('id2MetaData.pkl','rb'))
noun2Ids = pickle.load(open('noun2Ids.pkl','rb'))
noun2Id = pickle.load(open('noun2Id.pkl','rb'))
allNouns = pickle.load(open('allNouns.pkl','rb'))


@app.route("/")
def hello():
    print(allNouns)
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
        relevant_nouns = []
        for noun in nouns:
            if noun in allNouns:
                relevant_nouns.append(noun)
        app.logger.info("Detected the following keywords: ")
        app.logger.info(relevant_nouns)
        relevant_cases = {}

        for noun in relevant_nouns:
            for i in noun2Ids[noun]:
                relevant_cases[i] = relevant_cases.get(i, 0)
        similarities = []
        for i, count in relevant_cases.items():
            app.logger.info("count:")
            app.logger.info(count)
            app.logger.info(len(relevant_nouns))
            app.logger.info(id2MetaData[i]["numberOfNouns"])
            similarities.append((i, count / (len(relevant_nouns) + id2MetaData[i]["numberOfNouns"])))
        
        sorted(similarities, key=lambda x: x[1], reverse=True)
        app.logger.info(similarities)
        i = similarities[0][0]
        app.logger.info(similarities)

        res = {
            "text": "This case might be relevant for your current discussion: ",
            "file_name": id2MetaData[i]["fileName"],
            "case_title": id2MetaData[i]["name"],
            "catch_phrases": id2MetaData[i]["abstract"]
        }
        return jsonify(res)



if __name__ == "__main__":
     app.run(debug=True)
