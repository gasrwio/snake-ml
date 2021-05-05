import pygame
import sys

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake')

    x1 = 300
    y1 = 300
    x1_change = 0       
    y1_change = 0
     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
     
        x1 += x1_change
        y1 += y1_change
        display.fill(pygame.Color('gray13'))
        pygame.draw.rect(display, pygame.Color('green'), [x1, y1, 10, 10])
        pygame.display.update()
        clock.tick(30)
 
