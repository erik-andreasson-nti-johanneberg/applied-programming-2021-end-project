import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 625
WINDOW_WIDTH = 1250
num_cells_width = 50
num_cells_height = 25


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    # Check if the rect collides with the mouse pos.
                    blockSize = 25
                    for x in range(0, WINDOW_WIDTH, blockSize):
                        for y in range(0, WINDOW_HEIGHT, blockSize):
                            rect = pygame.Rect(x, y, blockSize, blockSize)
                            if rect.collidepoint(event.pos):
                                print('Area clicked.')
                                pygame.draw.rect(SCREEN, WHITE, (50, 50, 100, 100))

        pygame.display.update()


def drawGrid():
    blockSize = 25 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

main()