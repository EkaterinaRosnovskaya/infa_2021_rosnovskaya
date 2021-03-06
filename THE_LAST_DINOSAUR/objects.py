import tkinter as tk
from random import *
from PIL import Image, ImageTk
import numpy as np
class Dino():
    
    def __init__(self, x_0, y_0):
        self.lives = 3 #Dino's health
        self.x = x_0 #Dino's coordinates
        self.y = y_0
        self.heart_img1 = tk.PhotoImage(file='Cuore1.png') #Dino health pics
        self.heart_img2 = tk.PhotoImage(file='Cuore2.png')
        self.heart_img3 = tk.PhotoImage(file='Cuore3.png')
        self.heart_img4 = tk.PhotoImage(file='Cuore4.png')
        self.heart_img5 = tk.PhotoImage(file='Cuore5.png')
        self.heart_img6 = tk.PhotoImage(file='Cuore6.png')
        self.heart_img7 = tk.PhotoImage(file='Cuore7.png')
        self.heart_img8 = tk.PhotoImage(file='Cuore8.png')
        self.img1 = tk.PhotoImage(file='carl1.png') #Running Dino's pics
        self.img2 = tk.PhotoImage(file='carl2.png')
        self.img3 = tk.PhotoImage(file='carl3.png')
        self.img4 = tk.PhotoImage(file='carl4.png')
        self.img5 = tk.PhotoImage(file='carl5.png')
        self.img6 = tk.PhotoImage(file='carl6.png')
        self.img7 = tk.PhotoImage(file='carl7.png')
        self.birth1 = tk.PhotoImage(file='birth1.png') #Dino hatches out, pics for the beginning of the game
        self.birth2 = tk.PhotoImage(file='birth2.png')
        self.birth3 = tk.PhotoImage(file='birth3.png')
        self.birth4 = tk.PhotoImage(file='birth4.png')
        self.birth5 = tk.PhotoImage(file='birth5.png')
        self.birth6 = tk.PhotoImage(file='birth6.png')
        self.birth7 = tk.PhotoImage(file='birth7.png')
        self.birth8 = tk.PhotoImage(file='birth8.png')
        self.birth9 = tk.PhotoImage(file='birth9.png')
        self.birth10 = tk.PhotoImage(file='birth10.png')
        self.death1 = tk.PhotoImage(file='death1.png') #Dino's death pics
        self.death2 = tk.PhotoImage(file='death2.png')
        self.death3 = tk.PhotoImage(file='death3.png')
        self.death4 = tk.PhotoImage(file='death4.png')
        self.death5 = tk.PhotoImage(file='death5.png')
        self.death6 = tk.PhotoImage(file='death6.png')
        self.death7 = tk.PhotoImage(file='death7.png')
        self.after_death = tk.PhotoImage(file='gameover2.png') #"GAME OVER" pic
        self.type_ = "dino"
        self.vy = 50 #Dino's initial speed for jump
        self.vx = 10 #Dino's speed for running
        self.right_flag = 0 #Flag for the running to the right animation
        self.left_flag = 0 #Same for left
        self.jump_flag = 0 #Same for jump
        self.level_flag = 0 #Flag for jump on the "floor"
        ###
        self.start_y = y_0 #Initial level of jump, can be changed whan jumping on the "floor"
        self.fall_vy = 0 #Initial speed of fall from the "floor" to the ground
        self.fall_flag = 0 #Flag for that fall
        self.eggs_number = 0 #Eggs counter
        
    def move_left(self, dt):
        """Makes Dino to move to the left, dt - time step for motion"""
        if self.x >= 5:
            self.vx = -10
            self.x += self.vx * dt
        else:
            pass
        
    def move_right(self, dt):
        """Makes Dino to move to the right, dt - time step for motion"""
        if self.x >= 5:        
        if self.x <= 715:
            self.vx = 10
            self.x += self.vx * dt
        else:
            pass

    def jump(self, dt, g):
        """Makes Dino to move to jump, dt - time step for motion, g - graviational acceleration"""
        self.y = self.y - self.vy * dt + g * dt**2 / 2
        self.vy += g * dt
        
    def change_right_flag(self, x):
        """Changes flag of right-run"""
        if x:
            self.right_flag = 1
        else:
            self.right_flag = 0
            
    def change_left_flag(self, x):
        """Changes flag of left-run"""
        if x:
            self.left_flag = 1
        else:
            self.left_flag = 0

    def change_jump_flag(self, x):
        """Changes flag of jump"""
        if x:
            self.jump_flag = 1
        else:
            self.jump_flag = 0
            
    def change_of_level_test(self, obj):
        """Changes initial level of jump"""
        if self.y <= obj.y and obj.x <= self.x <= (obj.x + obj.length):
            self.start_y = obj.y - 25
            
    def return_of_level_test(self, obj):
        """Changes "floor" flag to check if Dino is not on the certain "floor" """
        if not(obj.x <= self.x <= (obj.x + obj.length)):
            obj.fall_flag = 1
            
    def return_of_level_test_1(self, obj):
        """Changes "floor" flag to check if Dino is on the certain "floor" """
        if (obj.x <= self.x <= (obj.x + obj.length)):
            obj.fall_flag = 0    
            
    def fall(self, dt, g):
        """Makes Dino to fall from the "floor" """
        self.y = self.y - self.fall_vy * dt + g * dt**2 / 2
        self.fall_vy += g * dt 
        
    def death(self,obj):
        """Reduces Dino's health when it interacts with enemies"""
        if self.x >= obj.x - 45 and self.x <=  obj.x + 45 and self.y >=  obj.y - 45 and self.y <=  obj.y + 45 and self.hit_flag == 0:
            self.lives -= 1
            self.hit_flag = 1
            print(self.hit_flag)
        else:
            self.hit_flag = 0
            
