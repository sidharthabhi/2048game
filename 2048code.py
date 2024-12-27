import pygame
import random
import sys

WINDOW_SIZE = 600
BACKGROUND_COLOR = (187, 173, 160)
CELL_COLOR = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
FONT_COLOR = (255, 255, 255)

pygame.init()
font = pygame.font.Font(None, 55)

class Game2048:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[0] * grid_size for _ in range(grid_size)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_tiles = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.grid[i][j] = random.choice([2, 4])

    def compress(self):
        new_grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            pos = 0
            for j in range(self.grid_size):
                if self.grid[i][j] != 0:
                    new_grid[i][pos] = self.grid[i][j]
                    pos += 1
        self.grid = new_grid

    def merge(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size - 1):
                if self.grid[i][j] == self.grid[i][j + 1] and self.grid[i][j] != 0:
                    self.grid[i][j] *= 2
                    self.score += self.grid[i][j]
                    self.grid[i][j + 1] = 0

    def reverse(self):
        new_grid = []
        for i in range(self.grid_size):
            new_grid.append([])
            for j in range(self.grid_size):
                new_grid[i].append(self.grid[i][self.grid_size - 1 - j])
        self.grid = new_grid

    def transpose(self):
        new_grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                new_grid[j][i] = self.grid[i][j]
        self.grid = new_grid

    def move_left(self):
        self.compress()
        self.merge()
        self.compress()
        self.add_new_tile()

    def move_right(self):
        self.reverse()
        self.compress()
        self.merge()
        self.compress()
        self.reverse()
        self.add_new_tile()

    def move_up(self):
        self.transpose()
        self.compress()
        self.merge()
        self.compress()
        self.transpose()
        self.add_new_tile()

    def move_down(self):
        self.transpose()
        self.reverse()
        self.compress()
        self.merge()
        self.compress()
        self.reverse()
        self.transpose()
        self.add_new_tile()

    def is_game_over(self):
        for row in self.grid:
            if 2048 in row:
                return True
        for i in range(self.grid_size):
            for j in range(self.grid_size - 1):
                if self.grid[i][j] == self.grid[i][j + 1] or self.grid[j][i] == self.grid[j + 1][i]:
                    return False
        return not any(0 in row for row in self.grid)

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                color = CELL_COLOR.get(value, (0, 0, 0))
                pygame.draw.rect(screen, color, (j * (WINDOW_SIZE // self.grid_size), i * (WINDOW_SIZE // self.grid_size), WINDOW_SIZE // self.grid_size, WINDOW_SIZE // self.grid_size))
                if value != 0:
                    text = font.render(str(value), True, FONT_COLOR)
                    text_rect = text.get_rect(center=(j * (WINDOW_SIZE // self.grid_size) + (WINDOW_SIZE // self.grid_size) // 2, i * (WINDOW_SIZE // self.grid_size) + (WINDOW_SIZE // self.grid_size) // 2))
                    screen.blit(text, text_rect)

        # Draw the score
        score_text = font.render(f"Score: {self.score}", True, FONT_COLOR)
        screen.blit(score_text, (10, 10))

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("2048 Game")
    grid_size = int(input("Select grid size (4, 5, or 6): "))
    game = Game2048(grid_size)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_UP:
                    game.move_up()
                elif event.key == pygame.K_DOWN:
                    game.move_down()

        if game.is_game_over():
            print("Game Over! Your score:", game.score)
            pygame.quit()
            sys.exit()
        game.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
