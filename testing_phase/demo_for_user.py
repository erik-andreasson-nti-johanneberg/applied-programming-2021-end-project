from turtle import position
from numpy import block
import pygame
import sys
import time
from functional.a_star_pure import astar
pygame.init()

CLOCK = pygame.time.Clock()
# Colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
GOLD = (255,215,0)
COPPER = (184, 115, 51)
ORANGE = (255,140,0)
MAGENTA = (255,0,255)
BROWN = (139,69,19)
VIOLET = (238,130,238)
# Screen sizes
WINDOW_HEIGHT = 625
WINDOW_WIDTH = 1250
num_cells_width = 50
num_cells_height = 25
blockSize = 25
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

# Global fonts
barrack_font = pygame.font.Font('freesansbold.ttf', 32)
menu_font = pygame.font.Font('freesansbold.ttf', 30)
next_turn_font = pygame.font.Font('freesansbold.ttf', 15)
info_bar_font = pygame.font.Font('freesansbold.ttf', 13)



#ant class
class Ant():
    def __init__(self, position=None, rect=None):
        self.position = position
        self.rect = rect

#builder ant
class Builder_ant():
    def __init__(self, position=None, rect=None, movement=2, hp=1, range=0, attack=0, color=VIOLET):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color

#beta ant
class Beta_ant():
    def __init__(self, position=None, rect=None, movement=5, hp=10, range=1, attack=5, color=RED):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color

#chad ant
class Chad_ant():
    def __init__(self, position=None, rect=None, movement=9, hp=5, range=1, attack=8, color=MAGENTA):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color

#sigma ant
class Sigma_ant():
    def __init__(self, position=None, rect=None, movement=7, hp=3, range=4, attack=4, color=BROWN):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color

#queen ant
class Queen_ant():
    def __init__(self, position=None, rect=None, movement=15, hp=20, range=2, attack=12, color=GREEN):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color

#resources class
class Resources():
    def __init__(self, gold=0, copper=0):
        self.gold = gold
        self.copper = copper

#hq class
class HQ():
    def __init__(self, position=None, rect=None, pr_storage=None, level=1, hp=4, armor=2, color=ORANGE, size=2):
        self.position = position
        self.rect = rect
        self.pr_storage = pr_storage
        self.level = level
        self.hp = hp
        self.armor = armor
        self.color = color
        self.size = size

#barracks class
class Barrack():
    def __init__(self, position=None, rect=None, level=1, hp=4, armor=2, color=WHITE, size=2):
        self.position = position
        self.rect = rect
        self.level = level
        self.hp = hp
        self.armor = armor
        self.color = color
        self.size = size

#gold mine class
class Gold_mine():
    def __init__(self, position=None, rect=None, tick=100, level=1, hp=4, armor=2, color=GOLD):
        self.position = position
        self.rect = rect
        self.tick = tick
        self.level = level
        self.hp = hp
        self.armor = armor
        self.color = color

#copper mine class
class Copper_mine():
    def __init__(self, position=None, rect=None, tick=200, level=1, hp=4, armor=2, color=COPPER, size=1):
        self.position = position
        self.rect = rect
        self.tick = tick
        self.level = level
        self.hp = hp
        self.armor = armor
        self.color = color
        self.size = size
        

class Wall():
    def __init__(self, position=None, rect=None, hp=10, armor=2):
        self.position = position
        self.rect = rect
        self.hp = hp
        self.armor = armor

class Turret():
    def __init__(self, position=None, rect=None, hp=5, armor=2, range=4, attack=4, level=1, color=GOLD, size=1):
        self.position = position
        self.rect = rect
        self.hp = hp
        self.armor = armor
        self.range = range
        self.attack = attack
        self.level = level
        self.color = color
        self.size = size
        

# ai_turn placeholder, will be moved to a seperate file
def ai_turn(resources, gold_buildings):
    for building in gold_buildings:
        resources.gold += building.tick
    print('')
    print(resources.gold)
    print(resources.copper)
    print('AI has made their turn')

