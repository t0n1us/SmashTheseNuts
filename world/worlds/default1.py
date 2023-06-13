import pygame
from world.map import Map
from world.objects.block import Block


class Default1(Map):
    def __init__(self, window: pygame.Surface, window_w, window_h, players):
        super().__init__(window, window_w, window_h, players)
        self.BLOCKS = [Block(self.window, 250, self.height - 100, 900, traversable=False),
                       Block(self.window, 300, self.height - 350, 200),
                       Block(self.window, 800, self.height - 350, 200),
                       Block(self.window, 450, self.height - 500, 400)]

    def _render_objects(self):
        for block in self.BLOCKS:
            block.render()
