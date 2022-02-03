import pygame as pygame
import sys
from pygame.locals import *
from random import *

#Initialize the game
pygame.init()

#Framerate
FPS = 10
FramePerSec = pygame.time.Clock()

#Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)

#Display with caption
DISPLAYSURF = pygame.display.set_mode((800,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
SCREEN_WIDTH = 800

# Creating Lines and Shapes
# pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
# pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
# pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
# pygame.draw.circle(DISPLAYSURF, YELLOW, (100,50), 30)
# pygame.draw.circle(DISPLAYSURF, YELLOW, (200,50), 30)
# pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
# pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))

#Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.rect = pygame.draw.rect(DISPLAYSURF, RED, (1, 0, 100, 50))
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        # print(pressed_keys)
        events = pygame.event.get()
        for event in events:
            if self.rect.left > 0:
                print(pressed_keys[K_1])
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.rect.move_ip(-5, 0)
                    if self.rect.right < SCREEN_WIDTH:
                        if event.key == pygame.K_RIGHT:   
                            if pressed_keys[K_0]:
                                self.rect.move_ip(5, 0)
    
    def draw(self, surface):
        surface.blit(surface, self.rect)     
 
         
P1 = Player()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    P1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
