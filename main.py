import pygame
from sprites.cloud import Cloud
from sprites.enemies import Stump
from sprites.player import Player
from sprites.gameplay import GameState
import random
import sys

pygame.init()

WINDOW_WIDTH = 1700
WINDOW_HEIGHT= 900
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption("Njoro The Explorer")



running = True

clock = pygame.time.Clock()





velocity_y = 10





crash_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
font = pygame.font.Font(None, 38)

# def draw_pause(screen, WINDOW_WIDTH, WINDOW_HEIGHT):
    

def crash():
    "Happens when player collides with enemy sprite"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(60)
    pygame.draw.rect(crash_surface, (0, 0, 0, 20), [0, 0, WINDOW_WIDTH, WINDOW_HEIGHT])
    message = pygame.draw.rect(crash_surface, 'gray', [500, 150, 600, 50], 0, 10)
    crash_surface.blit(font.render('You crashed! Click reload to try again', True, 'black'), (550, 162))

    w = 200
    h = 200
    # crash_surface.blit 
    reload_img = pygame.transform.scale(pygame.image.load('./assets/images/reload.png'), (w, h))
    reload_img_rect = reload_img.get_rect()
    replay = pygame.draw.rect(crash_surface, 'orange', [650, 500, 200, 60], 0, 15)
    crash_surface.blit(font.render('Replay', True, 'black'), (700, 515))
    screen.blit(crash_surface, (0, 0))
    # reload image
    screen.blit(reload_img, ((WINDOW_WIDTH / 2) - reload_img.get_width(), (WINDOW_HEIGHT / 2) - reload_img.get_height()))
    pygame.display.update()
    return replay

paused = False
crashed = False
FPS = 80

game_state = GameState(screen, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)

while running:
    game_state.main_game()
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         sys.exit()
    # draw_pause(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
    # game_state.game_paused(font)
    # crash()

    clock.tick(FPS)

pygame.quit()