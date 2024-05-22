import pygame


class StageCreation:

    def __init__(self, stage, x, y):
        self.x = x
        self.y = y
        self.size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.stage = self.create_list()

    def create_list(self):
        self.stage = []
        world = []
        if stage == 1:
            with open("Stage 1", "r") as t:
                for line in t:
                    self.world.append(line.strip())
            self.stage = [list(line) for line in world]

    def image(self, tile):
        self.tile = tile
        self.set_image()

    def set_image(self):
        if self.tile == 0:
            self.image = pygame.image.load("tile-0-pixilart.png")
        elif self.tile == 1 or self.tile == 4:
            self.image = pygame.image.load("tile-1-pixilart.png")
        elif self.tile == 2:
            self.image = pygame.image.load("tile-2-pixilart.png")
            self.image = image.resize((24, 24))
        elif self.tile == 3:
            self.image = pygame.image.load("tile-3-pixilart.png")
            self.image = image.resize((24, 24))

    def draw(self):
        for i in self.stage:
            for j in i:
                self.stage[i][j].set_image(self.stage[i][j][0])





