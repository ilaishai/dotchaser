import pygame

class Window:
    def __init__(self, surface):
        self.surface = surface

    def drawWindow(self):
        for col in range(16):
            for row in range(17):
                rect = pygame.rect.Rect(row * 50, col * 50, 50, 50)
                pygame.draw.rect(self.surface, ((row % 2) * 255 , (col % 2) * 255, 0), rect)