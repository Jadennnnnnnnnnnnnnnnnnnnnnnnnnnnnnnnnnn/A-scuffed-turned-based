import pygame


class StageCreation:

    def __init__(self, stage, x, y):
        self.tile = None
        self.world = None
        self.rect = None
        self.image = None
        self.x = x
        self.y = y
        self.stage = stage
        self.stage = self.create_list()

    def create_list(self):
        self.stage = []
        world = []
        if self.stage == 1:
            with open("Stage 1", "r") as t:
                for line in t:
                    self.world.append(line.strip())
            self.stage = [list(line) for line in world]
        return self.stage

    def set_image(self, tile):
        if tile == 0:
            self.image = pygame.image.load("tile-0-pixilart.png")
        elif tile == 1 or tile == 4:
            self.image = pygame.image.load("tile-0-pixilart.png")
            self.image = pygame.transform.scale(self.image, (24, 24))
        elif tile == 2:
            self.image = pygame.image.load("tile-2-pixilart.png")
            self.image = pygame.transform.scale(self.image, (24, 24))
        elif tile == 3:
            self.image = pygame.image.load("tile-3-pixilart.png")
            self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect(topleft=(24, 24))

    def draw(self, screen):
        for row in self.stage:
            for column in row:
                self.set_image(column)
                self.x += 24
                screen.blit(self.image, (self.x, self.y))
            self.x = 0
            self.y += 24
