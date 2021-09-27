import pygame
from pygame.draw import *
pygame.init()

clock = pygame.time.Clock()


FPS = 30
screen = pygame.display.set_mode((400, 400))

x1=0
x2=400
y1=0
y2=400

rect(screen, (217, 217, 217), (x1, y1,x2-x1, y2-y1), 0)
circle(screen, (255, 255, 0), (200, 200), 150, 0)
circle(screen, (0, 0, 0), (200, 200), 150, 5)
rect(screen, (0, 0, 0), (80, 250, 240, 20), 0)
circle(screen, (255, 0, 0), (115, 170), 40, 0)
circle(screen, (0, 0, 0), (115, 170), 40, 5)
circle(screen, (255, 0, 0), (275, 170), 40, 0)
circle(screen, (0, 0, 0), (275, 170), 40, 5)
circle(screen, (0, 0, 0), (115, 170), 10, 0)
circle(screen, (0, 0, 0), (275, 170), 10, 0)
polygon(screen, (0,0,0), [(70,100), (70, 135), (160,155), (160, 120)], 0)
polygon(screen, (0,0,0), [(240,120), (240, 155), (330,135), (330, 100)], 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
