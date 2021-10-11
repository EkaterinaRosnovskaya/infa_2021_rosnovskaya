import numpy as np
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

#COLOURS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    "Drawing first ball"
    global x, y, r, color
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_ball_2():
    "Drawing second ball"
    global x1, y1, r1, color1
    x1 = randint(100, 700)
    y1 = randint(100, 500)
    r1 = randint(30, 50)
    color1 = COLORS[randint(0, 5)]
    circle(screen, color, (x1, y1), r1)

def ball_motion(event, x, y):
    "Replacement of first ball"
    circle(screen, color, (x, y), r)

def ball_motion_1(event, x1, y1):
    "Replacecement of second ball"
    circle(screen, color1, (x1, y1), r1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

screen.fill(BLACK)
#Variables
new_ball()
new_ball_2()
speed_x = randint(-15, 15)
speed_y = randint(-15, 15)
speed_x_1 = randint(-15, 15)
speed_y_1 = randint(-15, 15)
dt = 3
dx = 0
dy = 0
dx1 = 0
dy1 = 0
score = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Comparing of positions of the balls and mouse
            dx = np.absolute(event.pos[0] - x)
            dy = np. absolute(event.pos[1] - y)
            dx1 = np.absolute(event.pos[0] - x1)
            dy1 = np. absolute(event.pos[1] - y1)
            if (dx**2 + dy**2) <= r**2 or (dx1**2 + dy1**2) <= r**2:
                print('Success!')
                score += 1
                print('Score: ', score)
            elif (dx**2 + dy**2) > r**2 and (dx1**2 + dy1**2) > r**2:
                print ('Haha, noob!')

    screen.fill(BLACK)
    #Replacement of the balls
    x += speed_x * dt
    y += speed_y * dt
    x1 += speed_x_1 * dt
    y1 += speed_y_1 * dt
    ball_motion(event, x, y)
    ball_motion_1(event, x1, y1)
    
    #Reflection of the balls if needed
    #First ball
    if x <= r and y <= r:
        speed_x = randint(5,10)
        speed_y = randint(5,10)
    elif x >= (1200 - r) and y <= r:
        speed_x = randint(-10,-5)
        speed_y = randint(5,10)
    elif x <= r and y >= (900 - r):
        speed_x = randint(5, 10)
        speed_y = randint(-10,5)
    elif x >= (1200 - r) and y >= (900 - r):
        speed_x = randint(-10,5)
        speed_y = randint(-10,5)
    elif x <= r and r < y < (900 - r):
        speed_x = randint(5,15)
    elif x >= (1200 - r) and r < y < (900 - r):
        speed_x = randint(-15,5)
    elif y <= r and r < x < (1200 - r):
        speed_y = randint(5, 15)
    elif y >= (900 - r) and r < x < (1200 - r):
        speed_y = randint(-15,5)

    #Second ball
    if x1 <= r1 and y1 <= r1:
        speed_x_1 = randint(5,10)
        speed_y_1 = randint(5,10)
    elif x1 >= (1200 - r1) and y1 <= r1:
        speed_x_1 = randint(-10,-5)
        speed_y_1 = randint(5,10)
    elif x1 <= r1 and y1 >= (900 - r1):
        speed_x_1 = randint(5, 10)
        speed_y_1 = randint(-10,5)
    elif x1 >= (1200 - r1) and y1 >= (900 - r1):
        speed_x_1 = randint(-10,5)
        speed_y_1 = randint(-10,5)
    elif x1 <= r1 and r < y1 < (900 - r1):
        speed_x_1 = randint(5,15)
    elif x1 >= (1200 - r1) and r1 < y1 < (900 - r1):
        speed_x_1 = randint(-15,5)
    elif y1 <= r1 and r < x1 < (1200 - r1):
        speed_y_1 = randint(5, 15)
    elif y1 >= (900 - r1) and r < x1 < (1200 - r1):
        speed_y_1 = randint(-15,5)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
