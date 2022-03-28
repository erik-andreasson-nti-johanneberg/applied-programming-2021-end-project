#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
 
# Setup pygame/window ---------------------------------------- #

WINDOW_HEIGHT = 625
WINDOW_WIDTH = 1250

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)


 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('Main Menu', font, (255, 255, 255), screen, (WINDOW_WIDTH/2)-10, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        menu_button_1 = pygame.Rect((WINDOW_WIDTH/2)-77, 100, 200, 50)
        menu_button_2 = pygame.Rect((WINDOW_WIDTH/2)-77, 200, 200, 50)
        menu_button_3 = pygame.Rect((WINDOW_WIDTH/2)-77, 500, 200, 50)
        if menu_button_1.collidepoint((mx, my)):
            if click:
                game()
        if menu_button_2.collidepoint((mx, my)):
            if click:
                options()
        if menu_button_3.collidepoint((mx, my)):
            if click:
                quit()
        pygame.draw.rect(screen, (0, 0, 255), menu_button_1)
        draw_text('Game', font, (255,255,255), screen, WINDOW_WIDTH/2,120)
        pygame.draw.rect(screen, (255, 0, 0), menu_button_2)
        draw_text('Options', font, (255,255,255), screen, WINDOW_WIDTH/2,220)
        pygame.draw.rect(screen, (0, 100, 0), menu_button_3)
        draw_text('Quit', font, (255,255,255), screen, WINDOW_WIDTH/2,520)
 
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Game', font, (255, 255, 255), screen, (WINDOW_WIDTH/2)-10, 20)
        draw_text('Play', font, (255,255,255), screen, WINDOW_WIDTH/2,120)
        game_button_1 = pygame.Rect((WINDOW_WIDTH/2)-77, 100, 200, 50)
        draw_text('Back', font, (255, 255, 255), screen, (WINDOW_WIDTH/2)-10, 220)
        game_button_2 = pygame.Rect((WINDOW_WIDTH/2)-77, 200, 200, 50)
        pygame.draw.rect(screen, (0, 0, 255), game_button_1)
        pygame.draw.rect(screen, (255, 0, 0), game_button_2)
        draw_text('Play', font, (255,255,255), screen, WINDOW_WIDTH/2,120)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()