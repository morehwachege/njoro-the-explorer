import pygame
pygame.init()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT= 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption("Njoro The Explorer")

# background
bg = pygame.image.load('assets/images/jungle.jpg')
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

njoro = pygame.image.load("./assets/images/player/walking/kid2.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = njoro  # Use the loaded sprite image
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2) 

running = True
i = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_RIGHT]:
        screen.fill((0,0,0))
        screen.blit(bg, (i, 0))
        screen.blit(bg, (WINDOW_WIDTH + i, 0))
        if (i==-WINDOW_WIDTH):
            screen.blit(bg,(WINDOW_WIDTH+i,0))
            i=0
            print("Right key pressed")
        i-=5
    all_sprites.update()

    all_sprites.draw(screen)




    pygame.display.update()

pygame.quit()