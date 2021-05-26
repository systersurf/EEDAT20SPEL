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
FPS = 10

#my images
bg_image = pygame.image.load("images/bg.png").convert()
player_image_1 = pygame.image.load("images/0.png").convert_alpha()
player_image_2 = pygame.image.load("images/1.png").convert_alpha()
player_image_3 = pygame.image.load("images/2.png").convert_alpha()




class Player:
    def __init__(self):
        self.x = HW
        self.y = H-200

    def spring(self, player_image):
        if player_image == 1:
            player_image = 2
        elif player_image == 2:
            player_image = 3
        else:
            player_image = 1

    def draw(self, player_image):
        SCREEN.blit(player_image,(self.x, self.y))

    def skrolla(self):
        SCREEN.blit(bg_image,(rel_x - bg_image.get_rect().width,0))
        if rel_x < W:
            SCREEN.blit(bg_image, (rel_x,0))

SCREEN.blit(bg_image,(0,0))

#x-position bakgrundsbilden
x = 0
player = Player()
player_images = [player_image_1, player_image_2, player_image_3]
player_image = 0

#spel-loopen
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()



    if pressed_keys[K_SPACE]:
        rel_x = x % bg_image.get_rect().width
        player.skrolla()
        x -= 2

        player.draw(player_images[player_image])
        player_image += 1
        if player_image == 2:
            player_image = 0

    pygame.display.update()
    CLOCK.tick(FPS)