#Draws text to the screen. Must be called after the backdrop menu has been drawn to the screen
def draw_text(text, font, text_color, background_color, surface, x, y):
    textobj = font.render(text, True, text_color, background_color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#Draws the grid and resource bar
def drawGrid(map, resources,message):
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
    draw_info_bar(resources,message)

def draw_info_bar(resources,message):
    info_bar = pygame.Rect(0,0, WINDOW_WIDTH, blockSize)
    pygame.draw.rect(SCREEN, BLUE, info_bar)
    draw_text('Gold: ' + str(resources.gold), info_bar_font, WHITE, BLUE, SCREEN, 50, blockSize/2)
    draw_text('Copper: ' + str(resources.copper), info_bar_font, WHITE, BLUE, SCREEN, 150, blockSize/2)
    draw_text(message, info_bar_font, WHITE, BLUE, SCREEN, WINDOW_WIDTH/2, blockSize/2)

def draw_movement_func(ant,map):
    print('we got here tho')
    blockSize = 25 #Set the size of the grid block
    for x in range((ant.position[1]-ant.movement)*blockSize, ant.position[1]*blockSize, blockSize):
        for y in range((ant.position[0]-ant.movement)*blockSize, ant.position[0]*blockSize, blockSize):
            if map[x/blockSize][y/blockSize] == 1:
                rect = pygame.Rect(y, x, blockSize, blockSize)
                rect2 = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, BLUE, rect)
                pygame.draw.rect(SCREEN, WHITE, rect2, 1)
            else:
                print('here as well')
                rect = pygame.Rect(y, x, blockSize, blockSize)
                pygame.draw.rect(SCREEN, RED, rect)

#removes the menu from the screen and redraws all buildings and ants
def remove_menu(ants, building_list):
    replace_with_black_rect = pygame.Rect(75, 75, 1100, 475)
    pygame.draw.rect(SCREEN, BLACK, replace_with_black_rect)
    for building in building_list:
        building_rect = pygame.Rect(building.position[1]*25, building.position[0]*25, building.size*25, building.size*25)
        pygame.draw.rect(SCREEN, building.color, building_rect)
    for ant in ants:
        ant_rect = pygame.Rect(ant.position[1]*25, ant.position[0]*25, blockSize, blockSize)
        pygame.draw.rect(SCREEN, ant.color, ant_rect)
    
#Menus
# barrack_menu    
def barrack_menu(building, ants, buildings):
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
        position_chad_myra = [building.position[0],building.position[1]+2]
        position_beta_myra = [building.position[0],building.position[1]+2]
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
                        chad_myra = Chad_ant(position_chad_myra, chad_myra_rect)
                        ants.append(chad_myra)
                        pygame.draw.rect(SCREEN, MAGENTA, (chad_myra_rect))
                        selected = True
                        break
                    if beta_myra_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants, buildings)
                        beta_myra = Beta_ant(position_beta_myra, beta_myra_rect)
                        ants.append(beta_myra)
                        pygame.draw.rect(SCREEN, RED, (beta_myra_rect))
                        selected = True
                        break
        pygame.display.update()

def hq_menu(building,ants,buildings):
    # Menu screen
    menu_rect = pygame.Rect(75, 75, 1100, 475)
    pygame.draw.rect(SCREEN, BLUE, (menu_rect))
    #Button text
    #Builder myra
    draw_text('Builder Myra', barrack_font, RED, BLACK, SCREEN, 825, 300)
    #beta myra
    draw_text('Queen Myra', barrack_font, RED, BLACK, SCREEN, 425, 300)
    selected = False
    while True:
        if selected:
            break
        builder_myra_button = pygame.Rect(800, 200, 50, 50)
        queen_myra_button = pygame.Rect(400, 200, 50, 50)
        position_builder_myra = [building.position[0],building.position[1]+2]
        position_queen_myra = [building.position[0],building.position[1]+2]
        builder_myra_rect = pygame.Rect(position_builder_myra[1]*25, position_builder_myra[0]*25, blockSize, blockSize)
        queen_myra_rect = pygame.Rect(position_queen_myra[1]*25, position_queen_myra[0]*25, blockSize, blockSize)

        pygame.draw.rect(SCREEN, WHITE, (builder_myra_button))
        pygame.draw.rect(SCREEN, WHITE, (queen_myra_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    if builder_myra_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants, buildings)
                        builder_ant = Builder_ant(position_builder_myra, builder_myra_rect)
                        ants.append(builder_ant)
                        pygame.draw.rect(SCREEN, builder_ant.color, (builder_myra_rect))
                        selected = True
                        break
                    if queen_myra_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants, buildings)
                        queen_ant = Queen_ant(position_queen_myra, queen_myra_rect)
                        ants.append(queen_ant)
                        pygame.draw.rect(SCREEN, queen_ant.color, (queen_myra_rect))
                        selected = True
                        break
        pygame.display.update()

