import pygame
import sys
import map

class Window:
    def __init__(self, surface):
        self.surface = surface
        self.map = map.Grid(surface)

    def drawWindow(self):
        self.map.draw()

    def keytype(self, event, player):
        print(event.key)
        if event.key == pygame.K_w:
            player.yloc -= 10
        if event.key == pygame.K_a:
            player.xloc -= 10
        if event.key == pygame.K_s:
            player.yloc += 10
        if event.key == pygame.K_d:
            player.xloc += 10

        return player
