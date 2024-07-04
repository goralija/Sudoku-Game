import pygame
from boards import *
from draw_the_board import *
from handle_events import *
from sudoku_solver import *
from menu import *
from database import *
from login import *
from visual_components import *
from messages import *

def main():
    setup_database()
    user = display_login_menu()
    while True:
        selected_difficulty = menu()
        board = fetch_new_board(selected_difficulty)
        validity_board = make_validity_board(board)
        selected = None
        running = True
        while running:
            selected = handle_events(board, validity_board, selected, screen)
            
            draw_grid()
            if selected:
                row, col = selected
                handle_selected(board, row, col)
            draw_numbers(board)
            
            pygame.display.flip()
        
        if is_board_solved(board):
            update_user_stats(user[1], True)  # Update wins
            draw_popup_message("Congratulations! You solved the puzzle!")
        else:
            update_user_stats(user[1], False)  # Update losses
            draw_popup_message("Game over. Better luck next time!")

if __name__ == "__main__":
    main()
