import random
from persona.alien import Alien as _alien



class Generator:

    def __init__(self, game):
        self.game = game
        margin = 30
        width = 50
        colors = []
        colors.append((255,255,255)) # white
        colors.append((255,0,0)) #red
        colors.append((228, 254, 60)) # yellow

        for x in range(margin, self.game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                num = random.randint(0,len(colors)-1)
                self.game.alienslist.append(_alien(self.game, x, y, colors[num]))
