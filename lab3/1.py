import numpy as np
import pygame
from pygame.draw import *
pygame.init()

clock = pygame.time.Clock()

FPS = 30
screen = pygame.display.set_mode((600, 800))

def needle(screen, x, y, al, gam, d, l):
    gam=d/(2*l)
    polygon(screen, (0, 0, 65), [(x,y), (x-l*np.cos(180-(al+np.arccos(gam))), y-l*np.sin(180-(al+np.arccos(gam)))), (x+d*np.cos(al), y-d*np.sin(al))])

al=-30
dal=4
l=10
d=5
x0=330
y0=700
dx=8
dy=15
gam=0
for i in range(15):
    for j in range(15):
        needle(screen,x0+i*dx, y0+j*dy, al+i*dal, gam, d, l)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
