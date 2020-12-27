import pygame
import math # used for mousebuttondown variable, basically like pythagorean's theorem to get distance bewteen two points( mouse to button)
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Hanging of Triminator!")

# button variables - mathemematical eqn used to equally space each circle. chr = character
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('quicksand', 50)
WORD_FONT = pygame.font.SysFont('quicksand', 70)
TITLE_FONT = pygame.font.SysFont('quicksand', 80)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables - words to describe me
hangman_status = 0
words = ["BEARD", "BALD", "HANDSOME", "TRIM"]
word = random.choice(words)
guessed = []

# colors
BACKGROUND = (192,192,192)
TEXT = (0,0,128)


def draw():
    win.fill(BACKGROUND)

    # draw title
    text = TITLE_FONT.render("DEATH OF TRIMINATOR", 1, TEXT)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, TEXT)
    win.blit(text, (400, 200))

    # draw buttons - ltr = letter, rendering is used to make image appear solid and 3 dimensional. The eqns used allowed the letters to be perfectly in the center of the buttons.
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, TEXT, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, TEXT)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message): #function displays winning or losing
    pygame.time.delay(1000) #1000 is millisecs, so 1 sec delay 
    win.fill(BACKGROUND)
    text = WORD_FONT.render(message, 1, TEXT)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw() #Draw is here so we see change immediately after a click rather than using it earlier and waiting for the next loop.

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("You WON!")
            break

        if hangman_status == 6:
            display_message("You LOST!")
            break
    
while True:
    
    main()
pygame.quit()