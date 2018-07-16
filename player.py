import pygame

class Player:

    def __init__(self, surface, xloc = 400, yloc = 300):
        self.surface = surface
        self.xloc = xloc
        self.yloc = yloc

    def drawPlayer(self):
        player = pygame.image.load('resources/player_left.png')
