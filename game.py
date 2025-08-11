import pygame

pygame.init()
color = (255,255,0)
grey = (128, 140, 131)
green = (99, 201, 62)
yellow = (242, 242, 48)
black = (79, 79, 66)
screen = pygame.display.set_mode((500, 570))
pygame.display.set_caption("Test Window")
print(pygame.font.get_fonts())
bg = pygame.image.load("bg.png")
font = pygame.font.SysFont("arial", 40)
board = [["a", "b", "c", "d", "e"],
        ["a", "b", "c", "d", "e"],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]]



guess_count = 0
guess_list = [""] * 6
turn = 0
letters_iterator = 0



def bg_init():
    screen.fill((255,255,255))
    # screen.blit(bg, (-7,10))
    for i in range(5):
        for j in range(6):
            rect = pygame.Rect(i * 57 + 110, j * 57.5 + 20,50,50)
            pygame.draw.rect(screen, grey, rect, 3)
            text_entry = font.render(board[j][i], True, black)
            screen.blit(text_entry, (i * 57 + 123, j * 57.5 + 20))


def delete():
    return

def check_guess():
    return

running = True
while running:
    bg_init()
    
    '''for i in range(0,10):
        for j in range(0,3):
            s = "0123456789"
            print(s[i])'''
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.TEXTINPUT:
            entry = event.__getattribute__('text')
            if entry.isalpha() and letters_iterator <= 4:
                board[turn][letters_iterator] = entry.lower()
                letters_iterator += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters_iterator >= 1:
                letters_iterator -= 1
                board[turn][letters_iterator] = " "
            if event.key == pygame.K_RETURN:
                print("") # enter key, make a function to check for list
                
            
    pygame.display.flip()
pygame.QUIT
