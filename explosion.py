import pygame
import objects


class Explosion(objects.GameObject):
    x = 0
    y = 0
    name = 'explosion'
    
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.animation_speed:
            self.last_update = current_time
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            if self.current_frame + 1 >= len(self.frames):
                pass # self.kill()