def builder_menu(builder,ants,buildings):
    # Menu screen
    ants.remove(builder)
    builder_position = builder.position
    menu_rect = pygame.Rect(75, 75, 1100, 475)
    pygame.draw.rect(SCREEN, BLUE, (menu_rect))
    #Button text
    draw_text('Copper Mine', barrack_font, RED, BLACK, SCREEN, 825, 300)
    draw_text('Turret', barrack_font, RED, BLACK, SCREEN, 425, 300)
    draw_text('Barracks', barrack_font, RED, BLACK, SCREEN, 825, 500)
    selected = False
    while True:
        if selected:
            break
        copper_mine_button = pygame.Rect(800, 200, 50, 50)
        tower_button = pygame.Rect(400, 200, 50, 50)
        barracks_button = pygame.Rect(800,400,50,50)

        position_copper_mine = builder_position
        position_tower = builder_position
        position_barracks = builder_position

        copper_mine_rect = pygame.Rect(position_copper_mine[1]*25, position_copper_mine[0]*25, blockSize, blockSize)
        tower_rect = pygame.Rect(position_tower[1]*25, position_tower[0]*25, blockSize, blockSize)
        barracks_rect = pygame.Rect(position_barracks[1]*25, position_barracks[0]*25, 50, 50)

        pygame.draw.rect(SCREEN, WHITE, (copper_mine_button))
        pygame.draw.rect(SCREEN, WHITE, (tower_button))
        pygame.draw.rect(SCREEN, WHITE, (barracks_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    if copper_mine_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants, buildings)
                        mine = Copper_mine(position_copper_mine, copper_mine_rect)
                        buildings.append(mine)
                        pygame.draw.rect(SCREEN, mine.color, (tower_rect))
                        selected = True
                        break
                    if tower_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants, buildings)
                        turret = Turret(position_tower, tower_rect)
                        buildings.append(turret)
                        pygame.draw.rect(SCREEN, turret.color, (tower_rect))
                        selected = True
                        break
                    if barracks_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants, buildings)
                        barrack = Barrack(position_barracks, barracks_rect)
                        buildings.append(barrack)
                        pygame.draw.rect(SCREEN, barrack.color, (barracks_rect))
                        selected = True
                        break
        pygame.display.update()

