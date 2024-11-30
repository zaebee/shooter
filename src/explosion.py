import pygame
import objects


class Explosion(objects.GameObject):
    x = 0
    y = 0
    name = 'explosion'
    
    def update(self):
        current_time = pygame.time.get_ticks()
        framerate = 14
        # print(current_time - self.last_update > self.animation_speed)
        if current_time - self.last_update > self.animation_speed:
            self.last_update = current_time
            self.current_frame = (self.current_frame + 1) % framerate
            try:
                self.image = next(self.frames) # [self.current_frame]
            except TypeError:
                if self.current_frame <= len(self.frames) and len(self.frames):
                    self.image = self.frames[self.current_frame]
            except StopIteration:
                self.frames = []
            if self.current_frame + 1 >= framerate:
                pass # TODO: self.kill() the explosion after N times.