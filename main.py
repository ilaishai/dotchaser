import pygame
import sys
import window
import player

pygame.init()
screen = pygame.display.set_mode((16 * 50, 16 * 50))
pygame.display.set_caption('BOMBERMAN')
surface = pygame.Surface(screen.get_size())
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
                p1.yloc -= 10
            if event.key == pygame.K_a:
                p1.xloc -= 10
            if event.key == pygame.K_s:
                p1.yloc += 10
            if event.key == pygame.K_d:
                p1.xloc += 10

    p1.drawplayer()
    screen.blit(surface, (0, 0))
    screen.blit(p1.drawplayer(), (0, 0))
    pygame.display.flip()