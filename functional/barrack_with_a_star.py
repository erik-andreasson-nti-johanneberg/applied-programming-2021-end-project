from numpy import blackman
import pygame
import sys
import random
import time
from functional.a_star_pure import astar
pygame.init()

CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WINDOW_HEIGHT = 625
WINDOW_WIDTH = 1250
num_cells_width = 50
num_cells_height = 25
blockSize = 25
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Global fonts
barrack_font = pygame.font.Font('freesansbold.ttf', 32)
menu_font = pygame.font.Font('freesansbold.ttf', 30)

#barracks class
class Barrack():
    def __init__(self, position=None, rect=None):
        self.position = position
        self.rect = rect

#ant class
class Ant():
    def __init__(self, position=None, rect=None):
        self.position = position
        self.rect = rect

#Draws text to the screen. Must be called after the backdrop menu has been drawn to the screen
def draw_text(text, font, text_color, background_color, surface, x, y):
    textobj = font.render(text, True, text_color, background_color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def drawGrid(map):
    blockSize = 25 #Set the size of the grid block
    for index_x, x in enumerate(range(0, WINDOW_WIDTH, blockSize)):
        for index_y, y in enumerate(range(0, WINDOW_HEIGHT, blockSize)):
            if map[index_x][index_y] == 1:
                rect = pygame.Rect(y, x, blockSize, blockSize)
                rect2 = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, BLUE, rect)
                pygame.draw.rect(SCREEN, WHITE, rect2, 1)
            else:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)

#removes the menu from the screen and redraws all buildings and ants
def remove_menu(ants, building_list):
    replace_with_black_rect = pygame.Rect(75, 75, 1100, 475)
    pygame.draw.rect(SCREEN, BLACK, replace_with_black_rect)
    for building in building_list:
        building_rect = pygame.Rect(building.position[0]*25, building.position[1]*25, 50, 50)
        pygame.draw.rect(SCREEN, WHITE, building_rect)
    for ant in ants:
        ant_rect = pygame.Rect(ant.position[0]*25, ant.position[1]*25, blockSize, blockSize)
        pygame.draw.rect(SCREEN, RED, ant_rect)
    
#Menus
# barrack_menu    
def menu(ants, buildings):
    # Menu screen
    menu_rect = pygame.Rect(75, 75, 1100, 475)
    pygame.draw.rect(SCREEN, BLUE, (menu_rect))
    #Button text
    #Chad myra
    draw_text('Chadmyra', barrack_font, RED, BLACK, SCREEN, 825, 300)
    #beta myra
    draw_text('Betamyra', barrack_font, RED, BLACK, SCREEN, 425, 300)
    selected = False
    while True:
        if selected:
            break
        chad_myra_button = pygame.Rect(800, 200, 50, 50)
        beta_myra_button = pygame.Rect(400, 200, 50, 50)
        position_chad_myra = [8,8]
        position_beta_myra = [20,4]
        chad_myra_rect = pygame.Rect(position_chad_myra[1]*25, position_chad_myra[0]*25, blockSize, blockSize)
        beta_myra_rect = pygame.Rect(position_beta_myra[1]*25, position_beta_myra[0]*25, blockSize, blockSize)

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
                        remove_menu(ants, buildings)
                        chad_myra = Ant(position_chad_myra, chad_myra_rect)
                        ants.append(chad_myra)
                        pygame.draw.rect(SCREEN, BLUE, (chad_myra_rect))
                        selected = True
                        break
                    if beta_myra_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants, buildings)
                        beta_myra = Ant(position_beta_myra, beta_myra_rect)
                        ants.append(beta_myra)
                        pygame.draw.rect(SCREEN, RED, (beta_myra_rect))
                        selected = True
                        break
        pygame.display.update()
