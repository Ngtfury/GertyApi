import random

def get_random_word(number=1):
    with open('english_words.txt', 'r') as f:
        _fulltext = f.read()
        _allwords = list(map(str, _fulltext.split('\n')))


        WORDS = []
        for x in range(number):
            _word = random.choice(_allwords)
            WORDS.append(_word)

        return WORDS


