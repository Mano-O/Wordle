import pygame
import random

# get the list of words from the file to minimise time and not open file each time
def get_list(file):
    with open(file) as f: # we use with to close the file after its done
        lst = [line.strip() for line in f]
    return lst, set(lst) # return the list

# get the random word
def theword(words):
    return random.choice(words)

file = "words.txt"
words, words_set = get_list(file) # getting words list from the file
word = theword(words)


pygame.init()
clock = pygame.time.Clock() # to set the speed of the game to be equal on all monitors
fps = 60
color = (255,255,0)
grey = (128, 140, 131)
green = (99, 201, 62)
yellow = (242, 242, 48)
black = (79, 79, 66)
white = (255,255,255)
screen = pygame.display.set_mode((500, 570))
pygame.display.set_caption("Wordle")
bg = pygame.image.load("bg.png")
big_font = pygame.font.SysFont("arial", 40)
small_font = pygame.font.SysFont("arial", 16)
board = [["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""]]




guess_count = 0
guess_list = [""] * 6
turn = 0
letters_iterator = 0
game_over = 0
delay = 1



screen.fill(white)

resized_bg = pygame.transform.scale_by(bg, 0.98)



def bg_init():
    global turn, game_over
    if game_over == 0:
        screen.fill(white, (0, turn * 57 + 20 , 500, 570))
        screen.blit(resized_bg, (7,374))
        for i in range(5):
            for j in range(turn, 6):
                rect = pygame.Rect(i * 57 + 110, j * 57.5 + 20,50,50)
                pygame.draw.rect(screen, grey, rect, 3)
                text_entry = big_font.render(board[j][i], True, black)
                screen.blit(text_entry, (i * 57 + 123, j * 57.5 + 20))
        
        delay_message = small_font.render("To turn on/off delays press '/'", True, black)
        screen.blit(delay_message, (110, 354))




def delete():
    global turn, letters_iterator
    letters_iterator -= 1
    board[turn][letters_iterator] = " "




def check_guess(x):
    global turn, letters_iterator, game_over

    for i in range(5):
        guess_list[x] += board[x][i]

    if len(guess_list[x]) == 5 and guess_list[x] in words_set:
        feedback(guess_list[x])
        if guess_list[x] == word:
            game_over = 2
        turn += 1
        letters_iterator = 0
    else: guess_list[x] = ""



def feedback(guess_list):
    global turn
    for i in range(5):
            if guess_list[i] == word[i]:
                rect = pygame.Rect(i * 57 + 110, turn * 57.5 + 20,50,50)
                pygame.draw.rect(screen, green, rect, 0)
                text_entry = big_font.render(board[turn][i], True, white)
                screen.blit(text_entry, (i * 57 + 123, turn * 57.5 + 20))
                pygame.display.update()
                pygame.time.delay(delay * 400)
            elif guess_list[i] in word:
                rect = pygame.Rect(i * 57 + 110, turn * 57.5 + 20,50,50)
                pygame.draw.rect(screen, yellow, rect, 0)
                text_entry = big_font.render(board[turn][i], True, white)
                screen.blit(text_entry, (i * 57 + 123, turn * 57.5 + 20))
                pygame.display.update()
                pygame.time.delay(delay * 400)
            else: 
                rect = pygame.Rect(i * 57 + 110, turn * 57.5 + 20,50,50)
                pygame.draw.rect(screen, grey, rect, 0)
                text_entry = big_font.render(board[turn][i], True, white)
                screen.blit(text_entry, (i * 57 + 123, turn * 57.5 + 20))
                pygame.display.update()
                pygame.time.delay(delay * 400)




running = True
while running:
    clock.tick(fps)
    bg_init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over == 0:
            if event.type == pygame.TEXTINPUT:
                entry = event.__getattribute__('text')
                if entry.isalpha() and letters_iterator <= 4:
                    board[turn][letters_iterator] = entry.lower()
                    letters_iterator += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and letters_iterator >= 1:
                    delete()

                if event.key == pygame.K_RETURN:
                    check_guess(turn) # enter key, make a function to check for list
                
                if event.key in (pygame.K_SLASH, pygame.K_KP_DIVIDE):
                    delay = not(delay)

                if turn >= 6:
                    game_over = 1
            
        if game_over != 0:
            screen.fill(white, (0, 6.2 * 57 + 20 , 500, 570))
            if game_over == 1:
                game_over_string = big_font.render("Game Over!", True, black)
                screen.blit(game_over_string, (160, 400))
                game_over_string = big_font.render("Press Space To Retry", True, black)
                screen.blit(game_over_string, (100, 450))
                show_word_string = big_font.render(f"The Word Was '{word}'", True, black)
                screen.blit(show_word_string, (100, 495))
            else:
                game_winning_string = big_font.render("Congrats! You won", True, black)
                screen.blit(game_winning_string, (110, 430))
                game_over_string = big_font.render("Press Space To Retry", True, black)
                screen.blit(game_over_string, (100, 469))
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE:
                    turn = 0
                    letters_iterator = 0
                    guess_list = [""] * 6
                    board = [[""] * 5 for _ in range(6)]
                    game_over = False
                
            
    pygame.display.flip()
pygame.QUIT
