import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 625
WINDOW_WIDTH = 1250
num_cells_width = 50
num_cells_height = 25


def drawGrid():
    blockSize = 25 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def menu():
    running = True
    while running:    
        chad_myra = pygame.Rect(500, 200, 50, 50)
        beta_myra = pygame.Rect(500, 500, 50, 50)

        pygame.draw.rect(SCREEN, WHITE, (chad_myra))
        pygame.draw.rect(SCREEN, WHITE, (beta_myra))

        if chad_myra.collidepoint((pygame.mouse.get_pos())):
            pygame.draw.rect(SCREEN, WHITE, (250, 250))

        if beta_myra.collidepoint((pygame.mouse.get_pos())):
            pygame.draw.rect(SCREEN, WHITE, (350, 350))
        pygame.display.update()
        CLOCK.tick(60)

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
        pygame.draw.rect(SCREEN, WHITE, 100, 100)

        pygame.display.update()

        ev = pygame.event.get()
        for event in ev:
            if  event.type == pygame.MOUSEBUTTONDOWN:
                barrack = pygame.Rect(100, 100, 50, 50)
                pygame.draw.rect(SCREEN, WHITE, (barrack))
                if barrack.collidepoint((pygame.mouse.get_pos())):
                    menu()
                    print("hi")
        

    #skapa en funktion som tar upp en meny






main()