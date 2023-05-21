import pygame
from world.default1 import Default1

WINDOW_DIMSENSION_X = 800
WINDOW_DIMSENSION_Y = 600
WINDOW_TITLE = "Smash These Nuts"

GAME_DELAY = 10  # In milliseconds


def run():
    pygame.init()

    window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))

    pygame.time.delay(GAME_DELAY)
    pygame.display.set_caption(WINDOW_TITLE)

    running = True
    map = Default1(window, WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        map.render()
        pygame.display.update()


if __name__ == "__main__":
    run()
    pygame.quit()
