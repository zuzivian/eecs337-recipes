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


Korean_Essentials=[
'Soy Sauce','Gralic','Sesame seed oil','Rice','Korean chili pepper powder',
'ginger','green oninons','Korean Soybean Paste'
]

Thai_Essentials=['Thai Fish Sauce','Curry Paste',
'Coconut Milk','Rice','Limes','Fresh Herbs','Lemongrass','basil','peanuts'
]


Addable = [
    'pasta','capellini','spaghetti','ziti',
    'fettuccine', 'lasagne','linguine','cavatappi',
    'ditalini','macaroni', 'penne','rigatoni','bowtie','rotini',
    'rice','stock','soup','noodle']

cooking=['stir','mix','Sauté']


def containCooking(substep,cook):
	for i in cook:
		for j in substep:
			if i in substep['raw'].lower():
				return i
	return None
#ingredients are list of dic
#steps are
def TransToAsian(ThaiOrKorean,ingredients,steps):
	changes=[]
	if ThaiOrKorean=='Thai':
		isThai=False
		marker=1
		for step in steps:
			if marker==0:
				break
			for substep in step:
				if containCooking(substep,Addable):
					materail=containCooking(substep,Addable)
					s=' Add coconut milk and fish sauce into the '+materail+'.'
					substep['raw']+=s
					substep['raw']+=' Sprinkle with curry powder'
					substep['ingredients'].append('coconut milk')
					substep['ingredients'].append('fish sauce')
					substep['ingredients'].append('curry powder')
					isThai=True
					marker=0
					break

		if not isThai:
			for step in steps:
				if marker==0:
					break
				for substep in step:
					if containCooking(substep,cooking):
						ingredients.append({'name':'fish sauce','quantity':'3','measurement':'teaspoon','Preparation':'NoItem'})
						ingredients.append({'name':'coconut milk','quantity':'2','measurement':'teaspoon','Preparation':'NoItem'})
						ingredients.append({'name':'curry paste','quantity':'1/2','measurement':'teaspoon','Preparation':'NoItem'})
						substep['raw']+=' Mix with Coconut and Thai Fish Sauce.'
						substep['raw']+=' Sprinkle with curry powder.'
						substep['ingredients'].append('coconut milk')
						substep['ingredients'].append('fish sauce')
						substep['ingredients'].append('curry powder')
						isThai=True
						marker=0
						break
		isRiceNeed=True
		for ingredient in ingredients:
			try:
				if 'rice' in ingredient['name']:
					isRiceNeed=False
					break
			except:
				continue
		if isRiceNeed:
			ingredients.append({'name':'cooked rice','quantity':'2','measurement':'cup','Preparation':'cooked'})
			changes.append({'name':'cooked rice','quantity':'2','measurement':'cup','Preparation':'cooked'})
		changes.append({'name':'lime','quantity':'1','measurement':'NoItem','Preparation':'NoItem'})
		changes.append({'name':'roasted peanuts','quantity':'1/2','measurement':'cup','Preparation':'roasted'})
		changes.append({'name':'fresh cilantro','quantity':'3','measurement':'tablespoon','Preparation':'NoItem'})	

		ingredients.append({'name':'lime','quantity':'1','measurement':'NoItem','Preparation':'NoItem'})
		ingredients.append({'name':'roasted peanuts','quantity':'1/2','measurement':'cup','Preparation':'roasted'})
		ingredients.append({'name':'fresh cilantro','quantity':'3','measurement':'tablespoon','Preparation':'NoItem'})
		steps.append( [{'conditions': None,'ingredients': ['rice','lime','roasted peanuts','fresh cilantro'],
			'methods': ['squeeze','sprinkle'],'times': None,'tools':None,
			'raw': 'Serve over rice with a squeeze of lime and a sprinkle of peanuts and chopped cilantro.',
  		 }])

		steps.append( [{'conditions': None,'ingredients': ['lemon grass','basil','herbs'],
				'methods': ['garnish'],'times': None,'tools':None,
				'raw': 'Garnish the dishes with lemongrass, basil and herbs.'
	  		 }])

		changes.append({'name':'minced lemon grass','quantity':'2','measurement':'NoItem','Preparation':'minced'})
		changes.append({'name':'diced herbs','quantity':'2','measurement':'teaspoon','Preparation':'diced'})
		changes.append({'name':'fresh basil','quantity':'1/4','measurement':'cup','Preparation':'NoItem'})

		ingredients.append({'name':'minced lemon grass','quantity':'2','measurement':'NoItem','Preparation':'minced'})
		ingredients.append({'name':'diced herbs','quantity':'2','measurement':'teaspoon','Preparation':'diced'})
		ingredients.append({'name':'fresh basil','quantity':'1/4','measurement':'cup','Preparation':'NoItem'})

		print('\nThings added:')
		for i in generator(changes):
			print(i)
		print('\n')
	if ThaiOrKorean=='Korean':
		isKorean=False
		marker=1
		for step in steps:
			if marker==0:
				break
			for substep in step:
				if containCooking(substep,Addable):
					materail=containCooking(substep,Addable)
					s=' Add soy sauce into the '+materail+'. '
					substep['raw']+=s
					substep['raw']+='Sprinkle with Korean chili pepper powder.'
					substep['ingredients'].append('Korean chili pepper powder')
					substep['ingredients'].append('soy sauce')
					ingredients.append({'name':'soy sauce','quantity':'1','measurement':'teaspoon','Preparation':'NoItem'})
					ingredients.append({'name':'Korean chili pepper powder','quantity':'1/2','measurement':'teaspoon','Preparation':'NoItem'})

					changes.append({'name':'soy sauce','quantity':'1','measurement':'teaspoon','Preparation':'NoItem'})
					changes.append({'name':'Korean chili pepper powder','quantity':'1/2','measurement':'teaspoon','Preparation':'NoItem'})
					isKorean=True
					marker=0
					break

		if not isKorean:
			for step in steps:
				if marker==0:
					break
				for substep in step:
					if containCooking(substep,cooking):
						ingredients.append({'name':'soy sauce','quantity':'1','measurement':'teaspoon','Preparation':'NoItem'})
						ingredients.append({'name':'Korean chili pepper powder','quantity':'1/2','measurement':'teaspoon','Preparation':'NoItem'})

						changes.append({'name':'soy sauce','quantity':'1','measurement':'teaspoon','Preparation':'NoItem'})
						changes.append({'name':'Korean chili pepper powder','quantity':'1/2','measurement':'teaspoon','Preparation':'NoItem'})

						substep['raw']+=' Mix with soy sauce.'
						substep['raw']+=' Sprinkle with Korean chili pepper powder.'
						substep['ingredients'].append('soy sauce')
						substep['ingredients'].append('Korean chili pepper powder')
						isKorean=True
						marker=0
						break
		isRiceNeed=True
		for ingredient in ingredients:
			try:
				if 'rice' in ingredient['name']:
					isRiceNeed=False
					break
			except:
				continue
		if isRiceNeed:
			ingredients.append({'name':'cooked rice','quantity':'2','measurement':'cup','Preparation':'cooked'})
			changes.append({'name':'cooked rice','quantity':'2','measurement':'cup','Preparation':'cooked'})

		ingredients.append({'name':'vinegar','quantity':'1','measurement':'teaspoon','Preparation':'NoItem'})
		changes.append({'name':'vinegar','quantity':'1','measurement':'teaspoon','Preparation':'NoItem'})

		steps.append( [{'conditions': None,'ingredients': ['rice','vinegar'],
			'methods': ['squeeze','sprinkle'],'times': None,'tools':None,
			'raw': 'Serve over rice covering with one teaspoon of vinegar.',
  		 }])

		steps.append( [{'conditions': None,'ingredients': ['garlic','ginger'],
				'methods': ['garnish'],'times': None,'tools':None,
				'raw': 'Garnish the dishes with ginger and green onions.'
	  		 }])
		ingredients.append({'name':'diced ginger','quantity':'1/2','measurement':'cup','Preparation':'diced'})
		ingredients.append({'name':'diced green onions','quantity':'2','measurement':'teaspoon','Preparation':'diced'})
		changes.append({'name':'diced ginger','quantity':'1/2','measurement':'cup','Preparation':'diced'})
		changes.append({'name':'diced green onions','quantity':'2','measurement':'teaspoon','Preparation':'diced'})


		print('\nThings added:')
		for i in generator(changes):
			print(i)
		print('\n')
	return [ingredients, steps]
