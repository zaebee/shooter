import random
import objects
import pygame


class Bullet(objects.GameObject):
    x = 0
    y = 0
    speed = 7
    name = 'bullet'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def update(self):
        """Updates Y coordinates every tick"""
        self.rect.y -= self.speed # self.y = self.y - self. speed
        # self.rect.x += random.randrange(-3, 3)
        if self.rect.y < 0:
            self.kill()
    
    def is_out(self):
        return self.rect.y < 0
    

class Laser(Bullet):
    """Laser is super fast."""
    speed = 12
