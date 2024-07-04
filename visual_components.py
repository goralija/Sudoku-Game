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