import random

# get the list of words from the file
def get_list(file):

def theword(words):
    return random.choice(words)

def guess_valid(guess):
    return len(guess) == 5 and guess in words

def evaluate(guess ):
    return 