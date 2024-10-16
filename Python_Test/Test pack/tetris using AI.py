import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define shapes
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[1, 1, 1, 1]],

    [[1, 0, 0],
     [1, 1, 1]],

    [[0, 0, 1],
     [1, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[1, 0],
     [1, 1],
     [0, 1]],

    [[0, 1],
     [1, 1],
     [1, 0]]
]

# Define class for Tetris piece
class Piece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = GRID_WIDTH // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(reversed(col)) for col in zip(*self.shape)]

# Define class for Tetris game
class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.piece = Piece(random.choice(SHAPES), random.choice([RED, WHITE]))
        self.score = 0

    def draw_grid(self, screen):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_piece(self, screen):
        for y, row in enumerate(self.piece.shape):
            for x, val in enumerate(row):
                if val == 1:
                    pygame.draw.rect(screen, self.piece.color, ((self.piece.x + x) * BLOCK_SIZE, (self.piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def update(self):
        self.piece.y += 1
        if self.check_collision():
            self.piece.y -= 1
            self.grid[self.piece.y][self.piece.x] = 1
            self.score += 1
            self.piece = Piece(random.choice(SHAPES), random.choice([RED, WHITE]))

    def check_collision(self):
        for y, row in enumerate(self.piece.shape):
            for x, val in enumerate(row):
                if val == 1 and (self.piece.x + x < 0 or self.piece.x + x >= GRID_WIDTH or self.piece.y + y >= GRID_HEIGHT or self.grid[self.piece.y + y][self.piece.x + x] == 1):
                    return True
        return False

# Create game instance
game = Tetris()

# Create Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.piece.x -= 1
            elif event.key == pygame.K_RIGHT:
                game.piece.x += 1
            elif event.key == pygame.K_DOWN:
                game.update()
            elif event.key == pygame.K_UP:
                game.piece.rotate()

    # Draw game
    screen.fill(BLACK)
    game.draw_grid(screen)
    game.draw_piece(screen)
    pygame.display.update()

    # Update game
    game.update()

    # Cap framerate
    pygame.time.delay(100)