import pygame
from world.map import Map


class Default1(Map):
    def __init__(self, window: pygame.Surface, window_w, window_h):
        super().__init__(window, window_w, window_h)

    def _render_objects(self):
        platform_height = 200

        pygame.draw.rect(self.window, self.PLATFORM_COLOR,
                         (self.width / 2 + 50, self.height - platform_height, 150, 20))

        pygame.draw.rect(self.window, self.PLATFORM_COLOR,
                         (self.width / 2 - 200, self.height - platform_height, 150, 20))
