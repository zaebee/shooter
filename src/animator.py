import pygame

def load_frames(filename: str, width: int, height: int):
    """
        Загружает спрайт с картинкой и возвращает 
        список кадров для анимации.
        Args:
            filename - абсолютный путь до файла с кадрами.
            width - ширина кадра
            height - высота кадра
    """
    sprite = pygame.image.load(filename).convert_alpha()
    for y in range(0, sprite.get_height(), height):
        for x in range(0, sprite.get_width(), width):
            rect = pygame.Rect(x, y, width, height)
            image = pygame.Surface(rect.size, pygame.SRCALPHA)
            image.blit(sprite, (0, 0), rect)
            # frame, total = x % width, sprite.get_width() // width
            yield image # , frame, total