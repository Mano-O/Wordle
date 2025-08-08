import random

# get the list of words from the file to minimise time and not open file each time
def get_list(file):
    with open(file) as f: # we use with to close the file after its done
        lst = [line.strip() for line in f]
    return lst, set(lst) # return the list

# get the random word
def theword(words):
    return random.choice(words)

# check if the guess is valid
def guess_valid(guess, words):
    return len(guess) == 5 and guess in words

#color the correct letters in the word
def evaluate(guess):
    strng = ""

    for i in range(len(guess)):
        if guess[i] == the_word[i]: # green for correct placement
            strng += '\033[32m' + guess[i]
        elif guess[i] in the_word: # yellow if its in the word
            strng += '\033[33m' + guess[i]
        else: strng += '\033[0m' + guess[i] # grey if its wrong

    return strng + '\033[0m' # add ending color character


attempts = 1 # counter for number of attempts
file = "words.txt"
words, words_set = get_list(file) # getting words list from the file
the_word = theword(words)

while (attempts <= 6):

    guess = input(f"Guess number {attempts}: ").lower() # getting the user guess

    if guess == the_word: # checking if the guess is correct
        print("Congrats you won!")
        break

    if not(guess_valid(guess, words_set)): # if the input is not valid re-input
        print("Invalid word")
        continue

    print(evaluate(guess)) # print the input colored for feedback

    attempts += 1 # increment attempts counter

if attempts == 7: # game over
    print("Game over the word was:", the_word) 