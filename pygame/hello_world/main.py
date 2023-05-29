import sys

import pygame
from pygame.locals import QUIT

pygame.init()

window_size = (400, 300)
display_surface = pygame.display.set_mode(window_size)
pygame.display.set_caption("Hello World!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
