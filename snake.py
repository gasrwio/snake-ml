import pygame
import sys

x_cord = 300
y_cord = 200

x_change = 0
y_change = 0

class Snake():
    def __init__(self):
        self.height = 10
        self.width = 10 

    def Draw(self, screen, x, y):
        self.shape = pygame.Rect((x, y), (self.height, self.width))
        pygame.draw.rect(screen, pygame.Color("blue"), self.shape)

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((600, 400))

    snake = Snake()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = +10
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = +10
                    y_change = 0

        x_cord += x_change
        y_cord += y_change
        snake.Draw(screen, x_cord, y_cord)
        pygame.display.update()
        screen.fill(pygame.Color("gray13"))
        clock.tick(15)
