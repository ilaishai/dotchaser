import pygame
import sys
import map

class Window:
    def __init__(self, surface):
        self.surface = surface
        self.grid = map.Grid(surface)

    def drawWindow(self):
        self.grid.draw()

    def keytype(self, event, player):
        if event.key == pygame.K_w:
            player.yloc -= 10
        if event.key == pygame.K_a:
            player.xloc -= 10
        if event.key == pygame.K_s:
            player.yloc += 10
        if event.key == pygame.K_d:
            player.xloc += 10

        return player
