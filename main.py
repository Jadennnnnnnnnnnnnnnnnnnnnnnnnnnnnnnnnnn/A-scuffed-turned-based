from world import StageCreation
from Rogue import Rogue
from Enemy import Enemy
import pygame


def speed_order(charas):
    base_speed = 0
    s_turn = []
    for chara in charas:
        if chara.order > base_speed:
            base_speed = chara.order
            s_turn = [chara]
        elif chara.order == base_speed:
            s_turn.append(chara)
    if len(s_turn) > 1:
        for i in s_turn:
            i.order += i.speed
    else:
        current_turn = s_turn[0]
        current_turn.order = 0
        if current_turn == "p1":
            p1.turn = True
        elif current_turn == "e1":
            e1.turn = True
    for chara in charas:
        chara.order += chara.speed
    return "Speed_Calc"


def enemy_turn(e, p, s):
    if e.movement > 0:
        if e.x < p.x:
            dx = 1
        elif e.x > p.x:
            dx = -1
        elif e.y < p.y:
            dy = 1
        elif e.y > p.y:
            dy = -1
        elif e.y + 1 == p.y or e.y - 1 == p.y:
            dy = 0
        elif e.x + 1 == p.x or e.x - 1 == p.x:
            dx = 0
        e.move(dx, dy, s)
    if abs(e.x - p.x) <= 1 and abs(e.y - p.y) <= 1:
        e.attack(p)
        e.hit_points = round(e.hit_points * 1.1)
    e.turn = False


def draw(scr, sta, p, e, hl):
    scr.fill((0, 0, 0))
    sta.draw(scr)
    p.draw(scr)
    if hl:
        hl = pygame.Rect(e.x * 24, e.y * 24, (24, 24))
        pygame.draw.rect(scr, (255, 0, 0), hl, 3)
    e.draw(scr)


pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
stage = StageCreation(1, 0, 0)
Rogue1 = Rogue(60, 50, 50, 75, 5, 5, 10, 40, 200)
e1 = Enemy(100, 75, 75, 50, 3, 3, 6, 5, 140)

running = True
phase = "Speed_Calc"
highlight = False

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if Rogue1.turn:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Rogue1.move(0, -1, stage)
                elif event.key == pygame.K_s:
                    Rogue1.move(0, 1, stage)
                elif event.key == pygame.K_a:
                    Rogue1.move(-1, 0, stage)
                elif event.key == pygame.K_d:
                    Rogue1.move(1, 0, stage)
                elif event.key == pygame.K_1:
                    if abs(Rogue1.x - e1.x) <= 1 and abs(Rogue1.y - e1.y) <= 1:
                        highlight = True

    draw(screen, stage, Rogue1, e1, highlight)
    pygame.display.flip()

pygame.quit()
