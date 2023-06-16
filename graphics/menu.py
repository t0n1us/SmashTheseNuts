from graphics.button import Button
from main import pygame
from main import run
import sys

WINDOW_DIMSENSION_X = 1400
WINDOW_DIMSENSION_Y = 800


def get_font(size):
    pygame.font.init()
    return pygame.font.SysFont('Comic Sans MS', size)


def menu():
    # screen setting
    pygame.display.set_caption("Menu")
    window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    background = pygame.image.load("graphics/assets/menu/Background.png")
    background = pygame.transform.scale(background, (WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    while True:
        window.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("graphics/assets/menu/Play_Rect.png"), pos=(WINDOW_DIMSENSION_X/2, 250),
                             text_input="PLAY", font=get_font(75), base_color="#FFFFFF", hovering_color="lightgreen")
        OPTIONS_BUTTON = Button(image=pygame.image.load("graphics/assets/menu/Options_Rect.png"), pos=(WINDOW_DIMSENSION_X/2, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#FFFFFF", hovering_color="orange")
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/assets/menu/Quit_Rect.png"), pos=(WINDOW_DIMSENSION_X/2, 550),
                             text_input="QUIT", font=get_font(75), base_color="#FFFFFF", hovering_color="red")

        window.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def options():
    pygame.display.set_caption("Options")
    window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        window.fill("black")
        # image
        back_img = pygame.image.load('graphics/assets/menu/button_back.png').convert_alpha()
        audio_img = pygame.image.load('graphics/assets/menu/button_audio.png')

        # button
        back_button = Button(back_img, pos=(WINDOW_DIMSENSION_X/2, 500), text_input='', font=get_font(75), base_color="white",
                             hovering_color="Green")

        back_button.changeColor(OPTIONS_MOUSE_POS)
        back_button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(OPTIONS_MOUSE_POS):
                    menu()

        pygame.display.update()

def nbOfPlayer():
    pass

def mapSelection():
    pass
