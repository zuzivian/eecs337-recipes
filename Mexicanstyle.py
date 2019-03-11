import nltk


Mexican_Essentials=[
'chilli pepper', 'coriander', 'jalapeno', 'poblano',
 'avocado', 'chipotle', 'chili powder', 'chorizo', 'salsa verde'
]

Mexican_replacement= {
    'rice': 'spanish rice',
    'soy sauce': 'hot sauce',
    'bell pepper': 'poblano',
    'sausage' : 'chorizo',
    'lemon' : 'lime',
    'peas' : 'corn',

}

Addable = [
    'pasta','capellini','spaghetti','ziti',
    'fettuccine', 'lasagne','linguine','cavatappi',
    'ditalini','macaroni', 'penne','rigatoni','bowtie','rotini',
    'rice','stock','soup','noodle']

cooking=['stir','mix','sauté']


def containCooking(substep,cook):
	for i in cook:
		for j in substep:
			if i in substep['raw'].lower():
				return i
	return None

def ReplaceIngredient(line, oldingredient, newingredient):
	return line.replace(oldingredient, newingredient)

def TransToMexican(ingredients,steps):
    isMexican=False
    marker=1
    ingredients_replace = Mexican_replacement.keys()
    for ingredient in ingredients:
        for ingredient_replace in ingredients_replace:
            if ingredient_replace in ingredient['name']:
                print(ingredient_replace + ' substitutes ' + Mexican_replacement[ingredient_replace])
                ingredient['name'] = ingredient['name'].replace(ingredient_replace, Mexican_replacement[ingredient_replace])

    for step in steps:
        for substep in step:
            for ingredient in substep['ingredients']:
                for ingredient_replace in ingredients_replace:
                    if ingredient_replace in ingredient:
                        ingredient = Mexican_replacement[ingredient_replace]
                        substep['raw'] = substep['raw'].replace(ingredient_replace, Mexican_replacement[ingredient_replace])
            if isMexican:
                break
            if containCooking(substep, Addable):
                print('poblano added.')
                print('chilli pepper added.')
                substep['raw']+=' Add poblano into the '+ containCooking(substep,Addable) +'.'
                substep['raw']+=' Sprinkle with chili pepper.'
                substep['ingredients'].append('chili pepper')
                substep['ingredients'].append('poblano peppers')
                ingredients.append({'name':'poblano peppers','quantity':'6','measurement':'NoItem','Preparation':'NoItem'})
                ingredients.append({'name':'chili pepper','quantity':'1/2','measurement':'teaspoon','Preparation':'NoItem'})
                isMexican=True
                break
            if containCooking(substep, cooking):
                print('jalapenos added.')
                print('chilli pepper added.')
                ingredients.append({'name':'jalapenos','quantity':'6','measurement':'NoItem','Preparation':'NoItem'})
                ingredients.append({'name':'chili pepper','quantity':'1/2','measurement':'teaspoon','Preparation':'NoItem'})
                substep['raw']+=' Mix in jalapenos and chili powder.'
                substep['ingredients'].append('jalapenos')
                substep['ingredients'].append('chilli powder')
                isMexican=True
                break
    containsSalsa=False
    for ingredient in ingredients:
    	try:
    		if 'salsa' in ingredient['name']:
    			containsSalsa=True
    			break
    	except:
    		continue
    if not containsSalsa:
        print('salsa verde added.')
        print('coriander added.')
        ingredients.append({'name':'salsa verde', 'quantity':'1/4', 'measurement':'cup', 'Preparation':'NoItem'})
        ingredients.append({'name':'coriander', 'quantity':'1/8', 'measurement':'cup', 'Preparation':'NoItem'})
        steps.append(
        [{'conditions': None,'ingredients': ['salsa verde','coriander'],
        'methods': ['garnish'],'times': None,'tools':None,
        'raw': 'Serve with a side bowl of salsa verde and coriander to garnish.'
        }]
        )
    return [ingredients, steps]
