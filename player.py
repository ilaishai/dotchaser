import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, xloc=40, yloc=30, score=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 800), pygame.SRCALPHA)
        #self.image.fill()
        self.xloc = xloc
        self.yloc = yloc
        self.score = score

    def drawplayer(self):
        self.image.fill(pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (self.xloc * 10, self.yloc * 10), 10)
        return self.image
