from main import *
from draw_the_board import *

font = pygame.font.Font(None, 36)

def draw_popup_message(message):
    popup_width = 700
    popup_height = 100
    popup_x = (WIDTH - popup_width) // 2
    popup_y = (HEIGHT - popup_height) // 2

    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    pygame.draw.rect(screen, (130, 130, 130), popup_rect)
    pygame.draw.rect(screen, (255, 255, 255), popup_rect, 3)

    text_surface = font.render(message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=popup_rect.center)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    pygame.time.wait(3000)