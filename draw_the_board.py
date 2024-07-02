import pygame

pygame.init()

WIDTH, HEIGHT = 738, 738
ROWS, COLS = 9, 9
SQUARE_SIZE = WIDTH // COLS
LINE_WIDTH = 2
BOLD_LINE_WIDTH = 5
FONT = pygame.font.SysFont('arial', 50)
BG_COLOR = (255, 238, 219)
LINE_COLOR = (0, 0, 0)
HIGHLIGHT_COLOR_1 = (233, 223, 223)
HIGHLIGHT_COLOR_2 = (103, 213, 249)
HIGHLIGHT_COLOR_3 = (208, 250, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def draw_grid():
    screen.fill(BG_COLOR)
    for row in range(ROWS + 1):
        if row % 3 == 0:
            width = BOLD_LINE_WIDTH
        else:
            width = LINE_WIDTH
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), width)
        pygame.draw.line(screen, LINE_COLOR, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, HEIGHT), width)

def draw_numbers(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != 0:
                text = FONT.render(str(board[row][col]), True, LINE_COLOR)
                screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE//3, row * SQUARE_SIZE + SQUARE_SIZE//6))

def get_clicked_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def get_subgrid_start(row, col):
    """ Returns the starting cell (top-left corner) of the subgrid containing the cell at (row, col) """
    subgrid_row_start = (row // 3) * 3
    subgrid_col_start = (col // 3) * 3
    return subgrid_row_start, subgrid_col_start

def get_subgrid_cells(row, col):
    """ Returns all cells in the subgrid containing the cell at (row, col) """
    subgrid_start = get_subgrid_start(row, col)
    subgrid_cells = []
    for r in range(3):
        for c in range(3):
            subgrid_cells.append((subgrid_start[0] + r, subgrid_start[1] + c))
    return subgrid_cells

def calculate_offset_selected(row, col):
    right = LINE_WIDTH
    left = LINE_WIDTH
    top = LINE_WIDTH
    bottom = LINE_WIDTH
    if col == 2 or col == 5 or col == 8:
        right = BOLD_LINE_WIDTH - 1
    if row == 2 or row == 5 or row == 8:
        bottom = BOLD_LINE_WIDTH - 1
    if col == 0 or col == 3 or col == 6:
        left = BOLD_LINE_WIDTH // 2 + 1
        right += 1
    if row == 0 or row == 3 or row == 6:
        top = BOLD_LINE_WIDTH // 2 + 1
        bottom += 1
    return left, top, right, bottom

def handle_selected(board, row, col):
    # first we highlight all the cells that have the value which is selected
    selected_value = board[row][col]
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == selected_value and selected_value != 0:
                left, top, right, bottom = calculate_offset_selected(i, j)
                pygame.draw.rect(screen, HIGHLIGHT_COLOR_3, (j * SQUARE_SIZE + left, i * SQUARE_SIZE + top, SQUARE_SIZE - right, SQUARE_SIZE - bottom))
                 
    # drawing the whole row, column and the region to which selected cell belongs
    for i in range(ROWS):
        left, top, right, bottom = calculate_offset_selected(i, col)
        pygame.draw.rect(screen, HIGHLIGHT_COLOR_1, (col * SQUARE_SIZE + left, i * SQUARE_SIZE + top, SQUARE_SIZE - right, SQUARE_SIZE - bottom))
    
    for i in range(COLS):
        left, top, right, bottom = calculate_offset_selected(row, i)
        pygame.draw.rect(screen, HIGHLIGHT_COLOR_1, (i * SQUARE_SIZE + left, row * SQUARE_SIZE + top, SQUARE_SIZE - right, SQUARE_SIZE - bottom))
    
    subgrid_cells = get_subgrid_cells(row, col)
    for cell in subgrid_cells:
        left, top, right, bottom = calculate_offset_selected(cell[0], cell[1])
        pygame.draw.rect(screen, HIGHLIGHT_COLOR_1, (cell[1] * SQUARE_SIZE + left, cell[0] * SQUARE_SIZE + top, SQUARE_SIZE - right, SQUARE_SIZE - bottom))
    
    left, top, right, bottom = calculate_offset_selected(row, col)
    pygame.draw.rect(screen, HIGHLIGHT_COLOR_2, (col * SQUARE_SIZE + left, row * SQUARE_SIZE + top, SQUARE_SIZE - right, SQUARE_SIZE - bottom))

