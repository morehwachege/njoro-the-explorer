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
    clock.tick(60)
    pygame.draw.rect(crash_surface, (0, 0, 0, 20), [0, 0, WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.draw.rect(crash_surface, 'gray', [500, 150, 600, 50], 0, 10)

    w = 120
    h = 200
    # crash_surface.blit 
    # reload_img = pygame.transform.scale(pygame.image.load('./assets/images/reload.png'), (w, h))
    play = pygame.draw.rect(crash_surface, 'lime', [500, 500, 600, 60], 0, 15)
    screen.blit(crash_surface, (0, 0))
    pygame.display.update()

    print(clock.get_fps(), "after")
    return play

paused = False
crashed = False
FPS = 80

game_state = GameState(screen, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)

while running:
    # game_state.main_game()
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         sys.exit()
    # draw_pause(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
    game_state.game_paused(font)

    clock.tick(FPS)

pygame.quit()