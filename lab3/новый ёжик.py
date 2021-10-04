import numpy as np
import pygame
from pygame.draw import *
pygame.init()

clock = pygame.time.Clock()

FPS = 30
screen = pygame.display.set_mode((600, 800))

#отрисовка ежа с регулированием его размера и позиции
def yozh(xo, yo, screen, size, x0_needle, dx_needle, dy_needle, y0_needle, alfa, d_alfa, gamma, d, l):
    #туловище
    ellipse(screen, (75, 55, 55), (xo, yo, 210/size, 90/size))
    ellipse(screen, (0, 0, 0), (xo, yo, 210/size, 90/size), 3)

    #отрисовка иголок

    #угол наклона
    alfa=14
    d_alfa=0.3

    #размеры
    l=100/size
    d=20/size

    #позиции
    x0_needle=xo+10/size
    y0_needle=yo+20/size
    dx_needle=10/size
    dy_needle=15/size

    #угол между основанием и боковой стороной
    gamma=np.arccos(d/(2*l))
    
    for i in range(5,14):
        for j in range(5):
            polygon(screen, (80, 80, 80), [((x0_needle+i*dx_needle)+d*np.cos(alfa+i*d_alfa), (y0_needle+j*dy_needle)+d*np.sin(alfa+i*d_alfa)),
                                           ((x0_needle+i*dx_needle)-l*np.cos(180-(alfa+i*d_alfa+gamma)), (y0_needle+j*dy_needle)+l*np.sin(180-(alfa+i*d_alfa+gamma))),
                                           ((x0_needle+i*dx_needle),(y0_needle+j*dy_needle))])
            polygon(screen, (0, 0, 0), [((x0_needle+i*dx_needle)+d*np.cos(alfa+i*d_alfa), (y0_needle+j*dy_needle)+d*np.sin(alfa+i*d_alfa)),
                                           ((x0_needle+i*dx_needle)-l*np.cos(180-(alfa+i*d_alfa+gamma)), (y0_needle+j*dy_needle)+l*np.sin(180-(alfa+i*d_alfa+gamma))),
                                           ((x0_needle+i*dx_needle),(y0_needle+j*dy_needle))], 1)
            
    #яблоко
    circle(screen, (255,0,0), (xo+80/size, yo), 30/size)
    
    #иголки поверх яблока
    alfa=14
    x0_needle=xo+10/size
    y0_needle=yo+20/size
    for i in range(5,10):
        for j in range(3,5):
            polygon(screen, (80, 80, 80), [((x0_needle+i*dx_needle)+d*np.cos(alfa+i*d_alfa), (y0_needle+j*dy_needle)+d*np.sin(alfa+i*d_alfa)),
                                           ((x0_needle+i*dx_needle)-l*np.cos(180-(alfa+i*d_alfa+gamma)), (y0_needle+j*dy_needle)+l*np.sin(180-(alfa+i*d_alfa+gamma))),
                                           ((x0_needle+i*dx_needle),(y0_needle+j*dy_needle))])
            polygon(screen, (0, 0, 0), [((x0_needle+i*dx_needle)+d*np.cos(alfa), (y0_needle+j*dy_needle)+d*np.sin(alfa+i*d_alfa)),
                                           ((x0_needle+i*dx_needle)-l*np.cos(180-(alfa+i*d_alfa+gamma)), (y0_needle+j*dy_needle)+l*np.sin(180-(alfa+i*d_alfa+gamma))),
                                           ((x0_needle+i*dx_needle),(y0_needle+j*dy_needle))], 1)
    
    #голова
    ellipse(screen, (75,55,55), (xo+190/size,yo+30/size,60/size,50/size))
    ellipse(screen, (0,0,0), (xo+190/size,yo+30/size,60/size,50/size),1)
    
    #лапки
    ellipse(screen, (75,55,55), (xo+50/size, yo+80/size, 40/size, 30/size))
    ellipse(screen, (0,0,0), (xo+50/size, yo+80/size, 40/size, 30/size), 1)
    ellipse(screen, (75,55,55), (xo+150/size, yo+80/size, 40/size, 30/size))
    ellipse(screen, (0,0,0), (xo+150/size, yo+80/size, 40/size, 30/size), 1)

    #глаз и нос
    ellipse(screen, (0,0,0), (xo+220/size,yo+40/size,10/size,10/size))
    ellipse(screen, (0,0,0), (xo+245/size,yo+45/size,20/size,15/size))


#фон
rect(screen, (44, 160, 90), (0, 0, 600, 600))
rect(screen, (108, 93, 83), (0, 600, 600, 400))

#деревья за ежами
rect(screen, (212, 170, 83), (0, 0, 50, 650))
rect(screen, (212, 170, 83), (400, 0, 50, 650))
rect(screen, (212, 170, 83), (500, 0, 30, 700))

#переменные для ежей
alfa=14
d_alfa=0.3
l=100
d=20
x0_needle=0
y0_needle=0
dx_needle=0
dy_needle=0
gamma=0

#ежи перед деревьями
yozh(340, 710, screen, 0.99, x0_needle, dx_needle, dy_needle, y0_needle, alfa, d_alfa, gamma, d, l)
yozh(510, 600, screen, 2, x0_needle, dx_needle, dy_needle, y0_needle, alfa, d_alfa, gamma, d, l)

#ёж за деревом
yozh(75, 650, screen, 1.5, x0_needle, dx_needle, dy_needle, y0_needle, alfa, d_alfa, gamma, d, l)

#дерево перед ежом
rect(screen, (212, 170, 83), (90, 0, 40, 730))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