# main menu
def main_menu():
    SCREEN.fill((0,0,0))
    draw_text('Main Menu', menu_font, WHITE, BLACK, SCREEN, WINDOW_WIDTH // 2, 50)
    while True:
        mx, my = pygame.mouse.get_pos()
 
        menu_button_1 = pygame.Rect(0, 0, 200, 50)
        menu_button_2 = pygame.Rect(0, 0, 200, 50)
        menu_button_3 = pygame.Rect(0, 0, 200, 50)
        menu_button_1.center = (WINDOW_WIDTH // 2, 100)
        menu_button_2.center = (WINDOW_WIDTH // 2, 175)
        menu_button_3.center = (WINDOW_WIDTH // 2, 500)
        if menu_button_1.collidepoint((mx, my)):
            if click:
                main()
        # if menu_button_2.collidepoint((mx, my)):
        #     if click:
        #         options()
        if menu_button_3.collidepoint((mx, my)):
            if click:
                quit()
        pygame.draw.rect(SCREEN, BLUE, menu_button_1)
        draw_text('Game', menu_font, WHITE, BLUE, SCREEN, WINDOW_WIDTH // 2, 100)
        pygame.draw.rect(SCREEN, GREEN, menu_button_2)
        draw_text('Options', menu_font, WHITE, GREEN, SCREEN, WINDOW_WIDTH // 2, 175)
        pygame.draw.rect(SCREEN, RED, menu_button_3)
        draw_text('Quit', menu_font, WHITE, RED, SCREEN, WINDOW_WIDTH // 2, 500)
 
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(60)

def barrack_():
    position = [4,4]
    barrack = pygame.Rect(position[1]*blockSize, position[0]*blockSize, 50, 50)
    pygame.draw.rect(SCREEN, WHITE, (barrack))
    barrack = Barrack(position, barrack)
    return barrack

def removeant(cord):
    antsize = 25
    removeant = pygame.Rect(cord[1], cord[0], antsize, antsize)
    pygame.draw.rect(SCREEN, BLACK, removeant)
    pygame.display.update()

def drawant(cord): #draws a red rectangle for the ant
    antsize = 25
    ant = pygame.Rect(cord[1], cord[0], antsize, antsize)
    pygame.draw.rect(SCREEN, RED, ant)

def gridpath(path):
    grid_path = []
    for cord in path:
        # print('cord in gridpath:')
        # print(cord)
        new_cord = []
        x = 25*cord[0]
        y = 25*cord[1]
        new_cord.append(x)
        new_cord.append(y)
        grid_path.append(new_cord)
    return grid_path

def main():
    global SCREEN, CLOCK
    SCREEN.fill(BLACK)
    barrack = barrack_()
    ant_already_clicked = False
    ants = []
    buildings = [barrack]
    while True:
        drawGrid(map)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    # Check if the barrack collides with the mouse pos.
                    if barrack.rect.collidepoint((pygame.mouse.get_pos())):
                        menu(ants, buildings)
                    if ant_already_clicked:
                        prev_cord = [-25,-25]
                        ant_already_clicked = False
                        mouse_position = pygame.mouse.get_pos()
                        # print(mouse_position)
                        column, r1 = divmod(mouse_position[0],25)
                        row, r2 = divmod(mouse_position[1],25)
                        end = (row, column)
                        print(end)
                        print(current_ant.position)
                        path = astar(current_ant.position,end,map)
                        print(path)
                        grid_path = gridpath(path)
                        print(grid_path)

                        for cord in grid_path:
                            print(cord)
                            drawGrid(map)
                            time.sleep(0.5)
                            removeant(prev_cord)
                            prev_cord = cord
                            drawant(cord)
                            pygame.display.update()
                        ant = pygame.Rect(end[1]*25, end[0]*25, blockSize, blockSize)
                        current_ant.rect = ant
                        current_ant.position = end
                        print(current_ant.rect)
                        print(current_ant.position)
                        continue
        
                    if len(ants) != 0:
                        for ant in ants:
                            if ant.rect.collidepoint(pygame.mouse.get_pos()):
                                print("Mouse clicked on the ant")
                                current_ant = ant
                                ant_already_clicked = True
                                break

        pygame.display.update()

main_menu()