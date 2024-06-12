import pygame
from AttackPhase import Damage


class Rogue:
    def __init__(self, hp, atk, df, spd, x, y, movement, cr, cd):
        self.hit_points = hp
        self.max_hp = hp
        self.attack_power = atk
        self.defense = df
        self.speed = spd
        self.crit_rate = cr
        self.crit_damage = cd
        self.og_crit_rate = cr
        self.og_crit_damage = cd
        self.movement = movement
        self.max_movement = movement
        self.move_phase = False
        self.attack_phase = False
        self.end_phase = False
        self.buffed_state = False
        self.x = x
        self.y = y
        self.turn = False
        self.image = pygame.image.load("Rogue.png")
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.order = 0
        self.current_action_points = 5
        self.action_points = 5

    def attack(self, target):
        Damage.attack(self, target)

    def take_damage(self, damage):
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
        self.crit_rate = self.og_crit_rate
        self.crit_damage = self.og_crit_damage
        self.current_action_points = self.action_points
        self.buffed_state = False

    def draw(self, screen):
        screen.blit(self.image, (self.x * 24, self.y * 24))

    def crit_up(self):
        self.crit_rate += 10
        self.crit_damage += 15
