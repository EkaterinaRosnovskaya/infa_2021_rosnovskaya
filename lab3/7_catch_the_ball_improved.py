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
SCREEN_COLORS = [GREEN, BLUE, CYAN]


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

def new_ball_2():
    "Drawing second ball"
    global x1, y1, r1, color1
    x1 = randint(100, 700)
    y1 = randint(100, 500)
    r1 = randint(30, 50)
    color1 = COLORS[randint(0, 5)]
    circle(screen, color, (x1, y1), r1)

def new_ball_3():
    "Drawing third ball"
    global x2, y2, r2, color2
    x2 = randint(100, 700)
    y2 = randint(100, 500)
    r2 = randint(30, 50)
    color2 = COLORS[randint(0, 5)]
    circle(screen, color, (x2, y2), r2)

def ball_motion(event, x, y):
    "Replacement of first ball"
    circle(screen, color, (x, y), r)

def ball_motion_1(event, x1, y1):
    "Replacecement of second ball"
    circle(screen, color1, (x1, y1), r1)

def ball_motion_2(event, x2, y2):
    "Replacecement of third ball"
    circle(screen, color2, (x2, y2), r2)

l = 50
g = l / 4
def special_target(x_spec, y_spec):
    "Drawing special target"
    global color_spec
    color_spec = COLORS[randint(0, 5)]
    polygon(screen, color_spec, [(x_spec, y_spec - l),
                                 (x_spec + l / 4, y_spec - g),
                                 (x_spec + l, y_spec),
                                 (x_spec + g, y_spec + g),
                                 (x_spec , y_spec + l),
                                 (x_spec - g, y_spec + g),
                                 (x_spec - l, y_spec),
                                 (x_spec - g, y_spec - g)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

#Background music
pygame.mixer.music.load("Make_The_Girl_Dance_Glocken.mp3")
pygame.mixer.music.play(-1)


#Placing balls in the screen
new_ball()
new_ball_2()
new_ball_3()

#Random speeds for the balls
speed_x = randint(-15, 15)
speed_y = randint(-15, 15)
speed_x_1 = randint(-15, 15)
speed_y_1 = randint(-15, 15)
speed_x_2 = randint(-15, 15)
speed_y_2 = randint(-15, 15)

#Variables: dt for the balls' motion, dx and dy for the comparison of the
#mouse position when tapped and position of a certain ball, dx/y_spec is the
#same for the special target, score is for count the score, star_health is for
# count health of special target
dt = 3
dx = 0
dy = 0
dx1 = 0
dy1 = 0
dx2 = 0
dy2 = 0
dx_spec = 0
dy_spec = 0
x_spec = randint(100, 700)
y_spec = randint(100, 500)
score = 0
star_health = 10

#Coefficient for the balls' accceleration
k = 1

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
            dx2 = np.absolute(event.pos[0] - x2)
            dy2 = np. absolute(event.pos[1] - y2)
            if (dx**2 + dy**2) <= r**2 or (dx1**2 + dy1**2) <= r1**2 or (dx2**2 + dy2**2) <= r2**2:
                print('Success!')
                score += 1
                print('Score: ', score)
                # If the ball is catched, balls' velocities change randomly with acceleration coeff
                k += np.mod(score, 2)
                speed_x = k * randint(-15, 15)
                speed_y = k * randint(-15, 15)
                speed_x_1 = k * randint(-15, 15)
                speed_y_1 = k * randint(-15, 15)
                speed_x_2 = k * randint(-15, 15)
                speed_y_2 = k * randint(-15, 15)
            "elif (dx**2 + dy**2) > r**2 and (dx1**2 + dy1**2) > r1**2 and (dx2**2 + dy2**2) > r2**2:"
            "print ('Haha, noob!')"
           

    #Screen changes color randomly
    screen.fill(SCREEN_COLORS[randint(0, 2)])

    #Replacement of the balls
    x += speed_x * dt
    y += speed_y * dt
    x1 += speed_x_1 * dt
    y1 += speed_y_1 * dt
    x2 += speed_x_2 * dt
    y2 += speed_y_2 * dt
    ball_motion(event, x, y)
    ball_motion_1(event, x1, y1)
    ball_motion_2(event, x2, y2)


    #Emergence of special target
    if score >= 3:
        dx_spec = randint(-50, 50)
        dy_spec = randint(-50, 50)
        x_spec += dx_spec
        y_spec += dy_spec
        if x_spec <= 50 or x_spec >= 1950 or y_spec <= 50 or y_spec >= 850:
            x_spec = randint(50, 900)
            y_spec = randint(100, 800)
        special_target(x_spec, y_spec)

            

        if event.type == pygame.MOUSEBUTTONDOWN:
                dx_star = np.absolute(event.pos[0] - x_spec)
                dy_star = np.absolute(event.pos[1] - y_spec)
                if star_health > 0:
                    
                        #Reducing the star health if it is cathed
                        if (dx_star**2 + dy_star**2) <= l**2 :
                            print('Wow guuuy! Star is catched!')
                            star_health = star_health - 1
                            
                        #Healing of the star if it is killed and increasing score with 3 points
                        if star_health == 0:
                            print('You have killed the star, OMG WHY?')
                            score += 3
                            star_health = 10
                            print('Score: ', score)

        #Table with level of star health
        if star_health <= 10 and star_health >= 7 :
            rect(screen, GREEN, (x_spec - l, y_spec + l + 3, 2*l, 10))
        elif star_health <= 6 and star_health >= 3 :
            rect(screen, YELLOW, (x_spec - l, y_spec + l + 3, 4*l / 3, 10))
        elif star_health <= 2 :
            rect(screen, RED, (x_spec - l, y_spec + l + 3, 2*l / 3 , 10))

    
    #Reflection of the balls if needed
    #First ball
    if x <= r and y <= r :
        speed_x = randint(5,10)
        speed_y = randint(5,10)
    elif x >= (1200 - r) and y <= r :
        speed_x = randint(-10,-5)
        speed_y = randint(5,10)
    elif x <= r and y >= (900 - r) :
        speed_x = randint(5, 10)
        speed_y = randint(-10,5)
    elif x >= (1200 - r) and y >= (900 - r) :
        speed_x = randint(-10,5)
        speed_y = randint(-10,5)
    elif x <= r and r < y < (900 - r):
        speed_x = randint(5,15)
    elif x >= (1200 - r) and r < y < (900 - r):
        speed_x = randint(-15,5)
    elif y <= r and r < x < (1200 - r) :
        speed_y = randint(5, 15)
    elif y >= (900 - r) and r < x < (1200 - r) :
        speed_y = randint(-15,5)

    #Second ball
    if x1 <= r1 and y1 <= r1 :
        speed_x_1 = randint(5,10)
        speed_y_1 = randint(5,10)
    elif x1 >= (1200 - r1) and y1 <= r1 :
        speed_x_1 = randint(-10,-5)
        speed_y_1 = randint(5,10)
    elif x1 <= r1 and y1 >= (900 - r1) :
        speed_x_1 = randint(5, 10)
        speed_y_1 = randint(-10,5)
    elif x1 >= (1200 - r1) and y1 >= (900 - r1) :
        speed_x_1 = randint(-10,5)
        speed_y_1 = randint(-10,5)
    elif x1 <= r1 and r < y1 < (900 - r1) :
        speed_x_1 = randint(5,15)
    elif x1 >= (1200 - r1) and r1 < y1 < (900 - r1) :
        speed_x_1 = randint(-15,5)
    elif y1 <= r1 and r < x1 < (1200 - r1) :
        speed_y_1 = randint(5, 15)
    elif y1 >= (900 - r1) and r < x1 < (1200 - r1) :
        speed_y_1 = randint(-15,5)

    #Tird ball
    if x2 <= r2 and y2 <= r2 :
        speed_x_2 = randint(5,10)
        speed_y_2 = randint(5,10)
    elif x2 >= (1200 - r2) and y2 <= r2 :
        speed_x_2 = randint(-10,-5)
        speed_y_2 = randint(5,10)
    elif x2 <= r2 and y2 >= (900 - r2) :
        speed_x_2 = randint(5, 10)
        speed_y_2 = randint(-10,5)
    elif x2 >= (1200 - r2) and y2 >= (900 - r2) :
        speed_x_2 = randint(-10,5)
        speed_y_2 = randint(-10,5)
    elif x2 <= r2 and r < y2 < (900 - r2) :
        speed_x_2 = randint(5,15)
    elif x2 >= (1200 - r2) and r2 < y2 < (900 - r2) :
        speed_x_2 = randint(-15,5)
    elif y2 <= r2 and r < x2 < (1200 - r2) :
        speed_y_2 = randint(5, 15)
    elif y2 >= (900 - r2) and r < x2 < (1200 - r2) :
        speed_y_2 = randint(-15,5)

    pygame.display.update()
    screen.fill(SCREEN_COLORS[randint(0, 2)])

pygame.quit()
