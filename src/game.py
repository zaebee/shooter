"""Shooter game based on pygame engine."""
import os
import math
import pygame
import random

import player
import enemy
import explosion
import objects
import splash

_config = objects._GAME


class Game:
    WIDTH = _config['WIDTH']
    HEIGHT = _config['HEIGHT']
    WHITE = (255, 255, 255)  # ffffff
    BLACK = (0, 0, 0)  # 000000
    FPS: int = 60

    def __init__(self):
        pygame.init()
        self.sound = pygame.mixer.music.load(
            os.path.join(_config ['SOUNDS'], 'space.ogg'))
        pygame.mixer.music.set_volume(0.1)
        # pygame.mixer.music.play()
        self._caption = 'Стрелялка'
        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT))

        # Load background image from _config, like: /path/to/file/images/bg.png
        self.background = pygame.image.load(
            os.path.join(_config['IMAGES'], 'bg.png'))
        self.background_rect = self.background.get_rect()

        self.hero = player.Player(
            x=self.WIDTH // 2, y=self.HEIGHT - 50)

        # TODO: spawn 10 mobs and put them into separate sprite group.
        self.enemies = pygame.sprite.Group()
        for _ in range(5):
            x = random.randint(1, self.WIDTH - 40)
            y = random.randint(1, self.HEIGHT // 2)
            # self.enemies.add(
            enemy.Enemy(x, y, [self.enemies])

    def scroll(self, img, screen, scroll_offset=0, speed=1):
        """Scrolls image background with `speed`. """
        tiles = math.ceil(screen.get_height() / img.get_height()) + 1

        for i in range(tiles):
            screen.blit(img, (0, -img.get_height() * i - scroll_offset)) 
        scroll_offset -= speed
        if abs(scroll_offset) > img.get_height(): 
            scroll_offset = 0
        return scroll_offset

    def _display_fps(self):
        pygame.display.set_caption(
            f'{self._caption} [FPS]: {self._clock.get_fps()}')

    def start(self):
        # Run main loop for game
        running = True
        bullet = None # Instance of Weapon gameObject.
        boom = None # Instance of Explosion gameObject.
        # splash.load_menu(self.screen)
        while running == True:
            self._display_fps()
            self._clock.tick(self.FPS)
            # TODO: Handles pygame events
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_a]:
                self.hero.moveLeft()
            if keys[pygame.K_d]:
                self.hero.moveRight()
            if keys[pygame.K_s]:
                self.hero.moveDown()
            if keys[pygame.K_w]:
                self.hero.moveUp()
            if keys[pygame.K_SPACE] and not bullet:
                bullet = self.hero.shoot()
            # TODO: disallow to move if X or Y out of screen size.
            for event in pygame.event.get(): # [event1, event2,]
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.BLACK)
            self.screen.blit(
                self.background, self.background_rect)
            
            self.enemies.update()
            # render bullet on the screen.
            if bullet:
                self.screen.blit(bullet.image, bullet.rect)
                bullet.update() 
            # render hero on the screen.
            self.screen.blit(
                self.hero.image, (self.hero.x, self.hero.y))

            # render enemies on the screen.
            if bullet:
                collide = pygame.sprite.spritecollide(bullet, self.enemies, False)
                for e in collide:
                    boom = explosion.Explosion(x=bullet.x, y=bullet.y)
                    self.screen.blit(boom.image, (boom.x, boom.y))
                    print('Damaged enemy: ', e)
                    #bullet.kill()
                    #e.kill()
                if bullet.is_out():
                    bullet.kill()
                    bullet = None
            
            if boom:
                boom.update()
            self.enemies.draw(self.screen)
            splash.load_score(self.screen, 0)
            pygame.display.flip()

        pygame.quit()


game = Game()
game.start()
