import pygame
from sprites.cloud import Cloud
from sprites.enemies import Stump
from sprites.player import Player
from sprites.gameplay import GameState
import random
import sys
import time

pygame.init()

WINDOW_WIDTH = 1500
WINDOW_HEIGHT= 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption("Njoro The Explorer")

running = True

clock = pygame.time.Clock()

font = pygame.font.Font(None, 38)
FPS = 80

game = GameState(screen, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)

while running:
    # game.intro(font)
    # time.sleep(2)
    game.state_manager(font)

    clock.tick(FPS)

pygame.quit()