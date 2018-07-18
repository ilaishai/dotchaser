import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, xloc=40, yloc=30, score=0, tail=0, face=""):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 800), pygame.SRCALPHA)
        #self.image.fill()
        self.xloc = xloc
        self.yloc = yloc
        self.score = score
        self.tail = tail
        self.face = face

    def drawplayer(self):
        self.image.fill(pygame.SRCALPHA)
        #pygame.draw.circle(self.image, (0, 0, 255), (self.xloc * 10, self.yloc * 10), 10)
        player = pygame.rect.Rect(self.xloc * 10, self.yloc * 10, 10, 10)
        pygame.draw.rect(self.image, (0, 0, 255), player)
        return self.image
