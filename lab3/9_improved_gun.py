import math
from random import choice
from random import randint
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
BOMB_COLORS = [RED, YELLOW]

WIDTH = 800
HEIGHT = 600

dt = 1
g = 0.1
score = 0
x = 150
y = 470

def draw_count():
    f1 = pygame.font.Font(None, 30)
    text1 = f1.render(str(score), True, BLACK)
    text2 = f1.render("score:", True, BLACK)
    screen.blit(text1, (460, 50))
    screen.blit(text2, (400, 50))

def draw_instruction():
    f2 = pygame.font.Font(None, 20)
    text3 = f2.render("For fire with balls tap B", True, BLACK)
    text4 = f2.render("For fire with torpedos tap V", True, BLACK)
    text5 = f2.render("Hit the black target to", True, BLACK)
    text6 = f2.render("get 5 points", True, BLACK)
    text7 = f2.render("Try not to hit yourself, escape bombs!", True, BLACK)
    text8 = f2.render("Move your tank with right and left arrows", True, BLACK)
    text9 = f2.render("Your enemy can move his own tank with D", True, BLACK)
    text10 = f2.render("and A (left and right) and fire with S in you", True, BLACK)
    screen.blit(text3, (550, 50))
    screen.blit(text4, (550, 80))
    screen.blit(text5, (550, 120))
    screen.blit(text6, (550, 130))
    screen.blit(text7, (550, 160))
    screen.blit(text8, (550, 190))
    screen.blit(text9, (50, 50))
    screen.blit(text10, (50, 70))

m_x = 0
m_y = 0
def get_mouse_position():
    pos = pygame.mouse.get_pos()
    m_x = pos[0]
    m_y = pos[1]


class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 30
        self.vy = 30
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx * dt
        self.y += self.vy * dt - g * dt**2 / 2
        self.vy += g*dt

        if self.x > 790 or self.x < 10:
            self.vx = - self.vx
        self.color = GAME_COLORS[randint(0, 5)]

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if abs(self.x - obj.x) < self.r + obj.r:
            if abs(self.y - obj.y) < self.r + obj.r:
                return True
            else:
                return False
        else:
            return False

    def hittest_yrslf(self, obj):
        if abs(self.x - obj.x) < self.r + 10:
            if abs(self.y - obj.y) < self.r + 10:
                return True
            else:
                return False
        else:
            return False
        
class Torpedo:
    
    
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.length = 10
        self.vx = 1000
        self.vy = 1000
        self.color = choice(GAME_COLORS)
        self.live = 30
        
    def move_tor(self):
        self.x += 3 * self.vx * dt
        self.y += 3 * self.vy * dt
        self.color = GAME_COLORS[randint(0, 5)]
    def draw_tor(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - self.length / 2 , self.y + 5),
                (self.x + self.length / 2 , self.y + 5),
                (self.x + self.length / 2 , self.y - 5),
                (self.x - self.length / 2 , self.y - 5)
                ])
            
    def hittest(self, obj):
        if abs(self.x - obj.x) < self.length + obj.r:
            if abs(self.y - obj.y) < self.length + obj.r:
                return True
            else:
                return False
        else:
            return False
        
    def hittest_yrslf(self, obj):
        if abs(self.x - (obj.x+60)) < self.length + 50:
            if abs(self.y - (obj.y+30)) < self.length + 50:
                return True
            else:
                return False
        else:
            return False

class Bomb:
    def __init__(self, screen):
        self.screen = screen
        self.color = GREY
        self.x = randint(10, 700)
        self.y = 10
        self.r = 30
        self.vy = 30

    def move_bomb(self):
        self.y += self.vy * dt
        self.color = BOMB_COLORS[randint(0, 1)]

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)
        
    def hittest(self, obj):
        if abs(self.x - obj.x) < self.r:
            if abs(self.y - obj.y) < self.r + 30:
                return True
            else:
                return False
        else:
            return False

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 50
        self.y = 460
        self.vx = 5

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bombs, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x + 120, self.y + 20)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        new_bomb = Bomb(self.screen)
        bombs.append(new_bomb)

    def fire3_end(self, event):
        global torpedos, bullet, bombs
        bullet += 1
        new_torpedo = Torpedo(self.screen, self.x + 120, self.y + 20)
        new_torpedo.length += 10
        self.an = math.atan2((event.pos[1]-new_torpedo.y), (event.pos[0]-new_torpedo.x))
        new_torpedo.vx = self.f2_power * math.cos(self.an)
        new_torpedo.vy = self.f2_power * math.sin(self.an)
        torpedos.append(new_torpedo)
        self.f2_on = 0
        self.f2_power = 10
        new_bomb = Bomb(self.screen)
        bombs.append(new_bomb)

    def fire4_end(self):
        global torpedos, bullet, bombs
        bullet += 1
        new_torpedo = Torpedo(self.screen, self.x + 120, self.y + 20)
        new_torpedo.length += 10
        new_torpedo.vx = randint(1, 10)
        new_torpedo.vy = randint(-10, 10)
        torpedos.append(new_torpedo)
        self.f2_on = 0
        self.f2_power = 10
        

    ''''def enemy_fire(self, event):
        global torpedos, bullet
        bullet += 1
        new_torpedo = Torpedo(self.screen, self.x + 120, self.y + 20)
        new_torpedo.length += 10
        torpedos.append(new_torpedo)
        self.f2_on = 0
        self.f2_power = 10
        new_bomb = Bomb(self.screen)
        bombs.append(new_bomb) '''
        
        
    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-460) / (event.pos[0]-50))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        tank = pygame.image.load('танк1.jpg')
        self.screen.blit(tank, (self.x - 30, self.y))
        #pygame.draw.line(self.screen, self.color, [self.x, self.y], [self.x + 10, self.y - 10], 10)


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def move_gun(self):
        self.x += self.vx * dt
    
            
