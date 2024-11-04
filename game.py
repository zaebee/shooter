"""Shooter game based on pygame engine."""
import os
import pygame
import random

import player
import enemy
import explosion
import objects
import splash

class Game:
    WIDTH = 800
    HEIGHT = 600
    WHITE = (255, 255, 255)  # ffffff
    BLACK = (0, 0, 0)  # 000000
    FPS = 60

    def __init__(self):
        pygame.init()
        self.sound = pygame.mixer.music.load(
            os.path.join(objects.sounds_folder, 'space.ogg'))
        pygame.mixer.music.set_volume(0.1)
        # pygame.mixer.music.play()
        self._caption = 'Стрелялка'
        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT))

        # Gets path for current folder and images folder.
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # Load background image from file, like: /path/to/file/images/bg.png
        self.background = pygame.image.load(
            os.path.join(images_folder, 'bg.png'))
        self.background_rect = self.background.get_rect()

        self.hero = player.Player(
            x=self.WIDTH // 2, y=self.HEIGHT - 50)

        # TODO: spawn 10 mobs and put them into separate sprite group.
        self.enemies = []
        for index in range(5):
            x = random.randint(1, self.WIDTH - 40)
            y = random.randint(1, self.HEIGHT // 2)
            self.enemies.append(enemy.Enemy(x=x, y=y))

    def _display_fps(self):
        pygame.display.set_caption(
            f'{self._caption} [FPS]: {self._clock.get_fps()}')

    def start(self):
        # Run main loop for game
        running = True
        bullet = None # Instance of Weapon gameObject.
        boom = None # Instance of Explosion gameObject.
        splash.load_menu(self.screen)
        while running == True:
            self._display_fps()
            self._clock.tick(self.FPS)
            # Handles pygame events
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_a]:
                self.hero.moveLeft()
            if keys[pygame.K_d]:
                self.hero.moveRight()
            if keys[pygame.K_s]:
                self.hero.moveDown()
            if keys[pygame.K_w]:
                self.hero.moveUp()
            if keys[pygame.K_SPACE]:
                bullet = self.hero.shoot()
                boom = explosion.Explosion(x=bullet.x, y=bullet.y)
            # TODO: disallow to move if X or Y out of screen size.
            for event in pygame.event.get(): # [event1, event2,]
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.BLACK)
            self.screen.blit(
                self.background, self.background_rect)
            
            # render bullet on the screen.
            if bullet:
                boom = explosion.Explosion(x=bullet.x, y=bullet.y)
                self.screen.blit(boom.image, (boom.x, boom.y))
                self.screen.blit(bullet.image, (bullet.x, bullet.y))
                
                bullet.update()
            if boom:
                self.screen.blit(boom.image, (boom.x, boom.y))
                boom.update() 
            # render hero on the screen.
            self.screen.blit(
                self.hero.image, (self.hero.x, self.hero.y))
            
            # render enemies on the screen.
            for enemy_object in self.enemies:
                self.screen.blit(enemy_object.image, (enemy_object.x, enemy_object.y))
                enemy_object.update()
            pygame.display.flip()

        pygame.quit()


game = Game()
game.start()
