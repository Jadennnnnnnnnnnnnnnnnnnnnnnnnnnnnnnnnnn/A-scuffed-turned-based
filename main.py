from world import StageCreation
import pygame

pygame.init()
stage = StageCreation(1, 0, 0)
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    stage.draw(screen)
    pygame.display.update()

pygame.quit()
