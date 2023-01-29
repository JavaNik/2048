import pygame
from pygame.surface import Surface, SurfaceType

pygame.init()
size = (600, 400)

screen: Surface | SurfaceType = pygame.display.set_mode(size)
pygame.display.set_caption('My first Game')      #Задать заголовок модального окна
font = pygame.font.SysFont('constantia', 25)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0 ,0)
FPS = (150)

direct_x = 1
direct_y = 1

direct_z = 1
direct_q = 1

follow = font.render('Уважаемый гость', 1, RED, GREEN)
like = font.render('Добро пожаловать', 1, GREEN, BLUE)
width, height = like.get_size()
x, y = 0, 300
z, q = 0, 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)
    screen.fill(BLACK)
    screen.blit(follow,(z, q))
    screen.blit(like, (x, y))
    x+=direct_x
    if x+width>=600 or x<0:     #Проверка правой границы текста
        direct_x = -direct_x


    y += direct_y
    if y + height >= 400 or y < 0:  # Проверка правой границы текста
        direct_y = -direct_y

    z += direct_z
    if z + width >= 600 or z < 0:  # Проверка правой границы текста
        direct_z = -direct_z

    q += direct_q
    if q + height >= 400 or q < 0:  # Проверка правой границы текста
        direct_q = -direct_q
    pygame.display.update()

