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

def bigramsMatchKeyword(ingtokens, keyword):
    keywordposition = ingtokens.index(keyword)
    ingbigrams = list(bigrams(ingtokens))
    gen_bigrams = []
    if keywordposition != 0:
        bg_before = ingbigrams[keywordposition-1][0] + " " + ingbigrams[keywordposition-1][1]
        gen_bigrams.append(bg_before)
    if keywordposition != len(ingtokens) - 1:
        bg_after = ingbigrams[keywordposition][0] + " " + ingbigrams[keywordposition][1]
        gen_bigrams.append(bg_after)
    return gen_bigrams

def ingredToVeg(inglist, masterdata):
    replacedict = {}
    for ingfull in inglist:
        ingredient = word_tokenize(ingfull['name'])
        indict = set(ingredient).intersection(set(masterdata['protein']))
        if len(indict) > 0:
            indictlist = list(indict)
            for i in range(len(indictlist)):
                item = indictlist[i]
                typecheck = proteinType(item, masterdata)
                if typecheck == "meat":
                    typereplace = proteinSub(item, masterdata)
                    ingredientWlength = len(ingredient)
                    if ingredientWlength > 2:
                        possibleWord = bigramsMatchKeyword(ingredient, item)
                        replacedict[possibleWord[0]] = typereplace
                        replacedict[possibleWord[0]+'s'] = typereplace
                        if len(possibleWord) == 2:
                            replacedict[possibleWord[1]] = typereplace
                    replacedict[ingfull['name']] = typereplace
                    replacedict[item] = typereplace
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
                        substep['raw'] = substep['raw'].replace(tobereplace[i], newitem)
                    else:
                        substep['ingredients'].append(tobereplace[i])
                        
    return steps

def replaceIngrInIngrs(ingredients, replacementdict):
    for item in ingredients:
        if 'broth' in item['name'] or 'stock' in item['name']:
            item['name'] = "vegetable broth"
        if item['name'] in list(replacementdict.keys()):
            tobereplace = item['name']
            item['name'] = replacementdict[tobereplace]
                        
    return ingredients

def TransToVeggie(ingredients, steps, masterdata):
    rep_dict = ingredToVeg(ingredients, masterdata)
    if len(rep_dict) > 0:
        newingr = replaceIngrInIngrs(ingredients, rep_dict)
        newsteps = replaceIngrInSteps(steps, rep_dict)
        return [newingr, newsteps]
    else:
        return [ingredients, steps]