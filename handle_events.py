from main import *
from draw_the_board import *
from sudoku_solver import *
import sys
from messages import *

def handle_events(board, selected):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Checking if the board is solvable...")
            if solve_sudoku(board):
                print("Board is solvable:")
                print_board(board)
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
                
                if event.unicode.isdigit():
                    num = int(event.unicode)
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                    else:
                        draw_popup_message(f"Cannot place {num} at ({row}, {col}). Invalid move.")
                
                if event.key == pygame.K_LEFT and col > 0:
                    col -= 1
                elif event.key == pygame.K_RIGHT and col < 8:
                    col += 1
                elif event.key == pygame.K_UP and row > 0:
                    row -= 1
                elif event.key == pygame.K_DOWN and row < 8:
                    row += 1
                
                selected = (row, col)
    
    return selected
