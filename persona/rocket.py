import pygame
from pygame.draw import rect

class Rocket:

    posx = None
    posy = None

    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y


    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (255, 0, 0), 
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2

    
