from importlib import resources
from turtle import position
from numpy import block
import pygame
import sys
import time
from functional.a_star_pure import astar
import random
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
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# Global fonts
barrack_font = pygame.font.Font('freesansbold.ttf', 32)
menu_font = pygame.font.Font('freesansbold.ttf', 30)
next_turn_font = pygame.font.Font('freesansbold.ttf', 15)
info_bar_font = pygame.font.Font('freesansbold.ttf', 13)
stat_font = pygame.font.Font('freesansbold.ttf', 5)



#ant class
class Ant():
    def __init__(self, position=None, rect=None):
        self.position = position
        self.rect = rect

#builder ant
class Builder_ant():
    def __init__(self, position=None, rect=None, movement=2, hp=1, range=0, attack=0, color=VIOLET, actions=2):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color
        self.actions = actions

#beta ant
class Beta_ant():
    def __init__(self, position=None, rect=None, movement=5, hp=10, range=1, attack=5, color=RED, actions=1):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color
        self.actions = actions

#chad ant
class Chad_ant():
    def __init__(self, position=None, rect=None, movement=9, hp=5, range=1, attack=6, color=MAGENTA, actions=1):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color
        self.actions = actions

#sigma ant
class Sigma_ant():
    def __init__(self, position=None, rect=None, movement=7, hp=3, range=4, attack=4, color=BROWN, actions=1):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color
        self.actions = actions

#queen ant
class Queen_ant():
    def __init__(self, position=None, rect=None, movement=15, hp=20, range=2, attack=12, color=GREEN, actions=1):
        self.position = position
        self.rect = rect
        self.movement = movement
        self.hp = hp
        self.range = range
        self.attack = attack
        self.color = color
        self.actions = actions

#resources class
class Resources():
    def __init__(self, gold=0, copper=0):
        self.gold = gold
        self.copper = copper

#hq class #builds two times max in a turn
class HQ():
    def __init__(self, position=None, rect=None, pr_storage=None, level=1, hp=4, armor=2, color=ORANGE, size=2, actions=2):
        self.position = position
        self.rect = rect
        self.pr_storage = pr_storage
        self.level = level
        self.hp = hp
        self.armor = armor
        self.color = color
        self.size = size
        self.actions = actions

#barracks class #builds 4 times max in a turn
class Barrack():
    def __init__(self, position=None, rect=None, level=1, hp=4, armor=2, color=WHITE, size=2, actions=4):
        self.position = position
        self.rect = rect
        self.level = level
        self.hp = hp
        self.armor = armor
        self.color = color
        self.size = size
        self.actions = actions

#gold mine class #Archived
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
    def __init__(self, position=None, rect=None, hp=5, armor=2, range=4, attack=4, level=1, color=GOLD, size=1, actions=1):
        self.position = position
        self.rect = rect
        self.hp = hp
        self.armor = armor
        self.range = range
        self.attack = attack
        self.level = level
        self.color = color
        self.size = size
        self.actions = actions

#checks if resources are available for a purchase and in that case deducts them from the balance
def purchase(resources,price):
    if resources.copper >= price[0] and resources.gold >= price[1]:
        resources.copper -= price[0]
        resources.gold -= price[1]
        return True
    else:
        return False

#combat between two ants
def combat(attacking,defending,ants):
    bonus = random.randint(-2,2)
    defending.hp = defending.hp - (attacking.attack + bonus)
    attacking.hp = attacking.hp - (defending.attack/2)
    if defending.hp <= 0:
        ants.remove(defending)
    if attacking.hp <= 0:
        ants.remove(attacking)

# makes building placements into walls in the map
def place_walls(position,size):
    for i in range(size):
        map[position[0]][position[1]] = 1
        map[position[0]][position[1]+i] = 1
        map[position[0]+i][position[1]] = 1
        map[position[0]+i][position[1]+i] = 1

# ai_turn placeholder, will be moved to a seperate file
def ai_turn(resources, mines):
    for building in mines:
        resources.copper += building.tick
    print('')
    print(resources.gold)
    print(resources.copper)

