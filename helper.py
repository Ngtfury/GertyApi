import random

def get_random_word():
    with open('english_words.txt', 'r') as f:
        _fulltext = f.read()
        _allwords = list(map(str, _fulltext.split('\n')))


        return random.choice(_allwords)


