from abc import ABC, abstractmethod
import pygame
from player import Player


class Map(ABC):
    EDGE_WIDTH = 100
    WINDOW_BACKGROUND_COLOR = (199, 125, 255)
    PLATFORM_COLOR = (90, 24, 154)

    GRAVITY = 0.5  # px per seconds

    def __init__(self, window: pygame.Surface, window_w, window_h, players: list[Player]):
        self.window = window
        self.width = window_w
        self.height = window_h
        self.players = players

    @abstractmethod
    def _render_objects(self):
        pass

    def render(self):
        self.window.fill(self.WINDOW_BACKGROUND_COLOR)
        pygame.draw.rect(self.window, self.PLATFORM_COLOR,
                         (self.EDGE_WIDTH, self.height - 20, self.width - self.EDGE_WIDTH * 2, 20))

        self._render_objects()

        for player in self.players:
            player.set_position(player.posx, player.posy + self.GRAVITY)
            player.render()

        pygame.display.flip()
