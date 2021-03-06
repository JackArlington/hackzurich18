from flask import Flask
from flask import request, jsonify
from preprocess import extract_nouns
from contact import getContactDetails
from flask_cors import CORS, cross_origin
import pickle
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

id2MetaData = pickle.load(open('id2MetaData.pkl','rb'))
noun2Ids = pickle.load(open('noun2Ids.pkl','rb'))
noun2Id = pickle.load(open('noun2Id.pkl','rb'))
allNouns = pickle.load(open('allNouns.pkl','rb'))


@app.route("/")
@cross_origin()
def hello():
    return "iLegal backend V1.1.2"

@app.route("/keywords")
@cross_origin()
def getAllKeywords():
    return jsonify(allNouns)

@app.route('/ai', methods=['POST'])
@cross_origin()
def parse_request():
    data = request.get_json(force=True)
    text = data['DisplayText']
    hello_name, nouns = extract_nouns(text.lower())
    app.logger.info(nouns)
    res = {"result":"empty"}    # there is no result
    if hello_name is not "":
        # greeting case
        app.logger.info(hello_name)
        res = getContactDetails(hello_name)
    else:
        # todo: do something smart, jaccard similarity of documents etc
        relevant_nouns = []
        for noun in nouns:
            if noun in allNouns:
                relevant_nouns.append(noun)
        app.logger.info("Detected the following keywords: ")
        app.logger.info(relevant_nouns)
        if len(relevant_nouns) > 0:

            relevant_cases = {}

            for noun in relevant_nouns:
                for i in noun2Ids[noun]:
                    relevant_cases[i] = relevant_cases.get(i, 0) + 1
            similarities = []
            for i, count in relevant_cases.items():
                app.logger.info("count:")
                app.logger.info(count)
                app.logger.info(len(relevant_nouns))
                app.logger.info(id2MetaData[i]["numberOfNouns"])
                similarities.append((i, count / (len(relevant_nouns) + id2MetaData[i]["numberOfNouns"])))

            similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
            app.logger.info(similarities)
            if len(similarities) > 0:
                app.logger.info(len(similarities))
                app.logger.info(similarities)
                i = similarities[0][0]
                app.logger.info(similarities)
                catchphrases = id2MetaData[i]["abstract"]
                relevant_catchphrase = ""
                if len(catchphrases) > 0:
                    relevant_catchphrase = catchphrases[0]
                best_catchphrases = []
                for ph in catchphrases:
                    cnt = 0
                    for n in relevant_nouns:
                        if ph.find(n) > -1:
                            cnt +=1
                    best_catchphrases.append( (ph, cnt))
                best_catchphrases = sorted(best_catchphrases, key=lambda x: x[1], reverse=True)
                app.logger.info("best catchphrases:")
                app.logger.info(best_catchphrases)
                if len(best_catchphrases) > 0:
                    relevant_catchphrase = best_catchphrases[0][0]

                res = {
                    "result": "success",
                    "text": "This case might be relevant for your current discussion: ",
                    "file_name": id2MetaData[i]["fileName"],
                    "case_title": id2MetaData[i]["name"],
                    "catch_phrases": id2MetaData[i]["abstract"],
                    "relevant_keywords": relevant_nouns,
                    "relevant_catchphrase": relevant_catchphrase
                }
    return jsonify(res)


if __name__ == "__main__":
     app.run(host='0.0.0.0', debug=True)
