import os
import pygame
import animator

game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')


class GameObject:
    """Base class for any game object."""
    def __init__(
        self, filename=None, x=0, y=0, *args, **kwargs):
        # TODO: Add try/except block to catch FileNotFoundError
        self.name = filename or self.name
        self.x = x
        self.y = y
        self.current_frame = 0
        self.last_update = 0
        self.animation_speed = 50 # milliseconds
        # TODO: Add try/except block to catch FileNotFoundError
        self.frames = list(animator.load_frames(
            os.path.join(images_folder, f'{self.name}.png'), 96, 96))
        
        self.image = self.frames[self.current_frame]
        try:
            self.sound = pygame.mixer.Sound(
                os.path.join(sounds_folder, f'{self.name}.wav'))
        except FileNotFoundError: 
            self.sound = None