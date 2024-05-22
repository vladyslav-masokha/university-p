import pygame
import random
import time

LAB_WIDTH, LAB_HEIGHT = 1280, 720
TILE = 60
cols, rows = LAB_WIDTH // TILE, LAB_HEIGHT // TILE

pygame.init()
RES = WIDTH, HEIGHT = LAB_WIDTH + 300, LAB_HEIGHT
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
BLUE = (10, 6, 125)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BUTTON_COLOR = (128, 128, 128)
TEXT_COLOR = (255, 255, 255)
BROWN = (139, 69, 19)

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.rect(sc, BLACK, (x, y, TILE, TILE))
        if self.walls['top']:
            pygame.draw.line(sc, BLUE, (x, y), (x + TILE, y), 3)
        if self.walls['right']:
            pygame.draw.line(sc, BLUE, (x + TILE, y), (x + TILE, y + TILE), 3)
        if self.walls['bottom']:
            pygame.draw.line(sc, BLUE, (x + TILE, y + TILE), (x, y + TILE), 3)
        if self.walls['left']:
            pygame.draw.line(sc, BLUE, (x, y + TILE), (x, y), 3)

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        if item_type == "key":
            self.image.fill(YELLOW)
        elif item_type == "coin":
            self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE
        self.rect.y = y * TILE
        self.item_type = item_type

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def generate_maze():
    grid_cells = [[Cell(col, row) for row in range(rows)] for col in range(cols)]
    stack = []
    current_cell = grid_cells[0][0]
    current_cell.visited = True
    stack.append(current_cell)

    while stack:
        current_cell = stack[-1]
        neighbors = []
        x, y = current_cell.x, current_cell.y

        if x > 0 and not grid_cells[x - 1][y].visited:
            neighbors.append(grid_cells[x - 1][y])
        if x < cols - 1 and not grid_cells[x + 1][y].visited:
            neighbors.append(grid_cells[x + 1][y])
        if y > 0 and not grid_cells[x][y - 1].visited:
            neighbors.append(grid_cells[x][y - 1])
        if y < rows - 1 and not grid_cells[x][y + 1].visited:
            neighbors.append(grid_cells[x][y + 1])

        if neighbors:
            next_cell = random.choice(neighbors)
            remove_walls(current_cell, next_cell)
            next_cell.visited = True
            stack.append(next_cell)
        else:
            stack.pop()

    items_group = pygame.sprite.Group()
    for i in range(10):
        x, y = random.randint(1, cols - 2), random.randint(1, rows - 2)
        item_type = random.choice(["key", "coin"])
        item = Item(x, y, item_type)
        items_group.add(item)

    return grid_cells, items_group

def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False

    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

def draw_maze(grid_cells):
    for col in grid_cells:
        for cell in col:
            cell.draw()

def draw_player(player_pos):
    x, y = player_pos
    x *= TILE
    y *= TILE

    pygame.draw.circle(sc, YELLOW, (x + 30, y + 30), 15)

def draw_button(text, x, y, width, height):
    pygame.draw.rect(sc, BUTTON_COLOR, (x, y, width, height))
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    sc.blit(text_surface, text_rect)

def button_clicked(x, y, width, height):
    mouse_pos = pygame.mouse.get_pos()
    return x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height

