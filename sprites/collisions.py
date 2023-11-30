import pygame 

def detect_collision(sprite1, sprite2):
    [mask1, rect1] = sprite1
    [mask2, rect2] = sprite2
    overlap = mask1.overlap(mask2, (int(rect2.x - rect1.x), int(rect2.y - rect1.y)))
    if overlap:
        return True
    else:
        return False


