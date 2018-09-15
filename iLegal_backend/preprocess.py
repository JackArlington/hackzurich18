import nltk
from nltk.corpus import stopwords

def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    stemmer = nltk.stem.porter.PorterStemmer()
    lemmatizer = nltk.WordNetLemmatizer()
    word = word.lower()
    # word = stemmer.stem_word(word) #if we consider stemmer then results comes with stemmed word, but in this case word will not match with comment
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword. We can increase the length if we want to consider large phrase"""
    swrds = stopwords.words('english')
    accepted = bool(2 <= len(word) <= 42
        and word.lower() not in stopwords.words('english'))
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term


def extract_nouns(text):
    nouns = []
    sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'
    grammar = r"""
        NBAR:
            {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
            
        NP:
            {<NBAR>}
            {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
    """
    chunker = nltk.RegexpParser(grammar)
    toks = nltk.regexp_tokenize(text, sentence_re)
    postoks = nltk.tag.pos_tag(toks)
    app.logger.info(postoks)
    tree = chunker.parse(postoks)
    terms = get_terms(tree)
    for term in terms:
        nouns.append(term)
    return nouns
