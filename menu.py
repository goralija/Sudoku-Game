from main import *
from draw_the_board import *
import sys
from visual_components import *
from database import fetch_user_stats

def draw_menu(user):
    screen.fill((255, 238, 219))
    title_font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 50)
    
    title_surface = title_font.render("Select Difficulty", True, (0, 0, 0))
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)
    
    buttons = [
        ("Easy", (WIDTH // 2, HEIGHT // 2 - 60)),
        ("Medium", (WIDTH // 2, HEIGHT // 2)),
        ("Hard", (WIDTH // 2, HEIGHT // 2 + 60))
    ]
    
    button_rects = []
    for text, pos in buttons:
        button_surface = button_font.render(text, True, (0, 0, 0))
        button_rect = button_surface.get_rect(center=pos)
        screen.blit(button_surface, button_rect)
        button_rects.append((text.lower(), button_rect))
        
    stats = fetch_user_stats(user[1])
    if stats:
        wins, losses = stats
        stats_surface = button_font.render(f"Wins: {wins}  Losses: {losses}", True, (0, 0, 0))
        stats_rect = stats_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        screen.blit(stats_surface, stats_rect)

    pygame.display.flip()
    
    return button_rects

def menu(user):
    button_rects = draw_menu(user)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for difficulty, rect in button_rects:
                    if rect.collidepoint(pos):
                        return difficulty
