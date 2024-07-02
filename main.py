import pygame
import sys
from boards import boards
import random
from draw_the_board import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def main():
    # Choose a random element
    board = random.choice(boards)
    
    selected = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected = get_clicked_pos(pos)
            if event.type == pygame.KEYDOWN:
                #we need to check if that number can go there
                if selected and event.unicode.isdigit():
                    row, col = selected
                    board[row][col] = int(event.unicode)

        draw_grid()
        if selected:
            row, col = selected
            handle_selected(board, row, col)
        draw_numbers(board)
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
