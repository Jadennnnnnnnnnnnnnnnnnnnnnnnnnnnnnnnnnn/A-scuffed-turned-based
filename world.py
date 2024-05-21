import pygame


class stage_creation:

    def __init__(self, stage):
        if stage == 1:
            t = open("Stage 1", "r")
            self.stage = [line.strip() for line in t]
            for i in self.stage:
                [line.strip() for line in i]





