import sys
import pygame

def load_menu(screen):
    splash = pygame.Surface([500, 500])
    font = pygame.font.SysFont('arial', 20)
    # список наших кнопок: [Играть, Выход]
    buttons = [
        (160, 140, 'Играть', 0), # x=160, y=140, text='Играть', 0 - индекс
        (160, 210, 'Выход', 1)
    ]
    # сделаем мышку видимой
    pygame.mouse.set_visible(True)
    # если мы показываем splash, то done = False (основная игра не запущена)
    done = False
    item = -1 # item - это индекс кнопки, по которой мы кликаем
    while not done:
        splash.fill([0, 0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # кликнули на крестик (выход)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print(item)
                if item == 0: 
                    # кликнули по кнопке "Играть", то останавливаем цикл
                    # и прячем splash
                    # TODO: game.restart()
                    done = True
                elif item == 1: # кликнули по кнопке "Выход"
                    pygame.quit()
                    sys.exit()
        
        for button in buttons:
            # создать текст для кнопки
            btn = font.render(button[2], 1, (255, 255, 255))
            # показали текст кнопки на splash поверхности
            splash.blit(btn, [button[0], button[1]])
        
        pointer = pygame.mouse.get_pos()
        for button in buttons:
            if (pointer[0] > button[0] and pointer[0] < button[0] + 155 and 
                pointer[1] > button[1] and pointer[1] < button[1] + 50):
                item = button[3]

        # показали splash поверхность на экране    
        screen.blit(splash, [0 ,0])
        pygame.display.flip()
       
def load_score(screen, score):
    surface = pygame.Surface([250, 40]) # создаем поверхность 500х40
    font = pygame.font.SysFont('arial', 20) # создаем шрифт 'arial' размером 20px
    surface.fill([131, 35, 35]) # заливаем нашу поверхность красным цветом
    surface.set_alpha(128)
    screen.blit(surface, [0, 0]) # отображаем поверхность на экране в точке 0px, 0px
    text = font.render(f'Score: {score}', 1, [255, 0, 0]) # создаем наш текст с очками
    screen.blit(text, [10, 10]) # отображаем текст на поверхности в точке 10px, 10px
    
    
def load_health(screen, health):
    """"""
    surface = pygame.Surface([250, 40]) # создаем поверхность 500х40
    font = pygame.font.SysFont('arial', 20) # создаем шрифт 'arial' размером 20px
    surface.fill([131, 35, 35]) # заливаем нашу поверхность красным цветом
    surface.set_alpha(128)
    screen.blit(surface, [250, 0]) # отображаем поверхность на экране в точке 0px, 0px
    text = font.render(f'Health: {health}', 1, [255, 0, 0]) # создаем наш текст с очками
    screen.blit(text, [260, 10]) # отображаем текст на поверхности в точке 10px, 10px