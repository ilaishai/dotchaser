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
                             pygame.rect.Rect(self.xcoord, self.ycoord, 10, 10))

        if self.type == "r":
            pygame.draw.rect(self.surface, (255, 0, 0),
                             pygame.rect.Rect(self.xcoord, self.ycoord, 10, 10))

class Grid:

    def __init__(self, surface):
        self.surface = surface
        self.gridmap = []
        self.objective = (0, 0)
        with open ("tilemap.txt", "r") as file:
            import re
            storedmap = file.readlines()
            count = 0
            for line in storedmap:
                self.gridmap.append([])
                totalrow = 0
                rowdata = (re.split('(\d+)', line))
                rowdata.pop(0)
                for i in range(len(rowdata)):
                    if is_num(rowdata[i]):
                        for k in range(int(rowdata[i])):
                            block = Block(self.surface, rowdata[i+1][0], count * 10, totalrow * 10)
                            self.gridmap[len(self.gridmap) - 1].append(block)
                            self.gridmap[len(self.gridmap) - 1][totalrow].drawBlock()
                            totalrow += 1
                count += 1
        self.set_room()

    def set_room(self):
        import random
        self.objective = (random.randint(2, 78), random.randint(2, 78))
        self.gridmap[self.objective[0]][self.objective[1]].type = "r"

    def draw(self):
        for i in range(len(self.gridmap)):
            for k in range(len(self.gridmap[i])):
                self.gridmap[k][i].drawBlock()
