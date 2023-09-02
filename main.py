import pygame
from sprites.cloud import Cloud
from sprites.enemies import Stump
import random

pygame.init()

WINDOW_WIDTH = 1700
WINDOW_HEIGHT= 900
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption("Njoro The Explorer")

# background
bg = pygame.image.load('assets/images/jungle.jpg')
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        self.w = 120
        self.h = 200
        self.speed_x = 8.5
        self.speed_y = 0
        self.direction = 0 # 0 = not moving, 1 = move right, -1 = move left
        self.is_jumping = False
        self.max_jump_height = 1000
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid1.png'), (self.w, self.h) ))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid2.png'), (self.w, self.h)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid3.png'), (self.w, self.h)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid4.png'), (self.w, self.h)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid5.png'), (self.w, self.h)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/images/player/walking/kid6.png'), (self.w, self.h)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topright = [WINDOW_WIDTH/3, WINDOW_HEIGHT - self.rect.height] 


    def update(self):
        " Update walk speed animation"
        if self.is_animating == True:
            self.current_sprite += 0.09
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.current_sprite = 0

    
    def animate(self):
        self.is_animating = True

    def move(self):
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

        
        if 0 <= horizontal_distance <= WINDOW_WIDTH - self.rect.width:
            self.rect.x = horizontal_distance

    def jump(self):
        keys = pygame.key.get_pressed()
        vertical_distance = self.rect.y
        
        if keys[pygame.K_UP] and not self.is_jumping:  # Check if not already jumping
            self.speed_y = -50  
            self.is_jumping = True

        if self.is_jumping:
            self.speed_y += gravity
            vertical_distance += self.speed_y

        if vertical_distance >= WINDOW_HEIGHT - self.rect.height:
            vertical_distance = WINDOW_HEIGHT - self.rect.height
            self.is_jumping = False  # Reset the jumping state

        self.rect.y = vertical_distance
        


running = True

clock = pygame.time.Clock()

# add stumps
ADDSTUMP = pygame.USEREVENT + 3
stump_time = random.randint(3000, 15000)
pygame.time.set_timer(ADDSTUMP, stump_time)
stumps = pygame.sprite.Group()

# add clouds
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1500)
clouds = pygame.sprite.Group()

gravity = 2
velocity_y = 10

i = 0

all_sprites = pygame.sprite.Group()
player = Player(300, 100)
all_sprites.add(player)
FPS = 100

while running:
    # run regardless
    screen.fill((0,0,0))
    screen.blit(bg, (i, 0))
    screen.blit(bg, (WINDOW_WIDTH + i, 0))
    if (i==-WINDOW_WIDTH):
        screen.blit(bg,(WINDOW_WIDTH+i,0))
        i=0
    i-=2
    player.animate()
    # end run regardless

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == ADDSTUMP:
            new_stump = Stump(WINDOW_WIDTH, WINDOW_HEIGHT)
            stumps.add(new_stump)
            all_sprites.add(new_stump)
            print(stump_time)


        elif event.type == ADDCLOUD:
            new_cloud = Cloud(WINDOW_WIDTH, WINDOW_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # if keys[pygame.K_RIGHT]:
    #     screen.fill((0,0,0))
    #     screen.blit(bg, (i, 0))
    #     screen.blit(bg, (WINDOW_WIDTH + i, 0))
    #     if (i==-WINDOW_WIDTH):
    #         screen.blit(bg,(WINDOW_WIDTH+i,0))
    #         i=0
    #         print("Right key pressed")
    #     i-=2
    #     player.animate(
   
    player.move()
    player.jump()
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()