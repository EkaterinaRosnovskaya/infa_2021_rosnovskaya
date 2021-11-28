import tkinter as tk
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