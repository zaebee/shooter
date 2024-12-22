import os
import pygame
import animator

_GAME = {
    'WIDTH': 800,
    'HEIGHT': 600,
    'ROOT': os.path.dirname(__file__),
    'IMAGES': os.path.join(os.path.dirname(__file__), 'images'),
    'SOUNDS': os.path.join(os.path.dirname(__file__), 'sounds'),    
}

_config = _GAME

class GameObject(pygame.sprite.Sprite):
    """Base class for any game object."""
    def __init__(self, x=0, y=0, *args, **kwargs):
        # TODO: Add try/except block to catch FileNotFoundError
        super().__init__(*args)
        self.name = kwargs.get('filename', self.name)
        self.x = x
        self.y = y
        self.current_frame = 0
        self.last_update = 0
        self.animation_speed = 50 # milliseconds
        # TODO: Add try/except block to catch FileNotFoundError
        self.frames = animator.load_frames(
            os.path.join(_config['IMAGES'], f'{self.name}.png'), 96, 96)
        
        # self.image = self.frames[self.current_frame]
        self.image = next(self.frames)  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # TODO: inject sound from devices
        try:
            self.sound = pygame.mixer.Sound(
                os.path.join(_config['SOUNDS'], f'{self.name}.wav'))
        except FileNotFoundError: 
            self.sound = None