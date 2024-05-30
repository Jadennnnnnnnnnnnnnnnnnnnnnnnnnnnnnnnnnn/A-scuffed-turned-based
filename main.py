from world import StageCreation
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
stage = StageCreation(1, 0, 0)
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    stage.draw(screen)
    pygame.display.flip()

pygame.quit()
