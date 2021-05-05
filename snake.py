import pygame
import sys

if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((400, 300))
    for events in pygame.events.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill((255, 255, 255))
    pygame.display.flip()
