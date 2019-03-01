import nltk
PunctuationList="!#$%&()*+,-.:;<=>?@[\]^_`{'~}"
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

