import os
import pygame

class Fireball:
    name = 'fireball'
    
    def __init__(self, filename=None, x=0, y=0):
        """Initialize fireball image."""
        self.x = x
        self.y = y
        self.name = filename or self.name
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # TODO: Add try/except block to catch FileNotFoundError
        self.image = pygame.image.load(
            os.path.join(images_folder, f'{self.name}.png'))
        
        def update(self):
            pass

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
