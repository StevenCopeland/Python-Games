import pygame, sys, time, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 1250
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds')

# Set up the colors.
WHITE = (255, 255, 255)

# Set up the block data structure.
player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage,(40, 40))
foodImage = pygame.image.load('cherry2.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

foodCounter = 0
NEWFOOD = 40

# Set up keyboard variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 8

# Set up the music.
pickUpSound = pygame.mixer.Sound('bang.wav')
pygame.mixer.music.load('Rynos Theme.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_n:
                foodImage = pygame.image.load('apple.png')
                print(foodImage)
                """if foodImage == pygame.image.load('cherry2.png'):
                    foodImage = pygame.image.load('apple.png')
                elif foodImage == pygame.image.load('apple.png'):
                    foodImage = pygame.image.load('cherry2.png')
                else:
                    print('Error!')"""
            if event.key == K_c:
                foodImage = pygame.image.load('cherry2.png')
                print(foodImage)
            if event.key == K_l:
                foodImage = pygame.image.load('lemon.png')
                print(foodImage)
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move the player.
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
        
    # Draw the block onto the surface.
    windowSurface.blit(playerStretchedImage, player)
    
    # Check whether the block has intersected with and food squares.
    if foodImage == '<Surface(63x71x24 SW)>':
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
                player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
                playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
                if musicPlaying:
                    pickUpSound.play()
    elif foodImage == '<Surface(41x54x24 SW)>':
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
                player = pygame.Rect(player.left, player.top, player.width + 4, player.height + 4)
                playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
                if musicPlaying:
                    pickUpSound.play()
    elif foodImage == '<Surface(30x38x24 SW)>':
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
                player = pygame.Rect(player.left, player.top, player.width + 6, player.height + 6)
                playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
                if musicPlaying:
                    pickUpSound.play()
    else:
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
                player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
                playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
                if musicPlaying:
                    pickUpSound.play()
    
    # Draw the food.
    for food in foods:
        windowSurface.blit(foodImage, food)
    
    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(70)
