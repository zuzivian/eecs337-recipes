import nltk


Mexican_Essentials=[
'chilli pepper', 'coriander', 'jalapeno', 'poblano',
 'avocado', 'chipotle', 'chili powder', 'chorizo', 'salsa verde'
]
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
#ingredients are list of dic
#steps are
def TransToMexican(ingredients,steps):
    isMexican=False
    marker=1
    for step in steps:
        if isMexican:
            break
        for substep in step:
            if containCooking(substep, Addable):
                substep['raw']+=' Add poblano into the '+ containCooking(substep,Addable) +'.'
                substep['raw']+=' Sprinkle with chili pepper.'
                substep['ingredients'].append('chili pepper')
                substep['ingredients'].append('poblano peppers')
                ingredients.append({'name':'poblano peppers','quantity':'6','measurement':'NoItem','Preparation':'NoItem'})
                ingredients.append({'name':'chili pepper','quantity':'1/2','measurement':'teaspoon','Preparation':'NoItem'})
                isMexican=True
                break
            if containCooking(substep, cooking):
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
        ingredients.append({'name':'salsa verde', 'quantity':'1/4', 'measurement':'cup', 'Preparation':'NoItem'})
        ingredients.append({'name':'coriander', 'quantity':'1/8', 'measurement':'cup', 'Preparation':'NoItem'})
        steps.append(
        [{'conditions': None,'ingredients': ['salsa verde','coriander'],
        'methods': ['garnish'],'times': None,'tools':None,
        'raw': 'Serve with a side bowl of salsa verde and coriander to garnish.'
        }]
        )
    return [ingredients, steps]
