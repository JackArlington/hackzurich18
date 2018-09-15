#!/bin/bash

import os
import nltk
from textblob import TextBlob
import re
from nltk import word_tokenize
import nltk


def getAllCatchPhrases(case):
    return re.findall(r'<catchphrase "id=c[0-9]{1,3}">(.*)</catchphrase>',case)

def getName(case):
    return re.findall(r'<name>(.*)</name>',case)


nltk.download('stopwords')
script_dir = os.path.dirname(__file__)

for fileName in os.listdir('corpus/fulltext_dev'):

    File = open(os.path.join('./corpus/fulltext_dev', fileName))
    print(os.path.join(script_dir, fileName))
    lines = File.read()

    # print(fileName)
    # print(getName(lines))
    # print(getAllCatchPhrases(lines))
    nouns = []

    for catchPhrase in getAllCatchPhrases(lines):
        tokens = word_tokenize(catchPhrase)
        text = nltk.Text(tokens)
        tags = nltk.pos_tag(tokens)

        nouns = [word for word,pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
        print(nouns)
