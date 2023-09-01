import pygame
pygame.init()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT= 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
title = pygame.display.set_caption("Cool Game")

bg = pygame.image.load('assets/images/jungle.jpg')
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
# bg_rect = bg.get_rect()
# bg_x = (WINDOW_WIDTH - bg_rect.width ) // 2
# bg_y = (WINDOW_HEIGHT - bg_rect.height ) // 2

running = True
i = 0
while running:
    screen.fill((0,0,0))
    screen.blit(bg, (i, 0))
    screen.blit(bg, (WINDOW_WIDTH + i, 0))
    if (i==-WINDOW_WIDTH):
        screen.blit(bg,(WINDOW_WIDTH+i,0))
        i=0
    i-= 1
    for event in pygame.event.get():
        pass
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()