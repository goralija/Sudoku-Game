from main import *
from handle_events import *
from menu import *
from draw_the_board import *
from messages import *
import pygame
import sys
from database import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def display_login_menu():
    menu_running = True
    user = None
    while menu_running:
        screen.fill(WHITE)
        draw_text(screen, "Login or Register", 50, WIDTH // 2, HEIGHT // 4)
        draw_text(screen, "1. Login", 40, WIDTH // 2, HEIGHT // 2 - 30)
        draw_text(screen, "2. Register", 40, WIDTH // 2, HEIGHT // 2)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    user = login()
                elif event.key == pygame.K_2:
                    user = register()
                if user:
                    menu_running = False
    return user

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = login_user(username, password)
    if user:
        print(f"Welcome back, {username}!")
        return user
    else:
        print("Invalid username or password.")
        return None

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if register_user(username, password):
        print(f"Registration successful. Welcome, {username}!")
        return login_user(username, password)
    else:
        print("Username already exists.")
        return None

def display_stats(user):
    screen.fill(WHITE)
    draw_text(screen, f"Stats for {user[1]}", 50, WIDTH // 2, HEIGHT // 4)
    draw_text(screen, f"Wins: {user[3]}", 40, WIDTH // 2, HEIGHT // 2 - 30)
    draw_text(screen, f"Losses: {user[4]}", 40, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    pygame.time.wait(3000)  # Display for 3 seconds
