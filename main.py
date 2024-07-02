import pygame
from boards import *
from draw_the_board import *
from handle_events import *
from sudoku_solver import *
from menu import *

def main():
    difficulty = menu()  # Get the selected difficulty from the menu
    board = fetch_new_board(difficulty)  # Fetch the board based on selected difficulty
    
    selected = None
    running = True
    while running:
        selected = handle_events(board, selected)
        draw_grid()
        if selected:
            row, col = selected
            handle_selected(board, row, col)
        draw_numbers(board)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
