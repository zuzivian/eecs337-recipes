import nltk
from pprint import pprint
from nltk.util import ngrams
from helpers import RemovePunctuation


def generate_directions(step_list):
    steps = []
    for step in step_list:
        steps.append(" ".join([substep['raw'] for substep in step]))
    text= "\n".join(steps)
    return text

def find_matching(sentence, strings):
    matches = []
    for string in strings:
        found = False
        processed = RemovePunctuation(string.lower())
        tokens = nltk.word_tokenize(processed)
        for n in [5, 4, 3, 2, 1]:
            ngram_list = ngrams(tokens,n)
            for ngram in ngram_list:
                joined_ngram = ' '.join(ngram)
                if joined_ngram in sentence.lower():
                    if joined_ngram in matches:
                        continue
                    matches.append(joined_ngram)
                    found = True
                    break
            if found:
                break
    return list(set(matches))

def get_steps(text, methods, ingredients, tools):
    step_list = []
    methods = methods['primary'] + methods['other']
    in_ingredient_section = True
    for step in text:
        if "Directions" in step:
            in_ingredient_section = False
            continue
        if not step or in_ingredient_section:
            continue
        substep_list = []
        sent_text = nltk.sent_tokenize(step) # this gives us a list of sentences
        for sentence in sent_text:
            if not sentence:
                continue
            substep = {}
            substep['methods'] = find_matching(sentence, methods)
            substep['tools'] = find_matching(sentence, tools)
            ingredient_names = [ingredient['name'] for ingredient in ingredients]
            substep['ingredients'] = find_matching(sentence, ingredient_names)
            substep['times'] = get_times(sentence)
            substep['conditions'] = get_conditions(sentence)
            substep['raw'] = sentence
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
    if len(indices) == 0:
        return 0
    return max(indices) if dir else min(indices)

def get_punctuation_index(text, dir):
    punctuation = [".", ",", ";"]
    indices = []
    for punct in punctuation:
        index = text.rfind(punct) if dir else text.find(punct)
        if index > -1:
            indices.append(index)
    if len(indices) == 0:
        return 0
    return max(indices) if dir else min(indices)
