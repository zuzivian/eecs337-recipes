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
				res+=ingredient['Preparation']
				res+=' '
		if ingredient['measurement']!='NoItem':
			res+=ingredient['measurement']
			res+=' '
		res+=ingredient['name']
		resultlist.append(res)
	return resultlist

print(generator([{'Preparation': 'chopped',
  'measurement': 'NoItem',
  'name': 'white onion,',
  'quantity': '1/2'}]))
