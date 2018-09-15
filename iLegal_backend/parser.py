#!/bin/bash

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

fileName2Id = {}
noun2Ids = {}
i = 0
for fileName in os.listdir('../corpus/fulltext_dev'):
    File = open(os.path.join('../corpus/fulltext_dev', fileName))

    lines = File.read()
    fileName2Id[i] = (fileName, getName(lines),os.path.join(script_dir, fileName))


    # print(fileName)
    # print(getName(lines))
    # print(getAllCatchPhrases(lines))
    nouns = []

    for catchPhrase in getAllCatchPhrases(lines):

        is_hello_exp, nouns = extract_nouns(catchPhrase)
        for noun in nouns:
            if noun in noun2Ids:
                noun2Ids[noun].add(i)
            else:
                noun2Ids[noun] = set([i])
    i += 1
pickle.dump(fileName2Id, open('fileName2Id.pkl','wb'))
pickle.dump(noun2Ids, open('noun2Ids.pkl','wb'))
