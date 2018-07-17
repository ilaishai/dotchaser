import pygame



def is_num(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

class Block:
    def __init__(self, surface, type, xcoord, ycoord):
        self.surface = surface
        self.type = type
        self.xcoord = xcoord
        self.ycoord = ycoord

    def drawBlock(self):
        if self.type == "w":
            pygame.draw.rect(self.surface, (0, 0, 0), pygame.rect.Rect(self.xcoord, self.ycoord, 10, 10))
            pygame.draw.rect(self.surface, (255, 255, 255),
                             pygame.rect.Rect(self.xcoord + 0.5, self.ycoord + 0.5, 9, 9))
        if self.type == "b":
            pygame.draw.rect(self.surface, (0, 0, 0),
                             pygame.rect.Rect(self.xcoord + 0.5, self.ycoord + 0.5, 9, 9))

class Grid:

    def __init__(self, surface):
        self.surface = surface
        for col in range(80):
            for row in range(80):
                block = Block(surface, "w", row * 10, col * 10)

    def draw(self):
        with open ("tilemap.txt", "r") as file:
            import re
            tilemap = file.readlines()
            count = 0
            for line in tilemap:
                totalrow = 0
                rowdata = (re.split('(\d+)', line))
                print(rowdata)
                rowdata.pop(0)
                for i in range(len(rowdata)):
                    if is_num(rowdata[i]):
                        for k in range(int(rowdata[i])):
                            block = Block(self.surface, rowdata[i+1][0], (totalrow) * 10, count * 10)
                            block.drawBlock()
                            totalrow += 1
                count += 1

        '''for col in range(80):
            for row in range(80):
                block = Block(self.surface, "empty", row * 10, col * 10)
                block.drawBlock()'''

        '''for unit in self.border:

        for unit in self.block:
            pygame.draw.rect(self.surface, (255, 255, 255), unit)'''