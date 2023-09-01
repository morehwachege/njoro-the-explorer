import pygame
pygame.init()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT= 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption("Njoro The Explorer")

# background
bg = pygame.image.load('assets/images/jungle.jpg')
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

# njoro = pygame.image.load("./assets/images/player/walking/kid2.png")
# njoro = pygame.transform.scale(njoro, (150, 240))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        self.w = 120
        self.h = 200
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
        if self.is_animating == True:
            self.current_sprite += 0.1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.current_sprite = 0

    
    def animate(self):
        self.is_animating = True

running = True
i = 0

all_sprites = pygame.sprite.Group()
player = Player(300, 100)
all_sprites.add(player)

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_UP:
            if event.key == K_RIGHT:
                player.update()

    if keys[pygame.K_RIGHT]:
        screen.fill((0,0,0))
        screen.blit(bg, (i, 0))
        screen.blit(bg, (WINDOW_WIDTH + i, 0))
        if (i==-WINDOW_WIDTH):
            screen.blit(bg,(WINDOW_WIDTH+i,0))
            i=0
            print("Right key pressed")
        i-=2
        player.animate()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()