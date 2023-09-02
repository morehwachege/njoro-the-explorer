import random
import pygame

class Cloud(pygame.sprite.Sprite):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        super(Cloud, self).__init__()
        self.image = pygame.image.load("./assets/images/cloud.png").convert()
        self.image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        # self.image.transform.scale()
        self.image = pygame.transform.scale(self.image, (150, 100))
        # Generate the starting position randomly 
        self.rect = self.image.get_rect(
            center=(
                random.randint(WINDOW_WIDTH + 20, WINDOW_WIDTH + 100),
                random.randint(0, WINDOW_HEIGHT/4),
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

