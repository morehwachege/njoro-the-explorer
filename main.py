import pygame
from sprites.cloud import Cloud
from sprites.enemies import Stump
from sprites.player import Player
import random
import sys

pygame.init()

WINDOW_WIDTH = 1700
WINDOW_HEIGHT= 900
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption("Njoro The Explorer")

# background
bg = pygame.image.load('assets/images/jungle.jpg')
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
     


running = True

clock = pygame.time.Clock()

# add stumps
ADDSTUMP = pygame.USEREVENT + 3
# stump_time = random.randint(3000, 15000)
stump_time = 7000
pygame.time.set_timer(ADDSTUMP, stump_time)
stumps = pygame.sprite.Group()

# add clouds
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1500)
clouds = pygame.sprite.Group()

gravity = 2
velocity_y = 10

i = 0

all_sprites = pygame.sprite.Group()
player = Player(300, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
all_sprites.add(player)
FPS = 80

pause_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
crash_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
font = pygame.font.Font(None, 38)

def draw_pause():
    " Draw Pause Screen"
    pygame.draw.rect(pause_surface, (0, 0, 0, 20), [0, 0, WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.draw.rect(pause_surface, 'gray', [500, 150, 600, 50], 0, 10)
    save = pygame.draw.rect(pause_surface, 'dark green', [500, 400, 250, 60], 0, 15)
    quit_game = pygame.draw.rect(pause_surface, 'dark red', [850, 400, 250, 60], 0, 15)
    play = pygame.draw.rect(pause_surface, 'lime', [500, 500, 600, 60], 0, 15)

    pause_surface.blit(font.render('Game Paused: Space bar to resume', True, 'black'), (570, 160)) 
    pause_surface.blit(font.render('Save', True, 'black'), (600, 415))
    pause_surface.blit(font.render('Quit', True, 'white'), (950, 415))
    pause_surface.blit(font.render('Play', True, 'black'), (770, 515))

    screen.blit(pause_surface, (0, 0))
    return play

def crash():
    "Happens when player collides with enemy sprite"
    clock.tick(60)
    pygame.draw.rect(crash_surface, (0, 0, 0, 20), [0, 0, WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.draw.rect(crash_surface, 'gray', [500, 150, 600, 50], 0, 10)

    w = 120
    h = 200
    # crash_surface.blit 
    # reload_img = pygame.transform.scale(pygame.image.load('./assets/images/reload.png'), (w, h))
    play = pygame.draw.rect(crash_surface, 'lime', [500, 500, 600, 60], 0, 15)
    screen.blit(crash_surface, (0, 0))
    print(clock.get_fps(), "after")
    return play

paused = False
crashed = False

while running:
    if not paused and not crashed:
        # run regardless
        screen.fill((0,0,0))
        screen.blit(bg, (i, 0))
        screen.blit(bg, (WINDOW_WIDTH + i, 0))
        if (i==-WINDOW_WIDTH):
            screen.blit(bg,(WINDOW_WIDTH+i,0))
            i=0
        i-=2
        player.animate()
        # end run regardless
    elif paused:
        play = draw_pause()


    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    paused = False 
                else:
                    paused = True

        if event.type == ADDSTUMP and not paused and not crashed:
            new_stump = Stump(WINDOW_WIDTH, WINDOW_HEIGHT)
            stumps.add(new_stump)
            all_sprites.add(new_stump)
            # print(stump_time)


        if event.type == ADDCLOUD and not paused and not crashed:
            new_cloud = Cloud(WINDOW_WIDTH, WINDOW_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        if event.type == pygame.MOUSEBUTTONDOWN and paused and not crashed:
            if play.collidepoint(event.pos):
                paused = False
            pass

        if pygame.sprite.spritecollideany(player, stumps):
            paused = False
            crashed = True
            # print("Collision detected boom!")
            # sys.exit()
            play = crash()

    if not paused and not crashed:
        player.move()
        player.jump(gravity)
        all_sprites.update()
        all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()