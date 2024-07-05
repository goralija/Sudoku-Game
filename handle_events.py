import pygame
import sys
import copy
import time
from messages import *
from sudoku_solver import *
from visual_components import *
from database import update_user_stats

def get_clicked_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def handle_events(board, validity_board, selected, screen, user):
    popup_end_time = None
    popup_message = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Checking if the board is solvable...")
            if solve_sudoku(board):
                print("Board is solvable:")
                print_board(board)
                update_user_stats(user[1], False)
            else:
                print("Board is not solvable.")
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            selected = get_clicked_pos(pos)
        
        if event.type == pygame.KEYDOWN:
            if selected:
                row, col = selected
                
                if event.unicode.isdigit() and validity_board[row][col] != 1:
                    num = int(event.unicode)
                    if is_valid(board, row, col, num):
                        board_copy = copy.deepcopy(board)
                        board_copy[row][col] = num
                        if solve_sudoku(board_copy):
                            board[row][col] = num
                        else:
                            popup_message = f"Cannot place {num} at ({row}, {col}). Invalid move."
                            popup_end_time = time.time() + 2
                    else:
                        popup_message = f"Cannot place {num} at ({row}, {col}). Invalid move."
                        popup_end_time = time.time() + 2
                
                if event.key == pygame.K_LEFT and col > 0:
                    col -= 1
                elif event.key == pygame.K_RIGHT and col < 8:
                    col += 1
                elif event.key == pygame.K_UP and row > 0:
                    row -= 1
                elif event.key == pygame.K_DOWN and row < 8:
                    row += 1
                selected = (row, col)

    if popup_message and time.time() < popup_end_time:
        draw_popup_message(screen, popup_message)
    
    return selected
