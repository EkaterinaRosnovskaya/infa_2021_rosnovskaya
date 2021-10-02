import numpy as np
import pygame
from pygame.draw import *
pygame.init()

clock = pygame.time.Clock()

FPS = 30
screen = pygame.display.set_mode((600, 800))

def needle(screen, x, y, al, gam, d, l):
    polygon(screen, (80, 80, 80), [(x+d*np.cos(al), y+d*np.sin(al)), (x-l*np.cos(180-(al+gam)), y+l*np.sin(180-(al+gam))), (x,y)])
    polygon(screen, (0, 0, 0), [(x+d*np.cos(al), y+d*np.sin(al)), (x-l*np.cos(180-(al+gam)), y+l*np.sin(180-(al+gam))), (x,y)],1)

rect(screen, (44, 160, 90), (0, 0, 600, 600))
rect(screen, (108, 93, 83), (0, 600, 600, 400))
rect(screen, (212, 170, 83), (0, 0, 50, 650))
rect(screen, (212, 170, 83), (400, 0, 50, 650))
rect(screen, (212, 170, 83), (500, 0, 30, 700))
rect(screen, (212, 170, 83), (90, 0, 70, 730))
ellipse(screen, (75, 55, 55), (320, 670, 210, 90))
ellipse(screen, (0, 0, 0), (320, 670, 210, 90), 3)
al=14
dal=0.3
l=100
d=20
x0=330
y0=690
dx=10
dy=15
gam=np.arccos(d/(2*l))
for i in range(5,14):
    for j in range(5):
        needle(screen,x0+i*dx, y0+j*dy, al+i*dal, gam, d, l)
circle(screen, (255,0,0), (400, 670), 30)
for i in range(5,10):
    for j in range(3,5):
        needle(screen,x0+i*dx, y0+j*dy, al+i*dal, gam, d, l)
ellipse(screen, (75,55,55), (510,700,60,50))
ellipse(screen, (0,0,0), (510,700,60,50), 1)
ellipse(screen, (75,55,55), (370,750,40,30))
ellipse(screen, (0,0,0), (370,750,40,30), 1)
ellipse(screen, (75,55,55), (470,750,40,30))
ellipse(screen, (0,0,0), (470,750,40,30), 1)
ellipse(screen, (0,0,0), (540,710,10,10))
ellipse(screen, (0,0,0), (565,715,20,15))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
