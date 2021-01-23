import pygame
from pygame.draw import rect

class Alien:

    def __init__(self, game, x, y, color=(255, 255, 255)):
        self.game = game
        self.x = x
        self.y = y
        self.color = color
        self.colordefault = (255,255,255)
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         self.color, 
                         pygame.Rect(self.x, self.y, 30, 30))
        self.y += 0.05

    def checkcollision(self):
        for rocket in self.game.rocketslist:
            if (rocket.x < self.x + self.size and
                    rocket.x > self.x - self.size and
                    rocket.y < self.y + self.size and
                    rocket.y > self.y - self.size):
                try:
                    self.game.points +=1
                    if self.color == self.colordefault:
                        self.game.points +=1
                    else:
                        self.game.points +=5
                    
                    self.game.rocketslist.remove(rocket)                    
                    self.game.alienslist.remove(self)
                except :
                    print('')

