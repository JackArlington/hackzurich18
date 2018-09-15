import os
import nltk
from textblob import TextBlob
import re
from nltk import word_tokenize
from preprocess import *
import pickle

def getAllCatchPhrases(case):
    return re.findall(r'<catchphrase "id=c[0-9]{1,3}">(.*)</catchphrase>',case)

def getName(case):
    return re.findall(r'<name>(.*)</name>',case)


nltk.download('stopwords')
script_dir = os.path.dirname(__file__)

id2MetaData = {}
noun2Ids = {}
id2Nouns = {}
allNouns = []

i = 0
for fileName in os.listdir('../corpus/fulltext'):
    try:
        File = open(os.path.join('../corpus/fulltext', fileName))

        lines = File.read()

        # print(fileName)
        # print(getName(lines))
        # print(getAllCatchPhrases(lines))
        nouns = []
        caseNouns = set()
        for catchPhrase in getAllCatchPhrases(lines):

            name, nouns = extract_nouns(catchPhrase)
            #allNouns.add(nouns)
            for noun in nouns:
                caseNouns.add(noun)
                if noun not in allNouns:
                    allNouns.append(noun)
                if noun in noun2Ids:
                    noun2Ids[noun].add(i)
                else:
                    noun2Ids[noun] = set([i])
                if i in id2Nouns:
                    id2Nouns[i].add(noun)
                else:
                    id2Nouns[i] = set([noun])
        id2MetaData[i] = {
            'fileName': fileName,
            'name': getName(lines),
            'path': os.path.join(script_dir, fileName),
            'abstract': list(getAllCatchPhrases(lines)),
            'numberOfNouns': len(caseNouns)
            }
        i += 1

    except:
        print("Oo")

print(id2MetaData)
print(noun2Ids)
print(id2Nouns)

pickle.dump(id2MetaData, open('id2MetaData.pkl','wb'))
pickle.dump(noun2Ids, open('noun2Ids.pkl','wb'))
pickle.dump(id2Nouns, open('id2Nouns.pkl','wb'))
pickle.dump(allNouns, open('allNouns.pkl','wb'))
