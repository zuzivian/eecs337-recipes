import json
from pprint import pprint
from steps import get_steps
from steps import generate_directions


file = open('data/moroccan-chicken-thighs.txt')
text = file.read()
pos = text.find("Directions:")
steps_text = text[pos+12:]

ingredients = open('data/ingredients.txt').read().split("\n")[:-1]
methods = open('data/methods.txt').read().split("\n")[:-1]
tools = open('data/tools.txt').read().split("\n")[:-1]

steps = get_steps(steps_text, methods, ingredients, tools)
pprint(steps)

text_new = generate_directions(steps)
pprint(text_new)

file = open('data/moroccan-chicken-thighs-new.txt', "w")
file.write(text_new)
