import pygame
from sprites.cloud import Cloud
from sprites.enemies import Stump
from sprites.player import Player
import random

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
stump_time = random.randint(3000, 15000)
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
FPS = 100

while running:
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

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == ADDSTUMP:
            new_stump = Stump(WINDOW_WIDTH, WINDOW_HEIGHT)
            stumps.add(new_stump)
            all_sprites.add(new_stump)
            print(stump_time)


        elif event.type == ADDCLOUD:
            new_cloud = Cloud(WINDOW_WIDTH, WINDOW_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # if keys[pygame.K_RIGHT]:
    #     screen.fill((0,0,0))
    #     screen.blit(bg, (i, 0))
    #     screen.blit(bg, (WINDOW_WIDTH + i, 0))
    #     if (i==-WINDOW_WIDTH):
    #         screen.blit(bg,(WINDOW_WIDTH+i,0))
    #         i=0
    #         print("Right key pressed")
    #     i-=2
    #     player.animate(
   
    player.move()
    player.jump(gravity)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()