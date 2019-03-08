import json
from pprint import pprint
from steps import *
from Mexicanstyle import *
from framework import *
from IngredientsGenrator import *


file = open('data/moroccan-chicken-thighs.txt')
text = file.read().split("\n")

methods = open('data/methods.txt').read().split("\n")[:-1]
tools = open('data/tools.txt').read().split("\n")[:-1]

steps = get_steps(text, GetMethods(text), GetIngredients(text), GetTools(text))

ingredients = GetIngredients(text)
pprint(ingredients)

[ingredients_new, steps_new] = TransToMexican(ingredients, steps)

directions_new = generate_directions(steps_new)

file = open('data/moroccan-chicken-thighs-new.txt', "w")
file.write("Ingredients:\n" + "\n".join(generator(ingredients_new)) + "\nDirections:\n"+ directions_new)
