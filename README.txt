the code is implemented in functions to make it easier to read.

at first, there is the 'get_list' function which is used to open the words text file and
save the words into a list for ease of access leater on

then the list is used in 'the_word' function to get a random word for the user to guess

and the 'guess_valid' function is used to check if the user input is valid, ie it is 5 letters
long and is a valid English word

then the 'evaluate' function is used to print the input of the user but with visual feedback, if
the letter is in a correct position it is printed in green and if the letter is in the word but in
the wrong position it is printed in yellow other wise the letter is grey

I was going to user a color library here to change colors but i found it easier to use the ANSI escape codes within the strings

after we initialized the functions we writing the game logic, we set an attempts counter to 1 and
increment it each time the user inputs a valid guess, and after 6 inputs if the user didn't get the
word he loses with each input we check if it is correct and he won or not and if it is valid or not if
it isn't the user has to re-input before continuing 
