import os
import sys
import pygame


def load_image(name, colorkey='black'):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ["ЗАСТАВКА",
                  "Правила игры",
                  "Чемпионат",
                  "Играть Пинг-Понг",
                  "Играть Танки"]

    fon = pygame.transform.scale(load_image('fon3.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'), (0, 50, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()

        clock.tick(FPS)




pygame.init()
pygame.key.set_repeat(200, 70)

FPS = 50
STEP = 5
size = WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

tile_width = tile_height = 50


start_screen()

terminate()


