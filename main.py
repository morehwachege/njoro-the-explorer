import pygame
from sprites.cloud import Cloud
from sprites.enemies import Stump
from sprites.player import Player
from sprites.gameplay import GameState
import random
import sys
import time
from screeninfo import get_monitors

pygame.init()

for screen in get_monitors():
    if screen.is_primary:
        WINDOW_WIDTH = screen.width - 100
        WINDOW_HEIGHT = screen.height - 200

# WINDOW_WIDTH = 1800 # screen size minus 120
# WINDOW_HEIGHT= 880 # screen size minus 200 

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption("Njoro The Explorer")

running = True

clock = pygame.time.Clock()

font = pygame.font.Font(None, 38)
FPS = 100

game = GameState(screen, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)

while running:
    # game.intro(font)
    # time.sleep(2)
    game.state_manager(font)

    clock.tick(FPS)

pygame.quit()