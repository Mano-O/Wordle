the code is implemented in functions to make it easier to read.

at first, there is the 'get_list_api' function which is used to open a github repo with the 5 letter words 
and save the words into a list for ease of access later on

then the list is used in 'the_word' function to get a random word for the user to guess

and in the game loop we initialize pygame which is the library responsible for the gui interface and we set the clock
so the speed us unified across machines
a 2d list is set to save the user input as rows and colums, and then printed with the background of the game, when
the user inputs something new the list is updated and printed on the screen

the usre input is checked if it is an alphapet or not by .isalpha() and if it is then it is passed as a lowercase letter
by .lower() and an iterator is updated so the user can input the next letter in the row

when the user wishes to confirm a guess he presses enter and it is checked by chec_guess, where it check if the guess is
5 letters and if it is an english word, and if it is then it is passed to the feedback function which checks if the letters
match the secret word and colors them accordingly, and after the feedback is given it checks if the user guessed the correct
word or not

if the user guessed it correctly the game congarts him and can restart by pressing space
the users turns are counted by the turns variable which is also the row he is writing on, if he passes 6 turns he loses and word
is revealed to him

i added the option to toggle the delay on/off by pressing '/'
an alternative approach to the pygame.time.delay() was pygame.time.get_ticks() but delay was easier to implement 

all key presses are checked in the game loop by event.type

an alternative approach to having bg_init in the game loop and always rendering the screen would be to render it once and only render it again when changes occur

i considered adding a leaderboard and making the user input the desired word length and attempts count
but didn't to stick with the original game