import pygame, sys
from pygame.locals import *

# bestam hur ditt spelfonsternster ska se ut
# samma hojd som bilden
#bredd och hojd
W = 700
H = 512

#halva hojden/bredden
HW = W / 2
HH = H / 2
#spelfonstrets area
AREA = W * H

#setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Bakgrundsbild")
FPS = 60

#my images
bg_image = pygame.image.load("images/bg.png").convert()

#x-position bakgrundsbilden
x = 0


#spel-loopen
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    rel_x = x % bg_image.get_rect().width

    SCREEN.blit(bg_image,(rel_x - bg_image.get_rect().width,0))
    if rel_x < W:
        SCREEN.blit(bg_image, (rel_x,0))
    x -= 1
    pygame.display.update()
    CLOCK.tick(FPS)
