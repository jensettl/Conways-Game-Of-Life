import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH / TILE_SIZE, HEIGHT / TILE_SIZE
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# draw_grid
def draw_grid(positions):
    for position in positions:
        x, y = position
        pygame.draw.rect(
            screen, YELLOW, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )

    for x in range(0, WIDTH, TILE_SIZE):  # 0, 20, 40, 60, ..., 780
        pygame.draw.line(screen, GREY, (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, GREY, (0, y), (WIDTH, y))


# Main loop
def main():
    running = True
    positions = set()

    while running:
        clock.tick(FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE

                if (col, row) in positions:
                    positions.remove((col, row))
                else:
                    positions.add((col, row))

        # Update
        # Draw
        screen.fill(BLACK)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
