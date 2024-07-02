import pygame
import sys
from boards import *
import random
from draw_the_board import *
from sudoku_solver import *
from messages import *
from menu import *

def main():
    difficulty = menu()  # Get the selected difficulty from the menu
    board = fetch_new_board(difficulty)  # Fetch the board based on selected difficulty
    
    selected = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Checking if the board is solvable...")
                if solve_sudoku(board):
                    print("Board is solvable:")
                    print_board(board)
                else:
                    print("Board is not solvable.")
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected = get_clicked_pos(pos)
            if event.type == pygame.KEYDOWN:
                if selected and event.unicode.isdigit():
                    row, col = selected
                    num = int(event.unicode)
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                    else:
                        draw_popup_message(f"Cannot place {num} at ({row}, {col}). Invalid move.")
        
        draw_grid()
        if selected:
            row, col = selected
            handle_selected(board, row, col)
        draw_numbers(board)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
