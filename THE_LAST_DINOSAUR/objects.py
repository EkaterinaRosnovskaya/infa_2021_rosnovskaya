import tkinter as tk
from random import *
from PIL import Image, ImageTk
class Dino():
    
    def __init__(self, x_0, y_0):
        
        self.x = x_0
        self.y = y_0
        self.img1 = tk.PhotoImage(file='carl1.png')
        self.img2 = tk.PhotoImage(file='carl2.png')
        self.img3 = tk.PhotoImage(file='carl3.png')
        self.img4 = tk.PhotoImage(file='carl4.png')
        self.img5 = tk.PhotoImage(file='carl5.png')
        self.img6 = tk.PhotoImage(file='carl6.png')
        self.img7 = tk.PhotoImage(file='carl7.png')
        self.type_ = "dino"
        self.vy = 50
        self.vx = 10
        self.right_flag = 0
        self.left_flag = 0
        self.jump_flag = 0
        self.level_flag = 0
        ###
        self.start_y = y_0
        self.fall_vy = 0
        self.fall_flag = 0
    def move_left(self, dt):
        
        if self.x >= 5:
            self.vx = -10
            self.x += self.vx * dt
        else:
            pass
        
    def move_right(self, dt):
        
        if self.x <= 715:
            self.vx = 10
            self.x += self.vx * dt
        else:
            pass

    def jump(self, dt, g):
        
        self.y = self.y - self.vy * dt + g * dt**2 / 2
        self.vy += g * dt
        
    def change_right_flag(self, x):
        if x:
            self.right_flag = 1
        else:
            self.right_flag = 0
            
    def change_left_flag(self, x):
        if x:
            self.left_flag = 1
        else:
            self.left_flag = 0

    def change_jump_flag(self, x):
        if x:
            self.jump_flag = 1
        else:
            self.jump_flag = 0
            
    def change_of_level_test(self, obj):
        if self.y <= obj.y and obj.x <= self.x <= (obj.x + obj.length):
            self.start_y = obj.y - 25  
    def return_of_level_test(self, obj):
        if not(obj.x <= self.x <= (obj.x + obj.length)):
            obj.fall_flag = 1
    def return_of_level_test_1(self, obj):
        if (obj.x <= self.x <= (obj.x + obj.length)):
            obj.fall_flag = 0    
            
    def fall(self, dt, g):
        
        self.y = self.y - self.fall_vy * dt + g * dt**2 / 2
        self.fall_vy += g * dt 
        
            

class Floor():
    
    def __init__(self, number):
        
        self.y = 300
        self.number = number
        self.x = 720 + (self.number - 1)*240
        self.length = randint(100, 200)
        self.type_ = "floor"
        self.width = 10
        self.fall_flag = 0
        self.img = Image.open('grace.png')
        self.img_resized = self.img.resize((self.length, 20))
        self.pic = ImageTk.PhotoImage(self.img_resized)
        
    def free_mind(self, obj1, obj2, obj3):
        if self.fall_flag == 1 and (obj1.fall_flag == 1 and obj2.fall_flag == 1):
            if  obj3.y <= self.y:
                obj3.fall_flag = 1
                obj3.start_y = 385
            