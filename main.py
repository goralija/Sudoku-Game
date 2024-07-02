import pygame
from boards import *
from draw_the_board import *
from handle_events import *
from sudoku_solver import *
from menu import *

def main():
    while True:
        difficulty = menu()  # Get the selected difficulty from the menu
        board = fetch_new_board(difficulty)  # Fetch the board based on selected difficulty
        validity_board = make_validity_board(board)
        
        selected = None
        running = True
        while running:
            selected = handle_events(board, validity_board, selected, screen)
            draw_grid()
            if selected:
                row, col = selected
                handle_selected(board, row, col)
                if is_board_solved(board):
                    running = False
            draw_numbers(board)
            pygame.display.flip()

if __name__ == "__main__":
    main()
