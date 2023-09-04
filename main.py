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





font = pygame.font.Font(None, 38)

# def draw_pause(screen, WINDOW_WIDTH, WINDOW_HEIGHT):
    

def crash(font):
    pass

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
    game_state.crashed(font)

    clock.tick(FPS)

pygame.quit()