import pygame

tile_size = 32


def create_tiles(r, g, b):
    tile = pygame.Surface((tile_size, tile_size))
    tile.fill((r, g, b))
    return tile


tile_colors = {
    grass: create_tiles(0, 255, 0),
    walls: create_tiles(150, 75, 0),
    wood: create_tiles(196, 164, 132)
}

tiles = [grass, walls, wood]