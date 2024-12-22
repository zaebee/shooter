import random
import pygame
import objects


class Enemy(objects.GameObject):
    x = 0
    y = 0
    speed = random.randrange(-5, 5)
    name = 'enemy'
    
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
    
    def is_damaged(self, fireball):
        # if fireball is collided with enemy -> destroy enemy and fireball
        hit = pygame.sprite.collide_rect(self.image, fireball.image)
        if hit:
            pass
            # +1 point / -1 HP
            # TODO: destroy enemy and fireball
            # after that create Explosion.
            # TODO: create explosion.Explosion(self.x, self.y)
    
    def update(self, speed=3):
        # TODO: change y coord randomly.
        self.rect.y += speed
        
        """ self.y += 5 # self.speed"""
        if self.rect.y > 800:  # objects._config['HEIGHT']:
            self.rect.y = 0
            self.rect.x = random.randrange(0, objects._config['WIDTH'])
        if self.rect.x < 0 or self.rect.x > objects._config['WIDTH']:
            self.rect.y = 0
            self.rect.x = random.randrange(0, objects._config['WIDTH'])