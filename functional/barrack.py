from tarfile import BLOCKSIZE
import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0,0,255)
RED = (255,0,0)
WINDOW_HEIGHT = 625
WINDOW_WIDTH = 1250
num_cells_width = 50
num_cells_height = 25
blockSize = 25

#barracks class
class Barrack():
    def __init__(self, position=None, rect=None):
        self.position = position
        self.rect = rect

#ant class
class Ant():
    #ant class
    def __init__(self, position=None, rect=None):
        self.position = position
        self.rect = rect




def drawGrid():
    blockSize = 25 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def remove_menu(button_list):
    for button in button_list:
        replace_with_black_rect = pygame.Rect(button[0], button[1], button[2], button[2])
        pygame.draw.rect(SCREEN, BLACK, replace_with_black_rect)
        num_of_rects = button[2]/blockSize
        i = 0
        while i < num_of_rects/2:
            draw_over_rect = pygame.Rect((button[0]+i*blockSize, button[1], blockSize, blockSize))
            pygame.draw.rect(SCREEN, WHITE, draw_over_rect, 1)
            i += 1
        i = 0
        while i < num_of_rects/2:
            draw_over_rect = pygame.Rect((button[0], button[1]+i*blockSize, blockSize, blockSize))
            pygame.draw.rect(SCREEN, WHITE, draw_over_rect, 1)
            i += 1
    


def menu():
    selected = False
    while True:
        if selected:
            break
        chad_myra_button = pygame.Rect(500, 200, 50, 50)
        beta_myra_button = pygame.Rect(500, 500, 50, 50)
        position_chad_myra = [8,8]
        position_beta_myra = [4,20]
        chad_myra_rect = pygame.Rect(position_chad_myra[0]*25, position_chad_myra[1]*25, blockSize, blockSize)
        beta_myra_rect = pygame.Rect(position_beta_myra[0]*25, position_beta_myra[1]*25, blockSize, blockSize)

        pygame.draw.rect(SCREEN, WHITE, (chad_myra_button))
        pygame.draw.rect(SCREEN, WHITE, (beta_myra_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    if chad_myra_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu([[500, 200, 50], [500, 500, 50]])
                        chad_myra = Ant(position_chad_myra, chad_myra_rect)
                        pygame.draw.rect(SCREEN, BLUE, (chad_myra_rect))
                        selected = True
                        break
                    if beta_myra_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu([[500, 500, 50], [500, 200, 50]])
                        beta_myra = Ant(position_beta_myra, beta_myra_rect)
                        pygame.draw.rect(SCREEN, RED, (beta_myra_rect))
                        selected = True
                        break
        pygame.display.update()

def barrack_():
    position = [4,4]
    barrack = pygame.Rect(position[0]*blockSize, position[1]*blockSize, 50, 50)
    pygame.draw.rect(SCREEN, WHITE, (barrack))
    barrack = Barrack(position, barrack)
    return barrack

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    barrack = barrack_()
    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    # Check if the barrack collides with the mouse pos.
                    if barrack.rect.collidepoint((pygame.mouse.get_pos())):
                        menu()

        pygame.display.update()
        

    #skapa en funktion som tar upp en meny






main()