import pygame
TILE_SIZE = 64
SPRITE_SIZE = 32

SCREEN_COLUMNS = 20
SCREEN_ROWS = 10
SCREEN_WIDTH = SCREEN_COLUMNS * TILE_SIZE
SCREEN_HEIGHT = SCREEN_ROWS * TILE_SIZE

UP = (0,-TILE_SIZE)
DOWN = (0,TILE_SIZE)
LEFT = (-TILE_SIZE,0)
RIGHT = (TILE_SIZE,0)

KEY_MAP = {
    pygame.K_UP: UP,
    pygame.K_DOWN: DOWN,
    pygame.K_LEFT: LEFT,
    pygame.K_RIGHT: RIGHT,
    pygame.K_w: UP,
    pygame.K_s: DOWN,
    pygame.K_a: LEFT,
    pygame.K_d: RIGHT

}

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

UPDATE_DELAY = 100

