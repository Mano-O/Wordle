import random

# get the list of words from the file
def get_list(file):
    with open(file) as f: # we use with to close the file after its done
        lst = [line.strip() for line in f]
    return lst # return the list

def theword(words):
    return random.choice(words)

def guess_valid(guess):
    return len(guess) == 5 and guess in words

def evaluate(guess ):
    return

attempts = 1
file = "words.txt"
words = get_list(file)
the_word = theword(words)

while (attempts <= 6):

    guess = input(f"Guess number {attempts}: ").lower()

    if guess == the_word:
        print("Congrats you won!")
        break

    if not(guess_valid):
        print("Invalid word")
        continue

    print(evaluate) #to make colors

    attempts += 1

if attempts == 7:
    print("Game over the word was:", the_word) 