"""Shooter game based on pygame engine."""
import os
import pygame
import random

import player


class Game:
    WIDTH = 800
    HEIGHT = 600
    WHITE = (255, 255, 255)  # ffffff
    BLACK = (0, 0, 0)  # 000000
    FPS = 60

    def __init__(self):
        pygame.init()
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
        for index in range(1, 10):
            x = random.randint(1, self.WIDTH)
            y = random.randint(1, self.HEIGHT // 2)
            self.enemies.append(player.Player('enemy', x, y))

    def _display_fps(self):
        pygame.display.set_caption(f'{self._caption} [FPS]: {
                                   self._clock.get_fps()}')

    def on_execute(self):
        # Run main loop for game
        running = True
        while running:
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
            # TODO: disallow to move if X or Y out of screen size.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.BLACK)
            self.screen.blit(
                self.background, self.background_rect)
            
            # render hero on the screen.
            self.screen.blit(
                self.hero.image, (self.hero.x, self.hero.y))
            
            # render enemies on the screen.
            for enemy in self.enemies:
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
            pygame.display.flip()

        pygame.quit()


game = Game()
game.on_execute()