def tower_menu(building,ants,buildings):
    # Menu screen
    menu_rect = pygame.Rect(75, 75, 1100, 475)
    pygame.draw.rect(SCREEN, BLUE, (menu_rect))
    #Button text
    draw_text('Level Up', barrack_font, RED, BLACK, SCREEN, 625, 462)
    selected = False
    while True:
        if selected:
            break
        level_up_button = pygame.Rect(600, 362, 50, 50)
        pygame.draw.rect(SCREEN, WHITE, (level_up_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    if level_up_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants, buildings)
                        building.level += 1
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

def hq_():
    position = [12,1]
    hq = pygame.Rect(position[1]*blockSize, position[0]*blockSize, 50, 50)
    pygame.draw.rect(SCREEN, ORANGE, hq)
    hq = HQ(position, hq)
    return hq

#old
def barrack_():
    position = [4,4]
    barrack = pygame.Rect(position[1]*blockSize, position[0]*blockSize, 50, 50)
    pygame.draw.rect(SCREEN, WHITE, (barrack))
    barrack = Barrack(position, barrack)
    return barrack

#old
def gold_mine_():
    position = [10,10]
    gold_mine = pygame.Rect(position[1]*blockSize, position[0]*blockSize, 50, 50)
    pygame.draw.rect(SCREEN, GOLD, (gold_mine))
    gold_mine = Gold_mine(position, gold_mine, 100)
    return gold_mine

#old
def copper_mine_():
    position = [10,15]
    copper_mine = pygame.Rect(position[1]*blockSize, position[0]*blockSize, 50, 50)
    pygame.draw.rect(SCREEN, COPPER, (copper_mine))
    copper_mine = Gold_mine(position, copper_mine, 100)
    return copper_mine

def removeant(cord):
    antsize = 25
    removeant = pygame.Rect(cord[1], cord[0], antsize, antsize)
    pygame.draw.rect(SCREEN, BLACK, removeant)
    pygame.display.update()

def drawant(cord, color): #draws a red rectangle for the ant
    antsize = 25
    ant = pygame.Rect(cord[1], cord[0], antsize, antsize)
    pygame.draw.rect(SCREEN, color, ant)

# rewrites a-star path to a path compatible with the grid
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
    turn_button = pygame.Rect(WINDOW_WIDTH-100, WINDOW_HEIGHT-50, 100, 50)
    hq = hq_()
    ant_already_clicked = False
    next_turn = False
    draw_movement = False
    ants = []
    buildings = [hq]
    gold_buildings = []
    resources = Resources(500, 1000)
    message = None
    while True:
        drawGrid(map, resources, message)
        pygame.draw.rect(SCREEN, GREEN, turn_button)
        draw_text('Next turn', next_turn_font, BLACK, GREEN, SCREEN, WINDOW_WIDTH-50, WINDOW_HEIGHT-25)
        if draw_movement:
            draw_movement_func(current_ant,map)
        for event in pygame.event.get():
            if next_turn:
                ai_turn(resources, gold_buildings)
                next_turn = False
                break
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    # Check if the barrack collides with the mouse pos.
                    if turn_button.collidepoint((pygame.mouse.get_pos())):
                        next_turn = True
                        continue

                    for building in buildings:
                        if building.rect.collidepoint((pygame.mouse.get_pos())):
                            if building.color == ORANGE:
                                hq_menu(building,ants,buildings)
                                break
                            if building.color == GOLD:
                                tower_menu(building,ants,buildings)
                                break
                            if building.color == WHITE:
                                barrack_menu(building,ants,buildings)
                                break
                    
                    # if barrack.rect.collidepoint((pygame.mouse.get_pos())):
                    #     menu(ants, buildings)
                    if ant_already_clicked:
                        draw_movement = False
                        prev_cord = [-25,-25]
                        ant_already_clicked = False
                        mouse_position = pygame.mouse.get_pos()
                        # print(mouse_position)
                        column, r1 = divmod(mouse_position[0],25)
                        row, r2 = divmod(mouse_position[1],25)
                        end = (row, column)
                        print(current_ant.position)
                        print(end)
                        print('')
                        print(current_ant.position[0])
                        print(current_ant.position[1])
                        print('')
                        print(column-current_ant.position[1])
                        print(row-current_ant.position[0])
                        print('')
                        print(current_ant.movement)
                        if column-current_ant.position[1] > current_ant.movement or current_ant.movement < row-current_ant.position[0]:
                            message = 'Clicked a tile out of range for ant. Range is {}'.format(current_ant.movement)
                            ants.append(current_ant)
                            continue

                        path = astar(current_ant.position,end,map)
                        # print(path)
                        grid_path = gridpath(path)
                        # print(grid_path)

                        for cord in grid_path:
                            print(cord)
                            drawGrid(map, resources, message)
                            time.sleep(0.5)
                            removeant(prev_cord)
                            prev_cord = cord
                            drawant(cord, current_ant.color)
                            pygame.display.update()
                        ant = pygame.Rect(end[1]*25, end[0]*25, blockSize, blockSize)
                        current_ant.rect = ant
                        current_ant.position = end
                        print(current_ant.rect)
                        print(current_ant.position)
                        print(ants)
                        print('')
                        ants.append(current_ant)
                        print(ants)

                        continue
        
                    if len(ants) != 0:
                        for ant in ants:
                            if ant.rect.collidepoint(pygame.mouse.get_pos()):
                                print("Mouse clicked on the ant")
                                draw_movement = True
                                current_ant = ant
                                ants.remove(ant)
                                ant_already_clicked = True
                                break
                if mouse_presses[2]: #right mouse button
                    for ant in ants:
                        if ant.rect.collidepoint(pygame.mouse.get_pos()):
                            print("Mouse right clicked on the ant")
                            if ant.color == VIOLET:
                                builder_menu(ant,ants,buildings)
                                break
        pygame.display.update()

main_menu()