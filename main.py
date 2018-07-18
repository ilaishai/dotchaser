import pygame
import sys
import window
import player
import time

pygame.init()
screen = pygame.display.set_mode((16 * 50, 16 * 50))
pygame.display.set_caption('BOMBERMAN')
surface = pygame.Surface(screen.get_size())
surface.fill((255, 20, 147))
scrnsize = pygame.display.get_surface().get_size()
win = window.Window(surface)
win.drawWindow()
p1 = player.Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                #p1.yloc -= 1
                p1.face = "up"
            if event.key == pygame.K_a:
                #p1.xloc -= 1
                p1.face = "lft"
            if event.key == pygame.K_s:
                #p1.yloc += 1
                p1.face = "dn"
            if event.key == pygame.K_d:
                #p1.xloc += 1
                p1.face = "rt"
    time.sleep(0.05)
    if p1.face == "up":
        p1.yloc -= 1
    if p1.face == "lft":
        p1.xloc -= 1
    if p1.face == "dn":
        p1.yloc += 1
    if p1.face == "rt":
        p1.xloc += 1

    p1.drawplayer()
    distance = ((win.grid.objective[0] - p1.xloc)**2 + (win.grid.objective[1] - p1.yloc)**2)**0.5
    strt = ((win.grid.objective[0] - 40)**2 + (win.grid.objective[1] - 30)**2)**0.5
    p1.score = strt - distance
    print(p1.score)
    screen.blit(surface, (0, 0))
    screen.blit(p1.drawplayer(), (0, 0))
    pygame.display.flip()