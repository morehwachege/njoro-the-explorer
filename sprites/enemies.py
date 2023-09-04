import pygame
import random

class Stump(pygame.sprite.Sprite):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        super(Stump, self).__init__()
        self.image = pygame.image.load("./assets/images/enemy/stump.png").convert_alpha()
        self.image.set_colorkey((0,0,0), pygame.RLEACCEL)
        self.image = pygame.transform.scale(self.image, (200, 150))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [WINDOW_WIDTH, WINDOW_HEIGHT] 

    def update(self):
        self.rect.move_ip(-4, 0)
        if self.rect.right < 0:
            self.kill()