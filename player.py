import os
import pygame

# int: 1,2,3
# float: 1.1, 3.13, math.pi
# str: 'asd', '', "", """TEST"""
# list: [1,2,3, '', 'df']
# tuple: (1,2,3)


def hello(self, args):
    return [self + 1, args[:]]


# hero = Player(filename='frog')

class Player:

    name = 'hero'
    speed = 5
    x = 300
    y = 500

    def __init__(self, filename=None, x=0, y=0):
        """Initialize hero image."""
        self.x = x
        self.y = y
        self.name = filename or self.name
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # TODO: Add try/except block to catch FileNotFoundError
        self.image = pygame.image.load(
            os.path.join(images_folder, f'{self.name}.png'))

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed


hero = Player()
print(hero.image)