class Target:
    def __init__(self):
        """ Инициализация новой цели. """
        self.screen = screen
        self.x = randint(400, 780)
        self.y = randint(300, 550)
        self.r = randint(10, 50)
        self.color = RED
        self.live = 1
        self.vy = randint(10, 20)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move_t(self):
        self.y += self.vy*dt

        if self.y > 590 or self.y < 10:
            self.vy = - self.vy

class Special:
    def __init__(self):
        """ Инициализация новой цели. """
        self.screen = screen
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(5, 10)
        self.color = BLACK
        self.live = 1
        self.vy = randint(-40, 40)
        self.vx = randint(-40, 40)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move_s(self):
        self.vy += randint(-5, 5)
        self.vx += randint(-5, 5)
        self.x += self.vx*dt
        self.y += self.vy*dt

        if self.y >= 590:
            self.vy = - self.vy - 10
        elif self.y <= 10:
            self.vy = - self.vy + 10
        elif self.x >= 690:
            self.vx = - self.vx - 10
        elif self.x <= 10:
            self.vx = - self.vx + 10

        if (self.vx**2 + self.vy**2) >= 1500:
            self.vx = self.vx / 10
            self.vy = self.vy / 10



            
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

tor_or_ball = 1 #переменная для того, чтобы понять, надо стрелять торпедой или шариком, 1 - шарик, 2 - торпеда
bullet = 0
balls = []
torpedos = []
bombs = []

clock = pygame.time.Clock()
gun = Gun(screen)
gun1 = Gun(screen)
target1 = Target()
target2 = Target()
special = Special()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    gun1.draw()
    target1.draw()
    target2.draw()
    special.draw()
    draw_count()
    draw_instruction()

    

    for b in balls:
        b.draw()
    for bomb in bombs:
        bomb.draw()

    for t in torpedos:
        t.draw_tor()
    for bomb in bombs:
        bomb.draw()
    pygame.display.update()

    


    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tor_or_ball = 1
                print('ball')
            elif event.key == pygame.K_v:
                tor_or_ball = 2
                print('torpedo')
            elif event.key == pygame.K_RIGHT:
                gun.vx = 5
                gun.move_gun()
            elif event.key == pygame.K_LEFT:
                gun.vx = -5
                gun.move_gun()
            elif event.key == pygame.K_d:
                gun1.vx = 5
                gun1.move_gun()
            elif event.key == pygame.K_a:
                gun1.vx = -5
                gun1.move_gun()
            elif event.key == pygame.K_s:
                gun1.fire4_end()
            else:
                pass
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
            
        elif event.type == pygame.MOUSEBUTTONUP and tor_or_ball == 1:
            gun.fire2_end(event)

        elif event.type == pygame.MOUSEBUTTONUP and tor_or_ball == 2:
            gun.fire3_end(event)
            
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

            
    for b in balls:
        b.move()
        if b.hittest(target1) and target1.live:
            target1.live = 0
            score += 1
            target1 = Target()
        if b.hittest(target2) and target2.live:
            target2.live = 0
            score += 1
            target2 = Target()
        if b.hittest(special) and special.live:
            special.live = 0
            score += 3
            special = Special()
        if b.hittest_yrslf(gun):
            score -= 1
            
    for t in torpedos:
        t.move_tor()
        if t.hittest(target1) and target1.live:
            target1.live = 0
            score += 1
            target1 = Target()
        if t.hittest(target2) and target2.live:
            target2.live = 0
            score += 1
            target2 = Target()
        if t.hittest(special) and special.live:
            special.live = 0
            score += 5
            special = Special()
        if t.hittest_yrslf(gun):
            score -= 1
    for bomb in bombs:
        bomb.move_bomb()
        if bomb.hittest(gun):
            score -= 1

            
    target1.move_t()
    target2.move_t()
    special.move_s()
    gun.power_up()
pygame.quit()
