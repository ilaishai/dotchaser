import pygame
import sys
import window

pygame.init()
screen = pygame.display.set_mode((17 * 50, 16 * 50))
pygame.display.set_caption('BOMBERMAN')
surface = pygame.Surface(screen.get_size())
scrnsize = pygame.display.get_surface().get_size()
win = window.Window(surface)
win.drawWindow()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(surface, (0, 0))
    pygame.display.flip()