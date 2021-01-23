import pygame
from pygame import surface
from persona.alien import Alien as _alien
from persona.fighter import Fighter as _fighter
from persona.rocket import Rocket as _rocket
from generator import Generator

class Game:

    title = 'Space Invader'
    FPS = 60
    COLORS = {'WHITE':(255, 255, 255),
                'BLACK':(0, 0, 0),
                'RED':(255, 0, 0),
                'YELLOW':(255, 255, 0)
                }
    KEYS = {'KSPACE':32}
    lost = False
    alienslist = []
    rocketslist = []
    points = 0
    clock = pygame.time.Clock()

    def __init__(self, width, height) -> None:
        """__init__         

        Args:
            width ([type]): [description]
            height ([type]): [description]
        """

        self.height = height
        self.width = width

        #pygame.init()
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.title)
        counter = 0
        timelimit = 10
        done = False

        hero = _fighter(self, self.width/2, self.height - 20)
        generator = Generator(self)

        while not done:

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_LEFT]:
                hero.x -= 2  if  hero.x > 20 else 0

            elif pressed[pygame.K_RIGHT]:
                hero.x += 2 if hero.x < width - 20 else 0


            if pressed[pygame.K_UP]:
                hero.y -= 2
            elif pressed[pygame.K_DOWN]:
                hero.y +=2

            for event in pygame.event.get():
                # manage quit
                if event.type == pygame.QUIT:
                    done = True              
                # manage bullet from fighter
                if event.type == pygame.KEYDOWN and event.key == self.KEYS['KSPACE']:
                    self.rocketslist.append(_rocket(self, hero.x, hero.y))

            # ====
            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.screen.fill((0, 0, 0))

            # set persona
            hero.draw()

            for alien in self.alienslist:
                alien.draw()
                alien.checkcollision()

            for rocket in self.rocketslist:
                rocket.draw()

            print('points:', self.points)

if __name__ == '__main__':
    space = Game(800, 600)