#Draws text to the screen. Must be called after the backdrop menu has been drawn to the screen
def draw_text(text, font, text_color, background_color, surface, x, y):
    textobj = font.render(text, True, text_color, background_color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#Draws the grid and resource bar
def drawGrid(map, resources,message,buildings,ants):
    blockSize = 25 #Set the size of the grid block
    buildings_to_draw = []
    for index_x, x in enumerate(range(0, WINDOW_HEIGHT, blockSize)):
        for index_y, y in enumerate(range(0, WINDOW_WIDTH, blockSize)):
            if map[index_x][index_y] == 1:
                for building in buildings:
                    if map[building.position[0]][building.position[1]] == map[index_x][index_y]:
                        buildings_to_draw.append(building)
                rect = pygame.Rect(y, x, blockSize, blockSize)
                rect2 = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, BLUE, rect)
                pygame.draw.rect(SCREEN, WHITE, rect2, 1)
            else:
                rect = pygame.Rect(y, x, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
    for building in buildings_to_draw:
        pygame.draw.rect(SCREEN,building.color,building.rect)
    draw_info_bar(resources,message)

def draw_info_bar(resources,message):
    info_bar = pygame.Rect(0,0, WINDOW_WIDTH, blockSize)
    pygame.draw.rect(SCREEN, BLUE, info_bar)
    draw_text('Gold: ' + str(resources.gold), info_bar_font, WHITE, BLUE, SCREEN, 50, blockSize/2)
    draw_text('Copper: ' + str(resources.copper), info_bar_font, WHITE, BLUE, SCREEN, 150, blockSize/2)
    draw_text(message, info_bar_font, WHITE, BLUE, SCREEN, WINDOW_WIDTH/2, blockSize/2)

def draw_movement_func(ant,map):
    blockSize = 25 #Set the size of the grid block
    for x in range((ant.position[1]-ant.movement)*blockSize, (ant.position[1]+ant.movement+1)*blockSize, blockSize):
        for y in range((ant.position[0]-ant.movement)*blockSize, (ant.position[0]+ant.movement+1)*blockSize, blockSize):
            try:
                if map[int(y/blockSize)][int(x/blockSize)] == 0:
                    rect = pygame.Rect(x, y, blockSize, blockSize)
                    white_space = pygame.Rect(x,y,blockSize,blockSize)
                    pygame.draw.rect(SCREEN, RED, rect)
                    pygame.draw.rect(SCREEN,WHITE,white_space,1)
            except:
                pass
    pygame.draw.rect(SCREEN,ant.color,ant.rect)

#removes the menu from the screen and redraws all buildings and ants
def remove_menu(ants, building_list):
    replace_with_black_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.draw.rect(SCREEN, BLACK, replace_with_black_rect)
    for building in building_list:
        building_rect = pygame.Rect(building.position[1]*25, building.position[0]*25, building.size*25, building.size*25)
        pygame.draw.rect(SCREEN, building.color, building_rect)
    for ant in ants:
        ant_rect = pygame.Rect(ant.position[1]*25, ant.position[0]*25, blockSize, blockSize)
        pygame.draw.rect(SCREEN, ant.color, ant_rect)
    
#Menus

#stat menu
# def stat_menu(ant):
#     menu_rect = pygame.Rect(ant.position[1]*25-25, ant.position[0]*25-50, 50, 50)
#     pygame.draw.rect(SCREEN,BLUE, (menu_rect))
#     draw_text('HP: {}'.format(ant.hp), stat_font, RED, BLACK, SCREEN, 5, 25)
#     draw_text('Attack: {}'.format(ant.attack), stat_font, RED, BLACK, SCREEN, 25, 25)


# barrack_menu    
def barrack_menu(building, ants, buildings,resources):
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
        exit_button = pygame.Rect(75,75,50,50)
        position_chad_myra = [building.position[0],building.position[1]+2]
        position_beta_myra = [building.position[0],building.position[1]+2]
        chad_myra_rect = pygame.Rect(position_chad_myra[1]*25, position_chad_myra[0]*25, blockSize, blockSize)
        beta_myra_rect = pygame.Rect(position_beta_myra[1]*25, position_beta_myra[0]*25, blockSize, blockSize)

        pygame.draw.rect(SCREEN, WHITE, (chad_myra_button))
        pygame.draw.rect(SCREEN, WHITE, (beta_myra_button))
        pygame.draw.rect(SCREEN,RED,(exit_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    if exit_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants,buildings)
                        selected = True
                        break
                    if chad_myra_button.collidepoint((pygame.mouse.get_pos())):
                        if purchase(resources, [100,0]):
                            remove_menu(ants, buildings)
                            chad_myra = Chad_ant(position_chad_myra, chad_myra_rect)
                            ants.append(chad_myra)
                            pygame.draw.rect(SCREEN, MAGENTA, (chad_myra_rect))
                            selected = True
                            break
                        else:
                            draw_info_bar(resources, 'You do not have enough resources!')
                    if beta_myra_button.collidepoint((pygame.mouse.get_pos())):
                        if purchase(resources, [150,0]):
                            remove_menu(ants, buildings)
                            beta_myra = Beta_ant(position_beta_myra, beta_myra_rect)
                            ants.append(beta_myra)
                            pygame.draw.rect(SCREEN, RED, (beta_myra_rect))
                            selected = True
                            break
                        else:
                            draw_info_bar(resources, 'You do not have enough resources!')
        pygame.display.update()

def hq_menu(building,ants,buildings,resources):
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
        exit_button = pygame.Rect(75,75,50,50)
        position_builder_myra = [building.position[0],building.position[1]+2]
        position_queen_myra = [building.position[0],building.position[1]+2]
        builder_myra_rect = pygame.Rect(position_builder_myra[1]*25, position_builder_myra[0]*25, blockSize, blockSize)
        queen_myra_rect = pygame.Rect(position_queen_myra[1]*25, position_queen_myra[0]*25, blockSize, blockSize)

        pygame.draw.rect(SCREEN, WHITE, (builder_myra_button))
        pygame.draw.rect(SCREEN, WHITE, (queen_myra_button))
        pygame.draw.rect(SCREEN,RED,(exit_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    if exit_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants,buildings)
                        selected = True
                        break
                    if builder_myra_button.collidepoint((pygame.mouse.get_pos())):
                        if purchase(resources, [100,0]):
                            remove_menu(ants, buildings)
                            builder_ant = Builder_ant(position_builder_myra, builder_myra_rect)
                            ants.append(builder_ant)
                            pygame.draw.rect(SCREEN, builder_ant.color, (builder_myra_rect))
                            selected = True
                            break
                        else:
                            draw_info_bar(resources, 'You do not have enough resources!')
                    if queen_myra_button.collidepoint((pygame.mouse.get_pos())):
                        if purchase(resources,[1000,500]):
                            remove_menu(ants, buildings)
                            queen_ant = Queen_ant(position_queen_myra, queen_myra_rect)
                            ants.append(queen_ant)
                            pygame.draw.rect(SCREEN, queen_ant.color, (queen_myra_rect))
                            selected = True
                            break
                        else:
                            draw_info_bar(resources, 'You do not have enough resources!')
        pygame.display.update()

def builder_menu(builder,ants,buildings,mines,resources):
    # Menu screen
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
        exit_button = pygame.Rect(75,75,50,50)

        position_copper_mine = builder_position
        position_tower = builder_position
        position_barracks = builder_position

        copper_mine_rect = pygame.Rect(position_copper_mine[1]*25, position_copper_mine[0]*25, blockSize, blockSize)
        tower_rect = pygame.Rect(position_tower[1]*25, position_tower[0]*25, blockSize, blockSize)
        barracks_rect = pygame.Rect(position_barracks[1]*25, position_barracks[0]*25, 50, 50)
        

        pygame.draw.rect(SCREEN, WHITE, (copper_mine_button))
        pygame.draw.rect(SCREEN, WHITE, (tower_button))
        pygame.draw.rect(SCREEN, WHITE, (barracks_button))
        pygame.draw.rect(SCREEN,RED,(exit_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    if exit_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants,buildings)
                        selected = True
                        break
                    if copper_mine_button.collidepoint((pygame.mouse.get_pos())):
                        if purchase(resources, [500,100]):
                            ants.remove(builder)
                            remove_menu(ants, buildings)
                            mine = Copper_mine(position_copper_mine, copper_mine_rect)
                            place_walls(builder_position,mine.size)
                            buildings.append(mine)
                            mines.append(mine)
                            pygame.draw.rect(SCREEN, mine.color, (tower_rect))
                            selected = True
                            break
                        else:
                            draw_info_bar(resources, 'You do not have enough resources!')
                    if tower_button.collidepoint((pygame.mouse.get_pos())):
                        if purchase(resources,[200,50]):
                            ants.remove(builder)
                            remove_menu(ants, buildings)
                            turret = Turret(position_tower, tower_rect)
                            place_walls(builder_position,turret.size)
                            buildings.append(turret)
                            pygame.draw.rect(SCREEN, turret.color, (tower_rect))
                            selected = True
                            break
                        else:
                            draw_info_bar(resources, 'You do not have enough resources!')
                    if barracks_button.collidepoint((pygame.mouse.get_pos())):
                        if purchase(resources,[300,100]):
                            ants.remove(builder)
                            remove_menu(ants, buildings)
                            barrack = Barrack(position_barracks, barracks_rect)
                            place_walls(builder_position,barrack.size)
                            buildings.append(barrack)
                            pygame.draw.rect(SCREEN, barrack.color, (barracks_rect))
                            selected = True
                            break
                        else:
                            draw_info_bar(resources, 'You do not have enough resources!')
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
        exit_button = pygame.Rect(75,75,50,50)
        pygame.draw.rect(SCREEN, WHITE, (level_up_button))
        pygame.draw.rect(SCREEN,RED,(exit_button))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    if exit_button.collidepoint((pygame.mouse.get_pos())):
                        remove_menu(ants,buildings)
                        selected = True
                        break
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
    map[12][1] = 1
    map[12][2] = 1
    map[13][1] = 1
    map[13][2] = 1

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
    mines = []
    resources = Resources(500, 1000)
    message = None
    fought = False
    while True:
        drawGrid(map, resources, message, buildings, ants)
        pygame.draw.rect(SCREEN, GREEN, turn_button)
        draw_text('Next turn', next_turn_font, BLACK, GREEN, SCREEN, WINDOW_WIDTH-50, WINDOW_HEIGHT-25)
        if draw_movement:
            draw_movement_func(current_ant,map)
        for event in pygame.event.get():
            if next_turn:
                ai_turn(resources, mines)
                next_turn = False
                break
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for ant in ants:
                if ant.rect.collidepoint((pygame.mouse.get_pos())):
                    message = 'HP: {} Attack: {} Ant has {} actions left'.format(ant.hp, ant.attack, ant.actions)
                    draw_info_bar(resources, message)
            for building in buildings:
                if building.rect.collidepoint((pygame.mouse.get_pos())):
                    message = 'HP: {} Armor: {} Building has {} actions left'.format(building.hp, building.armor, building.actions)
                    draw_info_bar(resources, message)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  # Left mouse button.
                    # Check if the barrack collides with the mouse pos.
                    if turn_button.collidepoint((pygame.mouse.get_pos())):
                        next_turn = True
                        continue

                    for building in buildings:
                        if building.rect.collidepoint((pygame.mouse.get_pos())):
                            if building.actions >= 1:
                                building.actions -= 1
                                if building.color == ORANGE:
                                    hq_menu(building,ants,buildings,resources)
                                    break
                                if building.color == GOLD:
                                    tower_menu(building,ants,buildings,resources)
                                    break
                                if building.color == WHITE:
                                    barrack_menu(building,ants,buildings,resources)
                                    break
                    
                    # if barrack.rect.collidepoint((pygame.mouse.get_pos())):
                    #     menu(ants, buildings)
                    if ant_already_clicked:
                        for defending in ants:
                            if defending.rect.collidepoint((pygame.mouse.get_pos())):
                                remove_menu(ants,buildings)
                                draw_movement = False
                                prev_cord = [-25,-25]
                                ant_already_clicked = False
                                mouse_position = pygame.mouse.get_pos()
                                # print(mouse_position)
                                column, r1 = divmod(mouse_position[0],25)
                                row, r2 = divmod(mouse_position[1],25)
                                end = (row, column-1)
                                if column-current_ant.position[1] > current_ant.movement or current_ant.movement < row-current_ant.position[0]:
                                    message = 'Clicked a tile out of range for ant. Range is {}'.format(current_ant.movement)
                                    ants.append(current_ant)
                                    remove_menu(ants,buildings)
                                    continue

                                path = astar(current_ant.position,end,map)
                                # print(path)
                                grid_path = gridpath(path)
                                # print(grid_path)

                                for cord in grid_path:
                                    drawGrid(map, resources, message, buildings,ants)
                                    time.sleep(0.5)
                                    removeant(prev_cord)
                                    prev_cord = cord
                                    drawant(cord, current_ant.color)
                                    pygame.display.update()
                                ant = pygame.Rect(end[1]*25, end[0]*25, blockSize, blockSize)
                                current_ant.rect = ant
                                current_ant.position = end
                                ants.append(current_ant)

                                combat(current_ant,defending,ants)
                                remove_menu(ants,buildings)

                                fought = True
                        print(fought)
                        if fought:
                            continue

                        remove_menu(ants,buildings)
                        fought = False
                        draw_movement = False
                        prev_cord = [-25,-25]
                        ant_already_clicked = False
                        mouse_position = pygame.mouse.get_pos()
                        # print(mouse_position)
                        column, r1 = divmod(mouse_position[0],25)
                        row, r2 = divmod(mouse_position[1],25)
                        end = (row, column)
                        if column-current_ant.position[1] > current_ant.movement or current_ant.movement < row-current_ant.position[0]:
                            message = 'Clicked a tile out of range for ant. Range is {}'.format(current_ant.movement)
                            ants.append(current_ant)
                            remove_menu(ants,buildings)
                            continue

                        path = astar(current_ant.position,end,map)
                        # print(path)
                        grid_path = gridpath(path)
                        # print(grid_path)

                        for cord in grid_path:
                            drawGrid(map, resources, message, buildings,ants)
                            time.sleep(0.5)
                            removeant(prev_cord)
                            prev_cord = cord
                            drawant(cord, current_ant.color)
                            pygame.display.update()
                        ant = pygame.Rect(end[1]*25, end[0]*25, blockSize, blockSize)
                        current_ant.rect = ant
                        current_ant.position = end
                        ants.append(current_ant)

                        continue
        
                    if len(ants) != 0:
                        for ant in ants:
                            if ant.rect.collidepoint(pygame.mouse.get_pos()):
                                if ant.actions >= 1:
                                    ant.actions -= 1
                                    print("Mouse clicked on the ant")
                                    draw_movement = True
                                    current_ant = ant
                                    ants.remove(ant)
                                    ant_already_clicked = True
                                    fought = False
                                    break
                if mouse_presses[2]: #right mouse button
                    for ant in ants:
                        if ant.rect.collidepoint(pygame.mouse.get_pos()):
                            print("Mouse right clicked on the ant")
                            fought = False
                            if ant.color == VIOLET:
                                builder_menu(ant,ants,buildings,mines,resources)
                                break
        pygame.display.update()

main_menu()