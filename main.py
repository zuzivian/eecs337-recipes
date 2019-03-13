from framework import *
from pprint import pprint

menu = '''
-------------------
TRANSFORMATION MENU
-------------------
0: Transform to vegetarian
1: Transform to vegan
2: Transform to healthy
3: Transform to Korean
4: Transform to Thai
5: Transform to Mexican

'''


def main():
    url = input('Please provide a url: ')
    text = GetData(url)
    steps = GetSteps(text)
    ingredients = GetIngredients(text)
    print("\n" + "".join(text))

    print("Ingredients:")
    for ingredient in ingredients:
        pprint(ingredient)
    print("\n\nDirections:")
    for step in steps:
        print("step:")
        for substep in step:
            print("substep:")
            pprint(substep)



    while True:
        print(menu)
        transform = int(input('Choose a transformation: '))
        if transform < 0 or transform > 5:
            print("Error: invalid code")
        else:
            break

    [ingredients_new, steps_new] = Transformation(text, transform)

    ingredient_text_new = "\n".join(generator(ingredients_new))
    directions_text_new = generate_directions(steps_new)
    print('Ingredients and Directions After Change are listed as below:')
    print("\nIngredients\n" + ingredient_text_new + "\n\nDirections\n" + directions_text_new)


if __name__ == '__main__':
    main()
