from main import *
from handle_events import *
from menu import *
from draw_the_board import *
from messages import *
import pygame
import sys
from database import *
from form_handle import *

def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def display_login_menu():
    menu_running = True
    user = None
    screen.fill((255, 238, 219))
    title_font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 50)

    title_surface = title_font.render("Login or Register", True, (0, 0, 0))
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)
    
    buttons = [
        ("Login", (WIDTH // 2, HEIGHT // 2 - 60)),
        ("Register", (WIDTH // 2, HEIGHT // 2))
    ]
    
    button_rects = []
    for text, pos in buttons:
        button_surface = button_font.render(text, True, (0, 0, 0))
        button_rect = button_surface.get_rect(center=pos)
        screen.blit(button_surface, button_rect)
        button_rects.append((text.lower(), button_rect))
    
    pygame.display.flip()
        
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for option, rect in button_rects:
                    if rect.collidepoint(pos):
                        if option == "login":
                            user = handle_form(screen, "Login", ["Username", "Password"], "Submit", login_action)
                        elif option == "register":
                            user = handle_form(screen, "Register", ["Username", "Password"], "Submit", register_action)
                        if user:
                            menu_running = False
    return user



def display_stats(user):
    screen.fill((255, 238, 219))
    draw_text(screen, f"Stats for {user[1]}", 50, WIDTH // 2, HEIGHT // 4)
    draw_text(screen, f"Wins: {user[3]}", 40, WIDTH // 2, HEIGHT // 2 - 30)
    draw_text(screen, f"Losses: {user[4]}", 40, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    pygame.time.wait(3000)  # Display for 3 seconds
