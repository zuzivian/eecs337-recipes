import nltk
import pandas as pd

PunctuationList="!#$%&()*+,.:;<=>?@[\]^_`{'~}"
PunctuationList+='"'

def RemovePunctuation(line):
	for x in PunctuationList:
		line=line.replace(x,'')
	return line

def GetLatterWord(sen1, w1):
	word_list = nltk.word_tokenize(sen1)
	for i in range(0, len(word_list) - 1):
		if w1 in word_list[i].lower():
			return ' '.join(K for K in word_list[i+1:] )
	return None

def loadTransformTable(directory):
	transformTable = pd.DataFrame()
	datalist = []
	transformTable = pd.read_csv(directory, delimiter=',', header = 0)
	return transformTable

def bigram1EndWithKeyword(sentokenlist, keywordlist):
    possibleBigram = ''
    stl_cutfirst = sentokenlist[1:len(sentokenlist)]
    keyidentify = set(stl_cutfirst).intersection(set(keywordlist))
    if len(keyidentify) > 0:
        keyposition = stl_cutfirst.index(list(keyidentify)[0])
        possibleBigram = sentokenlist[keyposition] + " " + sentokenlist[keyposition+1]
    return possibleBigram