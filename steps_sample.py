import json
from pprint import pprint
from steps import *
from Mexicanstyle import *
from framework import *
from IngredientsGenrator import *



text = GetData("https://allrecipes.com/recipe/262326/beef")


steps = GetSteps(text)
pprint(steps)

ingredients = GetIngredients(text)
pprint(ingredients)

[ingredients_new, steps_new] = TransToMexican(ingredients, steps)
pprint(ingredients_new)

directions_new = generate_directions(steps_new)

file = open('data/test.txt', "w")
file.write("Ingredients:\n" + "\n".join(generator(ingredients_new)) + "\nDirections:\n"+ directions_new)
