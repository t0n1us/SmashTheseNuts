import pygame
from world.worlds.default1 import Default1
from world.map import Map
from player.player import Player
from player import PlayerManager


WINDOW_DIMSENSION_X = 1400
WINDOW_DIMSENSION_Y = 800
WINDOW_TITLE = "Smash These Nuts"

FPS = 999

DEBUG_MODE = True


def run():
    pygame.init()

    # Window stuff
    window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    pygame.display.set_caption(WINDOW_TITLE)

    # Clock stuff
    clock = pygame.time.Clock()

    # Font stuff
    pygame.font.init()
    debug_font = pygame.font.SysFont('Comic Sans MS', 18)

    running = True

    players = [Player(window, 400, 50, 40), Player(window, 400, 50, 40, ai_controlled=True)]

    game_map: Map = Default1(window, WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y, players)

    while running:
        dt = clock.tick(FPS)  # dt is used to get the relative time difference

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_map.render()

        if DEBUG_MODE:
            fps_counter = debug_font.render(f"{clock.get_fps():.0f} fps", False, (89, 89, 0))
            window.blit(fps_counter, (WINDOW_DIMSENSION_X - 100, 20))

        PlayerManager.handle_move(players)
        PlayerManager.handle_gravity(players)

        game_map.vertical_colision_detection()

        pygame.display.flip()  # The only flip we need


if __name__ == "__main__":
    run()
    pygame.quit()
