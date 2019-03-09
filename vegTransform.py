

import pandas as pd
from nltk import *
from ingredients import *
from helpers import *
from AutoCrawl import *
from steps import *

def proteinType(input_protein, masterdata):
    protype = masterdata[masterdata['protein'] == input_protein]['veg_dim'].item()
    return protype

def proteinSub(input_protein, masterdata):
    replacement = masterdata[masterdata['protein'] == input_protein]['veg_closest'].item()
    return replacement

def ingredToVeg(inglist, masterdata):
    replacedict = {}
    for ingfull in inglist:
        print(ingfull)
        ingredient = ingfull['name'].split()
        indict = set(ingredient).intersection(set(masterdata['protein']))
        if len(indict) > 0:
            indictlist = list(indict)
            for i in range(len(indictlist)):
                item = indictlist[i]
                typecheck = proteinType(item, masterdata)
                if typecheck == "meat":
                    typereplace = proteinSub(item, masterdata)
                    replacedict[ingfull['name']] = typereplace
                else:
                    typereplace = item
    return replacedict

def replaceIngrInSteps(steps, replacementdict):
    for step in steps:
        for substep in step:
            if len(set(substep['ingredients']).intersection(set(replacementdict.keys()))) > 0:
                tobereplace = substep['ingredients']
                substep['ingredients'] = []
                for i in range(len(tobereplace)):
                    if tobereplace[i] in list(replacementdict.keys()):
                        newitem = replacementdict[tobereplace[i]]
                        substep['ingredients'].append(newitem)
                        print(tobereplace[i])
                        print(newitem)
                        substep['raw'] = substep['raw'].replace(tobereplace[i], newitem)
                    else:
                        substep['ingredients'].append(tobereplace[i])
                        
    return steps

def replaceIngrInIngrs(ingredients, replacementdict):
    for item in ingredients:
        if item['name'] in list(replacementdict.keys()):
            tobereplace = item['name']
            item['name'] = replacementdict[tobereplace]
                        
    return ingredients

def TransToVeggie(ingredients,steps, masterdata):
    rep_dict = ingredToVeg(ingredients, masterdata)
    if len(rep_dict) > 0:
        newingr = replaceIngrInIngrs(ingredients, rep_dict)
        newsteps = replaceIngrInSteps(steps, rep_dict)
        return [newingr, newsteps]
    else:
        return [ingredientlist, stepsIns]

# masterdata = pd.DataFrame()
# datalist = []
# txtfilename = 'proteins.csv'

# directory = "./data//" + txtfilename
# masterdata = pd.read_csv(directory, delimiter=',', header = 0)

# text = GetData("https://www.allrecipes.com/recipe/150306/the-best-chicken-fried-steak/")
# ingredientlist = GetIngredients(text)
# stepsIns = GetSteps(text)
# #replacementdict = ingredToVeg(ingredientlist)
# #newsteps = replaceIngrInSteps(stepsIns, replacementdict)
# TransToVeggie(ingredientlist,stepsIns)