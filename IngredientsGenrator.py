import nltk


def generator(listofIngredientsDic):
	res=''
	resultlist=[]
	for ingredient in listofIngredientsDic:
		res=''
		if ingredient['quantity']!='NoItem':
			res+=ingredient['quantity']
			res+=' '
		if ingredient['Preparation']!='NoItem':
			marker=0
			for i in ingredient['Preparation'].split():
				if i in ingredient['name']:
					marker=1
					break
			if marker==0:
				res+=ingredient['quantity']
				res+=' '
		if ingredient['measurement']!='NoItem':
			res+=ingredient['measurement']
			res+=' '
		res+=ingredient['name']
		resultlist.append(res)
	return resultlist

print(generator([{'name': 'chopped onions', 'quantity': '1 1/2', 'measurement': 'cup', 'Preparation': 'chopped '}]))
