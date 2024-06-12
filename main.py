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
        if current_turn == Rogue1:
            Rogue1.turn = True
        elif current_turn == e1:
            e1.turn = True
    for chara in charas:
        chara.order += chara.speed
    return "Speed_Calc"


def draw(scr, sta, p, e, hl):
    scr.fill((0, 0, 0))
    sta.draw(scr)
    if p.hit_points > 0:
        p.draw(scr)
    if hl:
        hl_rect = pygame.Rect(e.x * 24, e.y * 24, 24, 24)
        pygame.draw.rect(scr, (255, 0, 0), hl_rect, 3)
    if e.hit_points > 0:
        e.draw(scr)


pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
stage = StageCreation(1, 0, 0)
Rogue1 = Rogue(60, 50, 50, 75, 25, 3, 10, 50, 200)
e1 = Enemy(150, 50, 60, 50, 5, 10, 6, 5, 140)

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
font2 = pygame.font.Font(pygame.font.get_default_font(), 20)
text = font.render(f"HP: {Rogue1.hit_points}/{Rogue1.max_hp}", True, (255, 255, 255))
text2 = font2.render(f"Movement: {Rogue1.movement}", True, (255, 255, 255))
text3 = font2.render("1: Move", True, (255, 255, 255))
text4 = font2.render("2: Attack", True, (255, 255, 255))
text5 = font2.render("3: Crit+", True, (255, 255, 255))
text6 = font2.render("4: Rest", True, (255, 255, 255))
text7 = font2.render("5: End Turn", True, (255, 255, 255))
text8 = font2.render(f"Action Points: {Rogue1.action_points}", True, (255, 255, 255))
text9 = font2.render(f"0 to end movement", True, (255, 255, 255))
text10 = font2.render(f"CR + {Rogue1.crit_rate - Rogue1.og_crit_rate}", True, (255, 255, 255))
text11 = font2.render(f"CD + {Rogue1.crit_damage - Rogue1.og_crit_damage}", True, (255, 255, 255))
window_image = pygame.image.load("Rogue.png")
window_image = pygame.transform.scale(window_image, (96, 96))

running = True
game_state = "Speed_Calc"
highlight = False

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if Rogue1.turn:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Rogue1.move_phase = True
                elif event.key == pygame.K_2:
                    Rogue1.attack_phase = True
                elif event.key == pygame.K_3:
                    Rogue1.crit_up()
                    text10 = font2.render(f"CR + {Rogue1.crit_rate - Rogue1.og_crit_rate}", True, (255, 255, 255))
                    text11 = font2.render(f"CD + {Rogue1.crit_damage - Rogue1.og_crit_damage}", True, (255, 255, 255))
                    Rogue1.current_action_points -= 1
                    text8 = font2.render(f"Action Points: {Rogue1.current_action_points}", True, (255, 255, 255))
                    Rogue1.buffed_state = True
                elif event.key == pygame.K_4:
                    Rogue1.hit_points += 5
                    Rogue1.hit_points = min(Rogue1.hit_points, Rogue1.max_hp)
                    Rogue1.current_action_points -= 1
                    text8 = font2.render(f"Action Points: {Rogue1.current_action_points}", True, (255, 255, 255))
                elif event.key == pygame.K_5:
                    Rogue1.end_phase = True

            if Rogue1.attack_phase:
                if abs(Rogue1.x - e1.x) <= 1 and abs(Rogue1.y - e1.y) <= 1:
                    highlight = True
                    x, y = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN and highlight:
                        if x // 24 == e1.x and y // 24 == e1.y:
                            Rogue1.attack(e1)
                            highlight = False
                            Rogue1.current_action_points -= 1
                            text8 = font2.render(f"Action Points: {Rogue1.current_action_points}", True, (255, 255, 255))
                            Rogue1.attack_phase = False
                            print(e1.hit_points)
                else:
                    Rogue1.attack_phase = False

            if Rogue1.move_phase:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        Rogue1.move(0, -1, stage)
                    elif event.key == pygame.K_s:
                        Rogue1.move(0, 1, stage)
                    elif event.key == pygame.K_a:
                        Rogue1.move(-1, 0, stage)
                    elif event.key == pygame.K_d:
                        Rogue1.move(1, 0, stage)
                    text2 = font2.render(f"Movement: {Rogue1.movement}", True, (255, 255, 255))
                    if Rogue1.movement == 0 or event.key == pygame.K_0:
                        Rogue1.movement = Rogue1.max_movement
                        Rogue1.current_action_points -= 1
                        text8 = font2.render(f"Action Points: {Rogue1.current_action_points}", True, (255, 255, 255))
                        Rogue1.move_phase = False

                else:
                    Rogue1.attack_phase = False

            if Rogue1.current_action_points == 0:
                Rogue1.end_phase = True

            if Rogue1.end_phase:
                Rogue1.end_of_turn()
                Rogue1.turn = False
                Rogue1.end_phase = False

        if e1.turn:
            if not abs(e1.x - Rogue1.x) <= 1 and not abs(e1.y - Rogue1.y) <= 1:
                e1.move_phase = True
            elif abs(e1.x - Rogue1.x) <= 1 and abs(e1.y - Rogue1.y) <= 1:
                e1.attacking_phase = True

            if e1.move_phase:
                dx = dy = 0
                if e1.x < Rogue1.x:
                    dx = 1
                elif e1.x > Rogue1.x:
                    dx = -1
                if e1.y < Rogue1.y:
                    dy = 1
                elif e1.y > Rogue1.y:
                    dy = -1
                e1.move(dx, dy, stage)
                print(e1.movement)

                if e1.movement == 0 or abs(e1.x - Rogue1.x) <= 1 and abs(e1.y - Rogue1.y) <= 1:
                    e1.current_action_points -= 1
                    e1.move_phase = False
                    e1.movement = e1.max_movement

            if e1.attacking_phase:
                print("ATTACK")
                if abs(e1.x - Rogue1.x) <= 1 and abs(e1.y - Rogue1.y) <= 1:
                    e1.attack(Rogue1)
                    life_steal = round(0.75 * (Rogue1.max_hp - Rogue1.hit_points))
                    e1.hit_points += life_steal
                    e1.hit_points = min(e1.hit_points, e1.max_hp)
                    print(Rogue1.hit_points)
                e1.attacking_phase = False
                e1.current_action_points -= 1

            if e1.current_action_points == 0:
                e1.end_phase = True

            if e1.end_phase:
                e1.end_of_turn()
                e1.turn = False
                e1.end_phase = False
                print("END TURN")

        if not e1.turn and not Rogue1.turn:
            game_state = speed_order((Rogue1, e1))

    draw(screen, stage, Rogue1, e1, highlight)
    screen.blit(window_image, (650, 50))
    screen.blit(text, (750, 50))
    if Rogue1.turn and not Rogue1.move_phase and not Rogue1.attack_phase and not e1.turn:
        screen.blit(text8, (750, 100))
        screen.blit(text3, (750, 150))
        screen.blit(text4, (750, 180))
        screen.blit(text5, (750, 210))
        screen.blit(text6, (750, 240))
        screen.blit(text7, (750, 270))
    elif Rogue1.turn and Rogue1.move_phase and not Rogue1.attack_phase and not e1.turn:
        screen.blit(text2, (750, 100))
        screen.blit(text9, (750, 130))
    if Rogue1.buffed_state and not e1.turn:
        screen.blit(text10, (750, 700))
        screen.blit(text11, (750, 730))
    pygame.display.flip()

pygame.quit()
