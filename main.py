import pygame, sys
from button import Button
from world.worlds.default1 import Default1
from world.map import Map
from player.player import Player
from player import PlayerManager

WINDOW_DIMSENSION_X = 1400
WINDOW_DIMSENSION_Y = 800
WINDOW_TITLE = "Smash These Nuts"
game_pause = False
FPS = 999

DEBUG_MODE = True




def get_font(size):
    pygame.font.init()
    return pygame.font.SysFont('Comic Sans MS', size)

def handle_move(player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP]:
        player.jump()
    if keys[pygame.K_DOWN]:
        player.move_down()


def handle_gravity(player):  # applies gravity to the player
    if not player.vert_colision:
        player.fall_count += 0.00007
        player.y_vel += player.fall_count
        player.posy += player.y_vel


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

        PLAY_BUTTON = Button(image=pygame.image.load("graphics/assets/menu/Play_Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("graphics/assets/menu/Options_Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/assets/menu/Quit_Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

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


def get_font(size):
    pygame.font.init()
    return pygame.font.SysFont('Comic Sans MS', size)
def options():
    pygame.display.set_caption("Options")
    window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        window.fill("black")
        back_img = pygame.image.load('graphics/button_back.png').convert_alpha()
        back_button = Button(back_img, pos=(640, 460), text_input='', font=get_font(75),base_color="white", hovering_color="Green")
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



def run():
    global game_pause
    pygame.init()

    # Window stuff
    window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    pygame.display.set_caption(WINDOW_TITLE)
    window.fill("black")


    # Clock stuff
    clock = pygame.time.Clock()

    # Font stuff
    debug_font = get_font(18)

    running = True

    players = [Player(window, 400, 50, 40), Player(window, 500, 50, 40, ai_controlled=True)]

    game_map: Map = Default1(window, WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y, players)

    while running:
        dt = clock.tick(FPS)  # dt is used to get the relative time difference


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    options()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game_map.render()

        if DEBUG_MODE:
            fps_counter = debug_font.render(f"{clock.get_fps():.0f} fps", False, (89, 89, 0))
            window.blit(fps_counter, (WINDOW_DIMSENSION_X - 100, 20))

        PlayerManager.handle_move(players)
        PlayerManager.handle_gravity(players)

        game_map.vertical_colision_detection()

        pygame.display.flip()  # The only flip we need


if __name__ == "__main__":
    menu()
    pygame.quit()
