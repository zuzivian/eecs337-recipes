import nltk
from pprint import pprint


def generate_directions(step_list):
    steps = []
    for step in step_list:
        steps.append(" ".join([substep['raw'] for substep in step]))
    text= "\n".join(steps)
    return text

def get_steps(text, methods, ingredients, tools):
    step_list = []
    for step in text.split("\n"):
        if not step:
            continue
        substep_list = []
        sent_text = nltk.sent_tokenize(step) # this gives us a list of sentences
        for sentence in sent_text:
            if not sentence:
                continue
            substep = {}
            tokens = nltk.word_tokenize(sentence.lower())
            substep['raw'] = sentence
            substep['methods'] = [method for method in methods if method in tokens]
            # step['method'] = step['methods'][0]
            # substep['ingredients'] = [ingredient.name for ingredient in ingredients if ingredient.name in tokens]
            substep['ingredients'] = [ingredient for ingredient in ingredients if ingredient in tokens]
            substep['tools'] = [tool for tool in tools if tool in tokens]
            substep['times'] = get_times(sentence)
            substep['conditions'] = get_conditions(sentence)
            substep_list.append(substep)
        step_list.append(substep_list)
    return step_list


def get_times(text):
    end_words = ['minutes', 'minute', 'hours', 'hour']
    for word in end_words:
        if word not in text:
            continue
        index = text.find(word)
        punct = get_punctuation_index(text[:index+len(word)], 1)
        num = get_number_index(text[punct+1:index+len(word)], 0)
        return text[punct+num+1:index+len(word)]

def get_conditions(text):
    begin_words = ["for", "until"]
    for word in begin_words:
        if word not in text:
            continue
        index = text.find(word)
        punct = get_punctuation_index(text[index:], 0)
        return text[index:index+punct]

def get_number_index(text, dir):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    indices = []
    for num in numbers:
        index = text.rfind(num) if dir else text.find(num)
        if index > -1:
            indices.append(index)
    return max(indices) if dir else min(indices)

def get_punctuation_index(text, dir):
    punctuation = [".", ",", ";"]
    indices = []
    for punct in punctuation:
        index = text.rfind(punct) if dir else text.find(punct)
        if index > -1:
            indices.append(index)
    return max(indices) if dir else min(indices)
