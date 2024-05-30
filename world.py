import pygame


class StageCreation:

    def __init__(self, stage, x, y):
        self.tile = None
        self.world = []
        self.rect = None
        self.image = None
        self.x = x
        self.y = y
        self.stage = stage
        self.stage_map = self.create_list()

    def create_list(self):
        world = []
        if self.stage == 1:
            with open("Stage 1", "r") as t:
                for line in t:
                    world.append(line.strip())
            return [list(line) for line in world]

    def set_image(self, tile):
        if tile == "0":
            self.image = pygame.image.load("tile-0-pixilart.png")
            self.image = pygame.transform.scale(self.image, (32, 32))
        elif tile == "1" or tile == "4":
            self.image = pygame.image.load("tile-0-pixilart.png")
            self.image = pygame.transform.scale(self.image, (32, 32))
        elif tile == "2":
            self.image = pygame.image.load("tile-2-pixilart.png")
            self.image = pygame.transform.scale(self.image, (32, 32))
        elif tile == "3":
            self.image = pygame.image.load("tile-3-pixilart.png")
            self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        for i, row in enumerate(self.stage_map):
            for j, tile in enumerate(row):
                self.x = i * 32
                self.y = j * 32
                self.set_image(tile)
                screen.blit(self.image, (self.x, self.y))

