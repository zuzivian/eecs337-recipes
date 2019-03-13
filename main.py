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
6: See parsed ingredients
7: See parsed methods
8: See parsed tools
9: See parsed steps

'''


def main():
    url = input('Please provide a url: ')
    text = GetData(url)
    steps = GetSteps(text)
    ingredients = GetIngredients(text)
    print("\n" + "".join(text))

    while True:
        print(menu)
        try:
            transform = int(input('Choose a transformation: '))
        except:
            print('invalid input')
            break
        if transform >=0 and transform <= 5:

            [ingredients_new, steps_new] = Transformation(text, transform)

            ingredient_text_new = "\n".join(generator(ingredients_new))
            directions_text_new = generate_directions(steps_new)
            print('Ingredients and Directions After Change are listed as below:')
            print("\nIngredients\n" + ingredient_text_new + "\n\nDirections\n" + directions_text_new)

        elif transform>5 and transform<=9:
            if transform==6:
                for ingredient in ingredients:
                    print('Name:'+ingredient['name'])
                    if ingredient['quantity']!='NoItem':
                        print('Quantity:'+ingredient['quantity'])
                    if ingredient['measurement']!='NoItem':
                        print('Measurement:'+ingredient['measurement'])
                    if ingredient['Preparation']!='NoItem':
                        print('Preparation:'+ingredient['Preparation'])
                    print('\n')

            elif transform==7:
                print('Methods are listed below:')
                print(GetMethods(text))

            elif transform==8:
                print('Tools are listed below:')
                print(GetTools(text))

            else:
                index=0
                for step in steps:

                    print("Step:"+str(index))
                    for substep in step:
                        print("substep:")
                        pprint(substep)
                    index+=1

        else:
            print('invalid input')
            break


if __name__ == '__main__':
    main()
