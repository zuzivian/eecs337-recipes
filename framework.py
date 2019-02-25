from helpers import *
from AutoCrawl import *

def GetData(url):
	#if url already have been crawled, diretly return the crawled data
	if os.path.exists("data/"+url.split('/')[-2]+'.txt'):
		with open("data/"+url.split('/')[-2]+".txt",'r')as fp:
			print('Recipe File already exists')
			return fp.readlines()

	#if is a new url crawled the data an 
	else:
		print('New Recipe!')
		data=AutoCrawl(url)
		return data

def GetIngredients(text):
	"""
	Return a dictionary contains with Ingredient information
	This dictionary includes keys: 
	name/quantity/measurement/Descriptor(optional)/Preparation(optional)
	"""
	return {}


def GetTools(text):
	"""Return a list of tools such as pans graters"""
	return []


def GetMethods(text):
	"""
	Return a dictionary contains with methods information
	This dictionary includes 2 keys: primary(primary methods such as sauté, broil, boil, poach, etc.)
	and other(Other cooking methods used(e.g. chop, grate, stir, shake, mince, crush, squeeze, etc.))
	"""
	
	return {}




def GetSteps(text):
	"""Return a list of steps that each consist of ingredients, tools, methods, and times"""
	return []



def Transformation(category):
	"""category is the kind of transformation"""
	"""waiting for update"""


print(GetData("https://www.allrecipes.com/recipe/150306/the-best-chicken-fried-steak/"))
