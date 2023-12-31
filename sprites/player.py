import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, WINDOW_WIDTH, WINDOW_HEIGHT):
        super().__init__()
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.is_animating = False
        self.sprites = []
        self.w = 120
        self.h = 200
        self.speed_x = 8.5
        self.speed_y = 0
        self.direction = 0 # 0 = not moving, 1 = move right, -1 = move left
        self.is_jumping = False
        self.max_jump_height = 1000

        self.walking_sprites = [
            pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid1.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid2.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid3.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid4.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid5.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid6.png'), (self.w, self.h))
        ]

        self.jumping_sprites = [
            pygame.transform.scale(pygame.image.load('./assets/images/player/jumping/kid1.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/jumping/kid2.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/jumping/kid3.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/jumping/kid4.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/jumping/kid5.png'), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load('./assets/images/player/jumping/kid6.png'), (self.w, self.h)),
        ]

        self.current_sprite = 0
        self.image = self.walking_sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topright = [self.WINDOW_WIDTH/3, self.WINDOW_HEIGHT - self.rect.height] 
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        " Update walk speed animation"
        keys = pygame.key.get_pressed()
        if self.is_animating == True:
            self.current_sprite += 0.05
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.current_sprite = 0

    
    def animate(self):
        self.is_animating = True

    def move(self):
        """Move/walk forward/backwards """
        self.sprites = self.walking_sprites
        self.update()
        keys = pygame.key.get_pressed()
        horizontal_distance = self.rect.x
        if keys[pygame.K_LEFT]:
            horizontal_distance -= self.speed_x
            self.direction = -1
        elif keys[pygame.K_RIGHT]:
            horizontal_distance += self.speed_x
            self.direction = 1
        else:
            self.direction = 0

        # this willl stop the sprite
        # if self.direction == 0:
        #     self.is_animating = False

        
        if 0 <= horizontal_distance <= self.WINDOW_WIDTH - self.rect.width:
            self.rect.x = horizontal_distance

    def jump(self, gravity):
        """ 
            Player sprite jump
        """
        vertical_distance = self.rect.y
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] and not self.is_jumping:  # Check if not already jumping
            self.speed_y = -50  
            self.is_jumping = True

        if self.is_jumping:
            self.sprites = self.jumping_sprites
            self.update()
            self.speed_y += gravity
            vertical_distance += self.speed_y

        if vertical_distance >= self.WINDOW_HEIGHT - self.rect.height:
            vertical_distance = self.WINDOW_HEIGHT - self.rect.height
            self.is_jumping = False  # Reset the jumping state

        self.rect.y = vertical_distance 


    def update_mask(self):
        """Update the mask when the image changes (e.g., during animation)"""
        self.mask = pygame.mask.from_surface(self.image)