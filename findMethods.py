import pandas as pd
from nltk import *

from ingredients import *
from helpers import *
from AutoCrawl import *
from steps import *

def getVerbs(text):
    methodlist = set()
    #sentences = text.split("\n")
    for sentences in text:
        method = sentence_verbs(sentences)
        methodlist = methodlist.union(set(method))
    return list(methodlist)

def sentence_verbs(sentence):
    vblist = []
    subsentencelist = re.split('[;.:]', sentence)
    for subs in subsentencelist:
        vb = subsentence_verbs(subs)
        vblist = vblist + vb
    return vblist
        
def subsentence_verbs(subsentence):
    tokens = word_tokenize(subsentence)
    tagtup = nltk.pos_tag(tokens)
    methodlist = []
    for i in range(len(tagtup)):
        if i == 0 and tagtup[0][1] not in ["RB", "DT"]:
            methodlist.append(tagtup[i][0].lower())
        elif tagtup[i][1] in ["VB", "VBZ"] and tagtup[i][0] not in ['is', 'are', 'am', 'a', 'an']:
            methodlist.append(tagtup[i][0].lower())
    return methodlist

def getLOfMethods(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = [x.lower() for x in content]
    return content

def getDirections(text):
    recipeText = ""
    recipeText = text[text.index('Directions:\n') + 1:len(text)]
    return recipeText

def isCookingMethod(verblist, allmethods):
    methods = []
    for verb in verblist:
        if verb in allmethods:
            methods.append(verb)
    return methods

def isPrepMethod(verblist, cookingmethod):
    prepmethod = list(set(verblist) - set(cookingmethod))
    return prepmethod

def mainIngCookingMethod(mainingr, sentences, allmethods):
    cookingList = set()
    for sentence in sentences:
        if mainingr in sentence.lower():
            method = sentence_verbs(sentence)
            cooking = isCookingMethod(method, allmethods)
            cookingList = cookingList.union(cooking)

    return list(cookingList)

def parse_max_cook_time(get_times_result):
    timevalue = 0
    if isinstance(get_times_result, str) == True:
        splitted = get_times_result.split(" ")
        if 'hour' in get_times_result:
            timevalue += 3600 * int(splitted[len(splitted)-2])
        elif 'minute' in get_times_result:
            timevalue += 60 * int(splitted[len(splitted)-2])
        elif 'second' in get_times_result:
            timevalue += int(splitted[len(splitted)-2])
        else:
            timevalue += 0
    return timevalue

def longestCookingMethod(sentences, allmethods):
    minimumtime = 0
    for sentence in sentences:
        cookingtimestring = get_times(sentence)
        cookingtimestep = parse_max_cook_time(cookingtimestring)
        if cookingtimestep > 0 and cookingtimestep > minimumtime:
            maincookingverb = sentence_verbs(sentence)
            maincookingmethod = isCookingMethod(maincookingverb, allmethods)
            if len(maincookingmethod) > 0:
                minimumtime = cookingtimestep
    return maincookingmethod

def getMethodsDict(text):
    list_methods = getLOfMethods('ListOfMethods.txt')
    methodlist = [item.lower() for item in list_methods]
    recipeDirectons = getDirections(text)
    pri_method = longestCookingMethod(recipeDirectons, methodlist)
    all_methods = getVerbs(recipeDirectons)
    addi_method = isPrepMethod(methodlist, pri_method)
    methods_dict = {}
    methods_dict['primary'] = pri_method
    methods_dict['other'] = addi_method
    return methods_dict