class Floor():
    
    def __init__(self, number):
        
        self.y = 300 #Height of floor placement
        self.number = number #Floor identical number
        self.x = 720 + (self.number - 1)*240 #Initial x coordinate
        self.length = randint(100, 200) #Floor length
        self.type_ = "floor"
        self.width = 10 #Floor width
        self.fall_flag = 0 #Fall flag for check if Dino on the certin floor or not
        self.img = Image.open('grace.png') #Floor pic
        self.img_resized = self.img.resize((self.length, 20)) #Resizing according to the length
        self.pic = ImageTk.PhotoImage(self.img_resized) #Final pic
        
    def free_mind(self, obj1, obj2, obj3):
        """Changes Dino's initial level of jump if Dino is not on the one of the floors"""
        if self.fall_flag == 1 and (obj1.fall_flag == 1 and obj2.fall_flag == 1):
            if  obj3.y <= self.y:
                obj3.fall_flag = 1
                obj3.start_y = 385
                
class Meteors():
    def __init__(self):
        self.type_ = "meteor"
        self.x= randint(500,730) #Initial x coordinate
        self.y = -10 #Initial y coordinate
        self.vx = randint(-10, -5) #Speed in x direction
        self.vy = 0 #initial speed in y direction
        self.angle = np.arctan(self.vy/self.vx) #Angle to the vertical axis
        self.image = Image.open('meteor.png')
        self.size = randint(5,7) #Scale factor
        self.image_resized1 = self.image.resize((20*self.size, 20*self.size))
        self.image_resized = self.image_resized1.rotate((90 - self.angle)/np.pi*180)
        self.pic = ImageTk.PhotoImage(self.image_resized)
        
    def move(self,dt,g):
        """Makes meteor to fall and changes angle of picture according to the velocity direction"""
        self.x += self.vx*dt
        self.vy -= g*dt
        self.y += self.vy*dt - g*dt**2/2
        self.angle = np.arctan(self.vy/self.vx)
        self.image_resized1 = self.image.resize((self.size*20, self.size*20))
        self.image_resized = self.image_resized1.rotate((90 - self.angle)/np.pi*180)
        self.pic = ImageTk.PhotoImage(self.image_resized)        

    def explosion(self,obj,y_0):
        """BOOM when fell on the ground"""
        if obj.y + 5 >= self.y and obj.y - 5 <= self.y and obj.x >= self.x and obj.x + obj.length <= self.x or self.y > y_0 - 5:
            self.image = Image.open('explosion.png')
            self.image_resized = self.image.resize((self.size*20, self.size*20))
            self.pic = ImageTk.PhotoImage(self.image_resized)
            if obj.y - 5 >= self.y and obj.y - 10 <= self.y and obj.x >= self.x and obj.x + obj.length <= self.x or self.y > y_0 - -10:
                self.size = randint(5,7)
                self.x= randint(500,730)
                self.y = -10
                self.vx = randint(-10, -5)
                self.vy = 0
                self.angle = np.arctan(self.vy/self.vx)
                self.image = Image.open('meteor.png')
                self.image_resized = self.image.resize((self.size*20, self.size*20))
                self.pic = ImageTk.PhotoImage(self.image_resized.rotate((90 - self.angle)*180/np.pi))

