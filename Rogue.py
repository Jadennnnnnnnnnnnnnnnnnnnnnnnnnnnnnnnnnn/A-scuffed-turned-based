import pygame
from AttackPhase import Damage


class Rogue:

    def __init__(self, hp, atk, df, spd, x, y, movement, cr, cd):
        self.hit_points = hp
        self.attack = atk
        self.defense = df
        self.speed = spd
        self.crit_rate = cr
        self.crit_damage = cd
        self.movement = movement
        self.max_movement = movement
        self.x = x
        self.y = y
        self.turn = False
        self.image = pygame.image.load("Physical Change.jpg")
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.order = 0

    def attack(self, target):
        Damage.attack(self, target)

    def damage(self, damage):
        Damage.damage(self, damage)

    def move(self, dx, dy, stage):
        if self.movement > 0:
            new_x = self.x + dx
            new_y = self.y + dy
            if stage.is_passable(new_x, new_y):
                self.x = new_x
                self.y = new_y
                self.movement -= 1

    def end_of_turn(self):
        self.movement = self.max_movement

    def draw(self, screen):
        screen.blit(self.image, (self.x * 24, self.y * 24))
