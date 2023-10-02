import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH / TILE_SIZE, HEIGHT / TILE_SIZE
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
YELLOW = (255, 255, 0)

