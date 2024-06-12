import pygame
from AttackPhase import Damage


class Enemy:
    def __init__(self, hp, atk, df, spd, x, y, movement, cr, cd):
        self.hit_points = hp
        self.max_hp = hp
        self.attack_power = atk
        self.defense = df
        self.speed = spd
        self.crit_rate = cr
        self.crit_damage = cd
        self.movement = movement
        self.max_movement = movement
        self.x = x
        self.y = y
        self.turn = False
        self.image = pygame.image.load("Orc.png")
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.order = 0
        self.move_phase = False
        self.attacking_phase = False
        self.end_phase = False
        self.action_points = 3
        self.current_action_points = 3

    def attack(self, target):
        Damage.attack(self, target)

    def take_damage(self, damage):
        Damage.damage(self, damage)

    def move(self, dx, dy, stage):
        self.movement -= 1
        if self.movement > 0:
            new_x = self.x + dx
            new_y = self.y + dy
            if stage.is_passable(new_x, new_y):
                self.x = new_x
                self.y = new_y
            elif stage.is_passable(new_x, self.y):
                self.x = new_x
            elif stage.is_passable(self.x, new_y):
                self.y = new_y

    def end_of_turn(self):
        self.movement = self.max_movement
        self.action_points = self.current_action_points

    def draw(self, screen):
        screen.blit(self.image, (self.x * 24, self.y * 24))
