import pygame


class StageCreation:

    def __init__(self, stage):
        self.stage = []
        world = []
        if stage == 1:
            with open("Stage 1", "r") as t:
                for line in t:
                    self.world.append(line.strip())
            self.stage = [list(line) for line in world]

    def create_stage(self):
        for i in self.stage:
            for j in i:
                if j == 0:
                    self.image = pygame.image.load("tile-0-pixilart.png")
                elif j == 1 or j == 4:
                    self.image = pygame.image.load("tile-1-pixilart.png")
                elif j == 2:
                    self.image = pygame.image.load("tile-2-pixilart.png")
                    self.image = image.resize((24, 24))





