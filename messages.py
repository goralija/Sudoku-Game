from main import *
from draw_the_board import *
import pygame
import time
import sys

font = pygame.font.Font(None, 36)
def draw_popup_message(screen, message, duration=2):
    popup_width = 700
    popup_height = 100
    popup_x = (WIDTH - popup_width) // 2
    popup_y = (HEIGHT - popup_height) // 2
    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    text_surface = font.render(message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=popup_rect.center)
    
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (130, 130, 130), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 3)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

    pygame.time.wait(int(duration * 1000))
