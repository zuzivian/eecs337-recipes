## get tools from a recipe
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import bigrams, trigrams
from helpers import *
from AutoCrawl import *

def getLOfTools(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = [x.lower() for x in content]
    return content

def getUsefulData(text, speration):
    ind_ingredient = text.index(speration)
    return text[ind_ingredient+1:]

def checkRedun(LOfPhrases):
    # check redundant phrases
    LOfPh_copy = LOfPhrases.copy()
    for item in LOfPhrases:
        token = word_tokenize(item)
        if len(token) == 2 and token[1] in LOfPhrases:
            LOfPh_copy.remove(token[1])       
    return LOfPh_copy

def findTools(text):
    # load tools list
    LOfTools = getLOfTools('dictionary/ListOfTools.txt')
    # get content of "Directions"
    UsefulData = getUsefulData(text,'directions:')
    # find tools in text
    tools = []
    for q in range(len(UsefulData)):
        words_raw = word_tokenize(UsefulData[q])
        # single word
        SingleWord = [SingleWord.lower() for SingleWord in words_raw if SingleWord.isalpha()]
        # two words phrase
        bigram = list(bigrams(SingleWord))
        PhraseOf2 = [' '.join(word) for word in bigram]
        # three words phrase
        trigram = list(trigrams(SingleWord))
        PhraseOf3 = [' '.join(word) for word in trigram]
        for item in SingleWord:
            if item in LOfTools:
                tools.append(item)
        for item in PhraseOf2:
            if item in LOfTools:
                tools.append(item)
        for item in PhraseOf3:
            if item in LOfTools:
                tools.append(item)
        # remove duplicate
        tools = list(set(tools))
        # check redundant words
        tools = checkRedun(tools)
        
    return tools