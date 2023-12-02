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




class Hawk(pygame.sprite.Sprite):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        super().__init__()
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.is_animating = True
        self.w = 120
        self.h = 130

        self.sprites = [
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk1.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk2.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk3.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk4.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk5.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk6.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk7.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk8.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/enemy/hawk/hawk9.png'), (self.w, self.h)),
        ]

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        # self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(
            center=(
                random.randint(WINDOW_WIDTH + 20, WINDOW_WIDTH + 100),
                random.randint(0, WINDOW_HEIGHT/4),
            )
        )
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        " Update walk speed animation"
        keys = pygame.key.get_pressed()
        if self.is_animating == True:
            self.current_sprite += .19
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.current_sprite = 0
            self.is_animating = True
        self.rect.move_ip(-9, 0)
        if self.rect.right < 0:
            self.kill()



    def update_mask(self):
        """Update the mask when the image changes (e.g., during animation)"""
        self.mask = pygame.mask.from_surface(self.image)