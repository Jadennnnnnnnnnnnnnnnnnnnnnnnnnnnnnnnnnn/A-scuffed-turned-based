import random


class Damage:
    @staticmethod
    def calculate_damage(attacker, target):
        damage = round(((random.randint(85, 105) / 100) * attacker.attack) / target.defense * random.randint(5, 10))
        if random.randint(attacker.crit_rate, 100) <= attacker.crit_rate:
            damage = round(damage * ((random.randint(attacker.crit_damage - 10, attacker.crit_damage + 10) / 100) * target.defense / 3))
        return damage

    @staticmethod
    def attack(attacker, target):
        damage = Damage.calculate_damage(attacker, target)
        target.take_damage(damage)

    @staticmethod
    def damage(target, damage):
        target.hit_points -= damage
        if target.hit_points < 0:
            target.hit_points = 0
