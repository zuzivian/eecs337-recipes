import nltk


def generator(listofIngredientsDic):
	res=''
	resultlist
	for ingredient in listofIngredientsDic:
		res=''
		if ingredient['quantity']!='NoItem':
			res+=ingredient['quantity']
			res+=' '
		if ingredient['Preparation']!='NoItem':
			res+=ingredient['quantity']
			res+=' '
		if ingredient['measurement']!='NoItem':
			res+=ingredient['measurement']
			res+=' '
		res+=ingredient['name']
		resultlist.append(res)
	return resultlist