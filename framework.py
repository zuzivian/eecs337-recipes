from helpers import *
from AutoCrawl import *
from steps import *
from findTools import *
from findMethods import *
from ingredients import *
from pprint import pprint
from Asianstyle import *
from IngredientsGenrator import *
#from vegTransform import *
from VegVeganTransform import *
from hltyTransform import *
from Mexicanstyle import *


def GetData(url):
	#if url already have been crawled, diretly return the crawled data
	if os.path.exists("data/"+url.split('/')[-1]+'.txt'):
		with open("data/"+url.split('/')[-1]+".txt",'r')as fp:
			print('Recipe File already exists')
			return fp.readlines()

	#if is a new url crawled the data an
	else:
		print('New Recipe!')
		data=AutoCrawl(url)
		return data

def GetIngredients(text):
	"""
	Return a list of dictionaries containing Ingredient information
	This dictionary includes keys:
	name/quantity/measurement/Descriptor(optional)/Preparation(optional)
	"""
	# print(FormIngredientList1(text))
	return FormIngredientList1(text)



def GetTools(text):
	"""Return a list of tools such as pans graters"""
	data = [x.strip() for x in text]
	data = [x.lower() for x in data] # convert to lower case
	return findTools(data)



def GetMethods(text):
	"""
	Return a dictionary contains with methods information
	This dictionary includes 2 keys: primary(primary methods such as sauté, broil, boil, poach, etc.)
	and other(Other cooking methods used(e.g. chop, grate, stir, shake, mince, crush, squeeze, etc.))
	"""
	return getMethodsDict(text)



def GetSteps(text):
	"""Return a list of steps that each consist of ingredients, tools, methods, and times"""
	return get_steps(text, GetMethods(text), GetIngredients(text), GetTools(text))



def Transformation(text,category):
    """category is the kind of transformation"""
    """waiting for update"""

    if category==0:
        masterdata = loadTransformTable('./dictionary/proteins.csv')
        ingredientlist = GetIngredients(text)
        stepsIns = GetSteps(text)
        return TransToVeggie(ingredientlist, stepsIns, masterdata)

    elif category==1:
        masterdata = loadTransformTable('./dictionary/proteins.csv')
        ingredientlist = GetIngredients(text)
        stepsIns = GetSteps(text)
        return TransToVegan(ingredientlist, stepsIns, masterdata)

    elif category == 2:
        ingredientlist = GetIngredients(text)
        rawSteps = GetSteps(text)
        return getHltyTrans(ingredientlist, rawSteps)

    elif category == 3:
        return TransToAsian('Korean',GetIngredients(text),GetSteps(text))

    elif category == 4:
        return TransToAsian('Thai',GetIngredients(text),GetSteps(text))

    elif category == 5:
        return TransToMexican(GetIngredients(text),GetSteps(text))



#text = GetData("https://www.allrecipes.com/recipe/221227/honey-brined-fried-chicken-breasts/")
#[new_ingredients, new_steps] = Transformation(text,'healthy')
#pprint("Ingredients:\n" + "\n".join(generator(new_ingredients)) + "\nDirections:\n"+ generate_directions(new_steps))
#text = GetData("https://www.allrecipes.com/recipe/221227/honey-brined-fried-chicken-breasts/")
#[new_ingredients, new_steps] = Transformation(text,'vege')

#pprint("Ingredients:\n" + "\n".join(generator(new_ingredients)) + "\nDirections:\n"+ generate_directions(new_steps))
