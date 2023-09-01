import pygame
pygame.init()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT= 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption("Explorer")

bg = pygame.image.load('assets/images/jungle.jpg')
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
# bg_rect = bg.get_rect()
# bg_x = (WINDOW_WIDTH - bg_rect.width ) // 2
# bg_y = (WINDOW_HEIGHT - bg_rect.height ) // 2

running = True
i = 0
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



    pygame.display.update()

pygame.quit()