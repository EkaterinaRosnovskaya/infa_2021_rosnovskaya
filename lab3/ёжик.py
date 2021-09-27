import pygame
from pygame.draw import *
pygame.init()

clock = pygame.time.Clock()

FPS = 30
screen = pygame.display.set_mode((600, 800))

rect(screen, (44, 160, 90), (0, 0, 600, 600))
rect(screen, (108, 93, 83), (0, 600, 600, 400))
rect(screen, (212, 170, 83), (0, 0, 50, 650))
rect(screen, (212, 170, 83), (400, 0, 50, 650))
rect(screen, (212, 170, 83), (500, 0, 30, 700))
rect(screen, (212, 170, 83), (90, 0, 70, 730))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
