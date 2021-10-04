import numpy as np
import pygame
from pygame.draw import *
pygame.init()
#цвета
brown = (75, 55, 55)
black = (0, 0, 0)
grey = (80, 80, 80)
red = (255, 0, 0)
green = (44, 160, 90)
browngrey = (108, 93, 83)
yellow = (212, 170, 83)

clock = pygame.time.Clock()

FPS = 30
screen = pygame.display.set_mode((600, 800))


def yozh(xo, yo, screen, size, x0_needle, dx_needle, dy_needle, y0_needle, alfa, d_alfa, gamma, d, l):
    """
    отрисовка ежа с регулированием его размера и позиции
    xo,yo-координаты левого верхнего конца туловища,относительно него высчитываются координаты всех других частей ежа
    size-число, показывающее во сколько раз сжимается еж
    alfa-начальный угол 
    d_alfa-угол поворота за один шаг 
    l-боковые стороны 
    d-основание
    gamma-угол между основанием и боковой стороной
    """
    #отрисовка туловища
    ellipse(screen, brown, (xo, yo, 210 / size, 90 / size))
    ellipse(screen, black, (xo, yo, 210 / size, 90 / size), 3)
    #отрисовка иголок
    alfa = 14
    d_alfa = 0.3
    l = 100 / size
    d = 20 / size
    #координаты точки относительно которой вращаются иголки  
    x0_needle = xo + 10 / size
    y0_needle = yo + 20 / size
    #длины шага
    dx_needle = 10 / size
    dy_needle = 15 / size
    gamma = np.arccos(d / (2 * l))
    
    for i in range(5, 14):
        for j in range(5):
            polygon(screen, grey , [((x0_needle + i * dx_needle) + d * np.cos(alfa + i * d_alfa), (y0_needle + j * dy_needle) + d * np.sin(alfa + i * d_alfa)),
                                           ((x0_needle + i * dx_needle) - l * np.cos(180 - (alfa + i * d_alfa + gamma)), (y0_needle + j * dy_needle) + l * np.sin(180 - (alfa + i * d_alfa + gamma))),
                                           ((x0_needle + i * dx_needle), (y0_needle + j * dy_needle))])
            polygon(screen, black, [((x0_needle + i * dx_needle) + d * np.cos(alfa + i * d_alfa), (y0_needle + j * dy_needle) + d * np.sin(alfa + i * d_alfa)),
                                           ((x0_needle + i * dx_needle) - l * np.cos(180 - (alfa + i * d_alfa + gamma)), (y0_needle + j * dy_needle) + l * np.sin(180 - (alfa + i * d_alfa + gamma))),
                                           ((x0_needle + i * dx_needle), (y0_needle + j * dy_needle))], 1)
            
    #яблоко
    circle(screen, red, (xo+80/size, yo), 30/size)
    
    #иголки поверх яблока
    alfa = 14
    x0_needle = xo+10/size
    y0_needle = yo+20/size
    for i in range(5, 10):
        for j in range(3, 5):
            polygon(screen, grey, [((x0_needle+i*dx_needle)+d*np.cos(alfa+i*d_alfa), (y0_needle+j*dy_needle)+d*np.sin(alfa+i*d_alfa)),
                                           ((x0_needle+i*dx_needle)-l*np.cos(180-(alfa+i*d_alfa+gamma)), (y0_needle+j*dy_needle)+l*np.sin(180-(alfa+i*d_alfa+gamma))),
                                           ((x0_needle+i*dx_needle), (y0_needle+j*dy_needle))])
            polygon(screen, black, [((x0_needle+i*dx_needle)+d*np.cos(alfa), (y0_needle+j*dy_needle)+d*np.sin(alfa+i*d_alfa)),
                                           ((x0_needle+i*dx_needle)-l*np.cos(180-(alfa+i*d_alfa+gamma)), (y0_needle+j*dy_needle)+l*np.sin(180-(alfa+i*d_alfa+gamma))),
                                           ((x0_needle+i*dx_needle), (y0_needle+j*dy_needle))], 1)
    
    #голова
    ellipse(screen, brown, (xo+190/size, yo+30/size, 60/size, 50/size))
    ellipse(screen, black, (xo+190/size, yo+30/size, 60/size, 50/size), 1)
    
    #лапки
    ellipse(screen, brown, (xo+50/size, yo+80/size, 40/size, 30/size))
    ellipse(screen, black, (xo+50/size, yo+80/size, 40/size, 30/size), 1)
    ellipse(screen, brown, (xo+150/size, yo+80/size, 40/size, 30/size))
    ellipse(screen, black, (xo+150/size, yo+80/size, 40/size, 30/size), 1)

    #глаз и нос
    ellipse(screen, black, (xo+220/size, yo+40/size, 10/size, 10/size))
    ellipse(screen, black, (xo+245/size, yo+45/size, 20/size, 15/size))


#фон
rect(screen, green, (0, 0, 600, 600))
rect(screen, browngrey, (0, 600, 600, 400))

#деревья за ежами
rect(screen, yellow, (0, 0, 50, 650))
rect(screen, yellow, (400, 0, 50, 650))
rect(screen, yellow, (500, 0, 30, 700))

#переменные для ежей
alfa = 14
d_alfa = 0.3
l = 100
d = 20
x0_needle = 0
y0_needle = 0
dx_needle = 0
dy_needle = 0
gamma = 0

#ежи перед деревьями
yozh(340, 710, screen, 0.99, x0_needle, dx_needle, dy_needle, y0_needle, alfa, d_alfa, gamma, d, l)
yozh(510, 600, screen, 2, x0_needle, dx_needle, dy_needle, y0_needle, alfa, d_alfa, gamma, d, l)

#ёж за деревом
yozh(75, 650, screen, 1.5, x0_needle, dx_needle, dy_needle, y0_needle, alfa, d_alfa, gamma, d, l)

#дерево перед ежом
rect(screen, yellow, (90, 0, 40, 730))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
