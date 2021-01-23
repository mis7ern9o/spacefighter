import pygame
from pygame.draw import rect

class Fighter:

    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen,(255, 255, 0),
                         pygame.Rect(self.x, self.y, 8, 5))
