import pygame


class Block:

    def __init__(self, window, x, y, size): #size is the width of the block (not the height)
        self.window = window
        self.posx = x
        self.posy = y
        self.size = size
        self.right_edge = self.posx+self.size #position of the pixel of the block that is the most to the right

    def set_position(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def render(self):
        pygame.draw.rect(self.window, (255, 255, 255), (self.posx, self.posy, self.size, 20))
        pygame.display.update()

