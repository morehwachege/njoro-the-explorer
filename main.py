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

font = pygame.font.Font(None, 38)
FPS = 80

game = GameState(screen, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)

while running:
    # game.state_manager(font)
    game.intro(font)
    clock.tick(FPS)

pygame.quit()