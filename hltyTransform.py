## get tools from a recipe
from nltk import word_tokenize
from nltk import bigrams
from ingredients import *
from helpers import *
from AutoCrawl import *
import copy


def getLOfTrans(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.replace('\n','') for x in content]
    fileds = [x.split('|') for x in content]
    LOfTrans = [(x[0], x[1]) for x in fileds]

    return LOfTrans



def changeQuantity(str1):
    try:
        return convertStrToFloat(str1)
    except:
        return 1/2
    


def replaceIngred(ingredientlist):
    
    # load ListOfHltySub list
    ListOfHltySub = getLOfTrans('ListOfHltySub.txt')
    IngredInSub = [ListOfHltySub[i][0] for i in range(len(ListOfHltySub))]
    ToBeSubed = [ListOfHltySub[i][1] for i in range(len(ListOfHltySub))]
    
    # find the matching items and substitute
    ingredientlist_new = copy.deepcopy(ingredientlist)
    
    for q in range(len(ingredientlist)):
        
        fullwords_ingred = ingredientlist_new[q]['name']
        unigram_ingred = list(word_tokenize(fullwords_ingred))
        bigram_ingred = list(bigrams(unigram_ingred))
        
        # 1. matching full words
        if fullwords_ingred in IngredInSub:
            ind = IngredInSub.index(fullwords_ingred)
            if ToBeSubed[ind] != 'cf':
                ingredientlist_new[q]['name'] = ToBeSubed[ind]
            else:
                quant = ingredientlist_new[q]['quantity']
                ingredientlist_new[q]['quantity'] = changeQuantity(quant)
        else:
            continue
                
                
        # 2. matching two-words phrase
        for item in bigram_ingred:
            item1 = item[0] + ' ' + item[1]
            if item1 in IngredInSub:
                ind = IngredInSub.index(item1)
                if ToBeSubed[ind] != 'cf':
                    ingredientlist_new[q]['name'] = ingredientlist[q]['name'].replace(item1, ToBeSubed[ind])
                else:
                    quant = ingredientlist_new[q]['quantity']
                    ingredientlist_new[q]['quantity'] = changeQuantity(quant)
            else:
                continue
        
        # 3. matching single word
        for i in range(len(unigram_ingred)):
            singleword = unigram_ingred[i]
            bigwords = unigram_ingred[i-1] + ' '+ unigram_ingred[i]
            if singleword in IngredInSub and bigwords not in IngredInSub:
                ind = IngredInSub.index(singleword)
                if ToBeSubed[ind] != 'cf':
                    ingredientlist_new[q]['name'] = ingredientlist[q]['name'].replace(singleword, ToBeSubed[ind])
                else:
                    quant = ingredientlist[q]['quantity']
                    ingredientlist_new[q]['quantity'] = changeQuantity(quant)
            else:
                continue
         
    return ingredientlist_new



def replaceIngrInSteps(ingredientlist, steps):
    
    # get replaced ingredients
    ingredientlist_new = replaceIngred(ingredientlist)
    ingreName_new = [ingredientlist_new[i]['name'] for i in range(len(ingredientlist_new))]
    ingreName = [ingredientlist[i]['name'] for i in range(len(ingredientlist))]
    ingreName_diff = [(ingreName[i], ingreName_new[i]) for i in range (len(ingreName_new)) if ingredientlist[i] != ingredientlist_new[i]]
    ingreName_raw = [ingreName_diff[i][0] for i in range(len(ingreName_diff))]
   
    
    # get new steps    
    for i in range(len(steps)):
        for j in range(len(steps[i])):
            for k in range(len(steps[i][j]['ingredients'])):
                if steps[i][j]['ingredients'][k] in ingreName_raw:
                    ind = ingreName_raw.index(steps[i][j]['ingredients'][k])
                    steps[i][j]['ingredients'][k] = ingreName_diff[ind][1]
    
    return steps
                


def getHltyTrans(ingredientlist, steps):
    
    new_ingredientlist = replaceIngred(ingredientlist)
    
    new_steps = replaceIngrInSteps(ingredientlist, steps)
        
    return [new_ingredientlist, new_steps]


