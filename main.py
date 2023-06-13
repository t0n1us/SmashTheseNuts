import pygame
from world.worlds.default1 import Default1
from world.map import Map
from player.player import Player


WINDOW_DIMSENSION_X = 1400
WINDOW_DIMSENSION_Y = 800
WINDOW_TITLE = "Smash These Nuts"

FPS = 1000

DEBUG_MODE = True


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

    players = [Player(window, 400, 50, 40)]

    game_map: Map = Default1(window, WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y, players)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if DEBUG_MODE:
            fps_counter = debug_font.render(f"{clock.get_fps():.0f} fps", False, (89, 89, 0))
            rect = window.blit(fps_counter, (WINDOW_DIMSENSION_X - 100, 20))
            pygame.display.update(rect)

        handle_move(players[0])
        handle_gravity(players[0])

        game_map.vertical_colision_detection()
        game_map.render()

        pygame.display.flip()  # The only flip we need


if __name__ == "__main__":
    run()
    pygame.quit()
