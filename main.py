import pygame
import math
import random
from player import Player
from enemy import Hydrogen_bomb
from enemy import LandMine
from enemy import Atk_Chopper
pygame.init()

# Variables
WHITE = (255,255,255)
RED = (255,0,0)
clock = pygame.time.Clock()
fps = 15
score = 0
lastPointTicks = 0
oldticks = 0
start = 0



# Allow main loop to run
run = True


# Creates Screen 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Best Game Ever")
screen.fill(WHITE)

# Create Background
bg = pygame.image.load("assets/images/dino_bg.png")
bg_width = bg.get_width()
scroll = 0
tiles = math.ceil(SCREEN_WIDTH/ bg_width) + 1


# Create Player
player = Player(105, 480)

# Create Hydrogen bomb
hydro_bomb = Hydrogen_bomb(random.randint(350, 500), random.randint(300, 500))

# Create landmine
landmine = LandMine(random.randint(300,500), 500)

#create chopper
atk_Chopper = Atk_Chopper(500, 20)

# All sprites
all_sprites_list = pygame.sprite.Group()

player.draw(screen)
hydro_bomb.draw(screen)
landmine.draw(screen)
atk_Chopper.draw(screen)
all_sprites_list.add(atk_Chopper)
all_sprites_list.add(landmine)
all_sprites_list.add(player)
all_sprites_list.add(hydro_bomb)

while run:
    # Keeps the game running at a maximun of 60 fps
    clock.tick(fps)

    # Draw Background
    for i in range(0, tiles):
        screen.blit(bg, (i*bg_width + scroll, 0))
    
    # Scroll background
    scroll -= 5
    
    # Reset scroll
    if abs(scroll) > bg_width:
        scroll = 0


    all_sprites_list.draw(screen)
    player.draw(screen, player.rect)
    # Holds the font that I will be using
    font = pygame.font.SysFont("vivaldi", 30)
    # Event go here ---------------
    # closes pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    # Gives the player a chance to look at screen
    if start == 0:
        text = font.render("Ready?", 100, (69,5,128))
        screen.blit(text, (SCREEN_WIDTH/2- 50, SCREEN_HEIGHT/2-50))
        pygame.display.update()
        pygame.time.wait(1000)
        start = 1

    # Move player
    player.move(SCREEN_HEIGHT)

    # Checks if hydrogen bomb hits border and redraws it
    # hydro_bomb.move(SCREEN_WIDTH)
    # if hydro_bomb.rect.left < 0:
    #     hydro_bomb.kill()
    #     hydro_bomb = Hydrogen_bomb(random.randint(200, 500), random.randint(300, 500))
    #     all_sprites_list.add(hydro_bomb)

    # Check if landmine hits edge and redraw
    # landmine.move(SCREEN_WIDTH)
    # if landmine.rect.left < 0:
    #     landmine.kill()
    #     landmine = LandMine(random.randint(300,500), 500)
    #     all_sprites_list.add(landmine)
    
    # atk_Chopper.move(SCREEN_WIDTH)


    
    # Create Collision
    # if pygame.sprite.collide_mask(hydro_bomb, player) or pygame.sprite.collide_mask(landmine, player):
    #     player.kill()
    #     # Draw Game Overn and quit pygame
    #     text = font.render("Game Over", 100, (255,0,0))
    #     screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    #     pygame.display.update()
    #     pygame.time.wait(2000)
    #     run = False


    

    # Add score
    # Keeps track of the score
    ticks = pygame.time.get_ticks()
    if (ticks - lastPointTicks) > 500:
        score += 1
        lastPointTicks = ticks
    # Draw Score
    
    text = font.render("Score: " + str(score), 1, (69,5,128))
    screen.blit(text, (50, 10))

    # update display
    pygame.display.update()



# Exits pygame
pygame.quit()