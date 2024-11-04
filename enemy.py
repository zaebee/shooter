import random
import pygame
import objects


class Enemy(objects.GameObject):
    x = 0
    y = 0
    speed = 5
    name = 'enemy'
        
    def is_damaged(self, fireball):
        # if fireball is collided with enemy -> destroy enemy and fireball
        hit = pygame.sprite.collide_rect(self.image, fireball.image)
        if hit:
            pass
            # +1 point
            # TODO: destroy enemy and fireball
            # after that create Explosion.
            # TODO: create explosion.Explosion(self.x, self.y)
    
    def update(self):
        # TODO: change y coord randomly.
        self.x += random.randrange(-5, 5)
        self.y += self.speed