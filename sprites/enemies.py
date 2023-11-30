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
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Move the stump based on a constant speed. Remove it when it passes the left edge of the screen"""
        self.rect.move_ip(-4, 0)
        if self.rect.right < 0:
            self.kill()

    def update_mask(self):
        """Update the mask when the image changes (e.g., during animation)"""
        self.mask = pygame.mask.from_surface(self.image)