def display_message(message, color=RED):
    font = pygame.font.Font(None, 74)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(LAB_WIDTH // 2, LAB_HEIGHT // 2))
    sc.blit(text_surface, text_rect)
    pygame.display.flip()

def restart_game():
    maze, items_group = generate_maze()
    player_x, player_y = 0, 0
    finish_x, finish_y = cols - 1, rows - 1
    maze[finish_x][finish_y].walls['bottom'] = False
    start_time = time.time()
    return maze, player_x, player_y, finish_x, finish_y, start_time, items_group

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE
        self.rect.y = y * TILE

    def update(self, x, y):
        self.rect.x = x * TILE
        self.rect.y = y * TILE

def draw_menu():
    sc.fill(BLACK)
    draw_button("Start", WIDTH // 2 - 80, HEIGHT // 2 - 30, 160, 60)
    draw_button("Exit", WIDTH // 2 - 80, HEIGHT // 2 + 40, 160, 60)

def main():
    running = True
    start_game = False
    game_over = False
    maze = None
    player_x, player_y = 0, 0
    finish_x, finish_y = cols - 1, rows - 1
    start_time = None
    score = 0
    items_group = None

    player_sprite = Player(player_x, player_y)
    player_group = pygame.sprite.Group()
    player_group.add(player_sprite)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not start_game:
                    if button_clicked(WIDTH // 2 - 80, HEIGHT // 2 - 30, 160, 60): 
                        start_game = True
                        game_over = False
                        maze, items_group = generate_maze()
                        player_x, player_y = 0, 0 
                        finish_x, finish_y = cols - 1, rows - 1
                        maze[finish_x][finish_y].walls['bottom'] = False
                        start_time = time.time()
                    elif button_clicked(WIDTH // 2 - 80, HEIGHT // 2 + 40, 160, 60):
                        running = False
                else:
                    if button_clicked(LAB_WIDTH + 20, HEIGHT - 70, 80, 30):
                        maze, player_x, player_y, finish_x, finish_y, start_time, items_group = restart_game()
                        player_sprite.update(player_x, player_y)
                        game_over = False
                    elif button_clicked(LAB_WIDTH + 200, HEIGHT - 70, 80, 30):
                        running = False
                    elif button_clicked(LAB_WIDTH + 110, HEIGHT - 70, 80, 30):
                        start_game = False

            elif event.type == pygame.KEYDOWN and start_game and not game_over:
                if event.key == pygame.K_UP:
                    if player_y > 0 and not maze[player_x][player_y].walls['top']:
                        player_y -= 1
                elif event.key == pygame.K_DOWN:
                    if player_y < rows - 1 and not maze[player_x][player_y].walls['bottom']:
                        player_y += 1
                elif event.key == pygame.K_LEFT:
                    if player_x > 0 and not maze[player_x][player_y].walls['left']:
                        player_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if player_x < cols - 1 and not maze[player_x][player_y].walls['right']:
                        player_x += 1

        if start_game and not game_over:
            player_sprite.update(player_x, player_y)

            if player_x == finish_x and player_y == finish_y:
                sc.fill(BLACK)
                display_message("You Win!", WHITE)
                pygame.time.wait(2000)
                game_over = True

            hits = pygame.sprite.spritecollide(player_sprite, items_group, True)
            for hit in hits:
                if hit.item_type == "key":
                    score += 5
                elif hit.item_type == "coin":
                    score += 10

            sc.fill(WHITE)
            draw_maze(maze)
            draw_player((player_x, player_y))
            items_group.draw(sc)

            font = pygame.font.Font(None, 54)
            score_surface = font.render(f"Score: {score}", True, BLACK)
            sc.blit(score_surface, (LAB_WIDTH + 20, HEIGHT - 600))

            draw_button("Restart", LAB_WIDTH + 20, HEIGHT - 70, 80, 30)
            draw_button("Menu", LAB_WIDTH + 110, HEIGHT - 70, 80, 30)
            draw_button("Exit", LAB_WIDTH + 200, HEIGHT - 70, 80, 30)

            if start_time is not None:
                elapsed_time = time.time() - start_time
                font_small = pygame.font.Font(None, 24)
                time_surface = font_small.render("Time: {:.2f}".format(elapsed_time), True, BLACK)
                sc.blit(time_surface, (LAB_WIDTH + 20, HEIGHT - 100))

            pygame.draw.rect(sc, BLACK, (0, 0, LAB_WIDTH, LAB_HEIGHT), 4)

            if start_time is not None and elapsed_time >= 60:
                display_message("Time's Up! You Lose!")
                pygame.time.wait(2000)
                game_over = True

        elif game_over:
            draw_button("Restart", LAB_WIDTH + 20, HEIGHT - 70, 80, 30)
            draw_button("Menu", LAB_WIDTH + 110, HEIGHT - 70, 80, 30)
            draw_button("Exit", LAB_WIDTH + 200, HEIGHT - 70, 80, 30)

        else:
            draw_menu()

        pygame.display.flip()
        clock.tick()

    pygame.quit()

if __name__ == "__main__":
    main()