class Aliens():
    def __init__(self):
        self.type_ = "spaceship"
        self.x = 800
        self.y = 100 #Constant y level    
        self.img1 = tk.PhotoImage(file='spaceship1.png')
        self.img2 = tk.PhotoImage(file='spaceship2.png')
        self.img3 = tk.PhotoImage(file='spaceship3.png')
        self.img4 = tk.PhotoImage(file='spaceship4.png')
        self.img5 = tk.PhotoImage(file='spaceship5.png')
        self.img6 = tk.PhotoImage(file='spaceship6.png')
        self.img7 = tk.PhotoImage(file='spaceship7.png')
        self.img8 = tk.PhotoImage(file='spaceship8.png')
        self.img9 = tk.PhotoImage(file='spaceship9.png')
        self.img10 = tk.PhotoImage(file='spaceship10.png')
        self.img11 = tk.PhotoImage(file='spaceship11.png')
        self.img12 = tk.PhotoImage(file='spaceship12.png')
        self.vx= -10 #Constant speed in x direction
        self.bomb_flag = 0
        self.gap = 500 #Random (will be random in MAIN) x coordinate of the beginning of fire
        
    def move(self,dt):
        """Makes alien to move"""
        self.x+=self.vx*dt
        if self.x < -2500:
            self.x = 2500
            
    def change_bomb_flag(self):
        """Changes flag for the bomb fire"""
        if 0<= self.x <= self.gap:
            self.bomb_flag = 1
        else:
            self.bomb_flag = 0
        
class Bullets(): #Alien's bomb
    def __init__(self):
        self.type_ = "bullet"
        self.x0 = 0
        self.y0 = 0
        self.x = 0
        self.y  = 0
        self.vx = 0
        self.vy = 15
        self.t = 0
        self.deltax = 0
        self.img1 = tk.PhotoImage(file='bomb1.png')
        self.img2 = tk.PhotoImage(file='bomb2.png')
        self.boom1 = tk.PhotoImage(file='boom1.png')
        self.boom2 = tk.PhotoImage(file='boom2.png')
        self.boom3 = tk.PhotoImage(file='boom3.png') 
        self.flag = 0
        
    def fall(self,dt,obj):
        """Makes bomb to fall"""
        if obj.bomb_flag == 1:
            self.x0 = obj.x
            self.y0 = obj.y - 50
            self.vx = obj.vx
            self.vy = 20
            self.deltax += self.vy * dt
            self.x = self.x0 - self.vx * dt
            self.y = self.y0 + self.deltax
        elif obj.bomb_flag == 0:
            self.x = obj.x
            self.y = obj.y - 50
            self.deltax = 0
            
    def change_flag(self, obj):
        """Changes bomb fllag"""
        if obj.bomb_flag == 1:
            self.flag = 1
        elif obj.bomb_flag == 0:
            self.flag = 0

        
    def explode(self,obj1,obj2,y_0):
        """Makes bomb to explode"""
        if obj1.y + 5 >= self.y and obj1.y - 5 <= self.y and obj1.x >= self.x and obj1.x + obj1.length <= self.x or self.y > y_0 - 5:
            self.image = Image.open('bomb_character_o_explode.png')
            self.image_resized = self.image.resize((100,100))
            self.pic = ImageTk.PhotoImage(self.image_resized)
            if obj1.y - 5 >= self.y and obj1.y - 10 <= self.y and obj1.x >= self.x and obj1.x + obj1.length <= self.x or self.y > y_0 - -10:
                self.x = obj2.x
                self.y = obj2.y + 100
                self.vx = obj2.vx
                self.vy = 20
                self.image = Image.open('bomb_character_o_idle.png')
                self.image_resized = self.image.resize((100,100))
                self.pic = ImageTk.PhotoImage(self.image_resized)
                
class Egg():
    def __init__(self):
        self.type_ = "egg"
        self.x = 800
        self.y = randint(100, 300) #Random height of egg's placement
        self.img1 = tk.PhotoImage(file='egg1.png')
        self.img2 = tk.PhotoImage(file='egg2.png')
        self.img3 = tk.PhotoImage(file='egg3.png')
        self.img4 = tk.PhotoImage(file='egg4.png')
        self.img5 = tk.PhotoImage(file='birth1.png')
        
        
    def getting_egg(self, obj):
        """Makes Dino to get Egg"""
        if (self.x - 20) <= obj.x <= (self.x + 20) and (self.y - 20) <= obj.y <= (self.y + 20):
            obj.eggs_number += 1
            self.y = randint(100, 300)
            self.x = 800
            
    def egg_motion(self, dt):
        """Moves Egg with the background and teleports it"""
        self.x -= dt*5
        if self.x < -10:
            self.x = 730

class Heal():
    
    def __init__(self):
        self.type_ = "heal"
        self.x = 1500
        self.y = randint(100, 400) #Random height of meal placement
        self.img1 = tk.PhotoImage(file='fish1.png')
        self.img2 = tk.PhotoImage(file='fish2.png')
        self.img3 = tk.PhotoImage(file='beer.png')
        
        
    def getting_heal(self, obj):
        """Makes Dino get meal"""
        if (self.x - 20) <= obj.x <= (self.x + 20) and (self.y - 20) <= obj.y <= (self.y + 20):
            if obj.lives < 3:
                obj.lives += 1
            self.y = randint(100, 400)
            self.x = 1500
            
    def heal_motion(self, dt):
        """Moves meal with the backgroung"""
        self.x -= dt*5
        if self.x < -1500:
            self.x = 1500