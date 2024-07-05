from input_field import *
from draw_the_board import *
from messages import *
from database import *
import time
from visual_components import *

popup_message = None
popup_end_time = None

def display_form(screen, title, inputs, button_text):
    screen.fill(WHITE)
    title_font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 50)

    title_surface = title_font.render(title, True, BLACK)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)
    
    button_surface = button_font.render(button_text, True, BLACK)
    button_rect = button_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    
    input_boxes = []
    for i, input in enumerate(inputs):
        input_box = InputBox(WIDTH // 2 - 100, HEIGHT // 2 - 60 + (i * 60), 200, 40)
        input_boxes.append(input_box)
    
    pygame.display.flip()
    
    return input_boxes, button_surface, button_rect

def handle_form(screen, title, inputs, button_text, submit_action):
    input_boxes, button_surface, button_rect = display_form(screen, title, inputs, button_text)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    values = [input_box.text for input_box in input_boxes]
                    if submit_action(*values):
                        user = submit_action(*values)
                        done = True

            for input_box in input_boxes:
                input_box.handle_event(event)
                
        if popup_message and time.time() < popup_end_time:
            draw_popup_message(popup_message, popup_end_time)

        for input_box in input_boxes:
            input_box.draw(screen)
        
        screen.blit(button_surface, button_rect)
        pygame.display.flip()
    
    return user

def login_action(username, password):
    user = login_user(username, password)
    if user:
        print(f"Welcome back, {username}!")
        return user
    else:
        popup_message = "Username or password is incorrect"
        popup_end_time = time.time() + 2
        return None

def register_action(username, password):
    if register_user(username, password):
        print(f"Registration successful. Welcome, {username}!")
        return login_action(username, password)
    else:
        popup_message = "User already registered"
        popup_end_time = time.time() + 2
        return None
