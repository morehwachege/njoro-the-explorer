import random
import pygame

class Apple(pygame.sprite.Sprite):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        super(Apple, self).__init__()
        self.image = pygame.image.load("./assets/images/fruits/apple.png").convert()
        self.image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        # self.image.transform.scale()
        self.image = pygame.transform.scale(self.image, (55, 60))
        # Generate the starting position randomly 
        self.rect = self.image.get_rect(
            center=(
                random.randint(WINDOW_WIDTH + 20, WINDOW_WIDTH + 100),
                random.randint(100, WINDOW_HEIGHT/4),
            )
        )

    def update(self):
        """Move the apple based on a constant speed. Remove it when it passes the left edge of the screen"""
        self.rect.move_ip(-4.8, 0)
        if self.rect.right < 0:
            self.kill()

