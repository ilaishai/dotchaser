import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, xloc = 400, yloc = 300):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 800), pygame.SRCALPHA)
        #self.image.fill()
        self.xloc = xloc
        self.yloc = yloc

    def drawplayer(self):
        self.image.fill(pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (self.xloc, self.yloc), 10)
        return self.image
