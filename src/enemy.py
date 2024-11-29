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
    
    def update(self):
        # TODO: change y coord randomly.
        self.x += self.speed # random.randrange(-5, 5)
        
        self.y += 5 # self.speed
        if self.y > objects._config['HEIGHT']:
            self.y = 0
            self.x = random.randrange(0, objects._config['WIDTH'])
        if self.x < 0 or self.x > objects._config['WIDTH']:
            self.y = 0
            self.x = random.randrange(0, objects._config['WIDTH'])