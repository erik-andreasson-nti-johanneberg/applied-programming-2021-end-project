import pygame
import sys
import random
pygame.init()
fps=30
fpsclock=pygame.time.Clock()
width = 800
height = 600
sur_obj=pygame.display.set_mode((width,height))
pygame.display.set_caption("Keyboard_Input")
White=(255,255,255)
pixel = 64
p1=10
p2=(height - pixel)
step=5
SCREEN_WIDTH = 800
blockXPosition = random.randint(0, (width - pixel))
print(blockXPosition)
blockYPosition = 0
blockXPositionChange = 0
blockYPositionChange = 2  

def block(x, y):
  pygame.draw.rect(sur_obj,(0,0,255),(x, y, 64, 64))

def crash(p1, p2):
    global blockYPosition
    global blockXPosition

    if (blockYPosition + pixel) > p2:
        if ((blockXPosition + pixel) > p1 and (blockXPosition + pixel) < (p1 + pixel)) or (blockXPosition < (p1 + (pixel-10)) and p1 < blockXPosition):
            blockYPosition = height + 1000


while True:
    sur_obj.fill(White)
    pygame.draw.rect(sur_obj, (255,0,0), (p1, p2, 50, 50))
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_a]:
        p1 -= step
    if key_input[pygame.K_w]:
        p2 -= step
    if key_input[pygame.K_d]:
        p1 += step
    if key_input[pygame.K_s]:
        p2 += step

    crash(p1, p2)
    
    if (blockYPosition >= height - 0):
        blockYPosition = 0 - pixel
        blockXPosition = random.randint(0, (width - pixel))
        print('done')

    blockYPosition += blockYPositionChange

    block(blockXPosition, blockYPosition)
    pygame.display.update()
    fpsclock.tick(fps)