import tkinter as tk
from objects import *
from menu import *

i = 0
g = -1.3
dt = 1
background = []
objects = []
root, space = None, None
player_name = None
#game_started = False

def animation():
  global root, space, objects, background, g, dt, i

  i+=1
  
  space.delete("all")
  
  space.create_image(600 - 2.5*i %855, 240, image=background[0])
  space.create_image(600 - 5*i %855, 240, image=background[1])
  
  """if 1 <= i <= 50:
    space.create_image(360, 240, image=beg1)
  elif 51 <= i <= 58:
    space.create_image(360, 240, image=beg2)
  elif 59 <= i <= 65:
    space.create_image(360, 240, image=beg2)"""    
  
  for obj in objects:
    if (obj.type_ == "dino"):
      if i % 14 == 1 or i % 14 == 2:
        space.create_image(obj.x, obj.y, image=obj.img1)
      elif i% 14 == 3 or i % 14 == 4:
        space.create_image(obj.x, obj.y, image=obj.img2)
      elif i% 14 == 5 or i % 14 == 6:
        space.create_image(obj.x, obj.y, image=obj.img3)
      elif i% 14 == 7 or i % 14 == 8:
        space.create_image(obj.x, obj.y, image=obj.img4)
      elif i% 14 == 9 or i % 14 == 10:
        space.create_image(obj.x, obj.y, image=obj.img5)
      elif i% 14 == 11 or i % 14 == 12:
        space.create_image(obj.x, obj.y, image=obj.img6) 
      elif i% 14 == 13 or i % 14 == 0:
        space.create_image(obj.x, obj.y, image=obj.img7)
        
      if obj.right_flag == 1:

        obj.move_right(dt)
        
      if obj.left_flag == 1:
        obj.move_left(dt)
        
      if obj.y < 385:
       obj.jump(dt, g)
       obj.vy = obj.vy + g * dt
      elif obj.y >= 380: 
        obj.vy = 10
        obj.y = 385
        
      
  
  space.after(40, animation)



def main():
  global root, space, objects, background, player_name
  #game_started = True
  #теперь оба окна не главные и чтобы игра кончилась надо чето сделать но я устал поэтому потом 
  root = tk.Toplevel()
  root.geometry("720x480+600+100")
  root.title("The Last Dinosaur")
  
  space = tk.Canvas(root, width=720, height=480, bg='black')
  space.focus_set()
  space.pack()

  background.append(tk.PhotoImage(file='Background_up.png'))
  background.append(tk.PhotoImage(file='Background_down.png'))
  """beg1 = tk.PhotoImage(file='beg1.png')
  beg2 = tk.PhotoImage(file='beg2.png')
  beg3 = tk.PhotoImage(file='beg3.png')
  beg4 = tk.PhotoImage(file='beg4.png')
  beg5 = tk.PhotoImage(file='beg5.png')
  beg6 = tk.PhotoImage(file='beg6.png')
  beg7 = tk.PhotoImage(file='beg7.png')
  beg8 = tk.PhotoImage(file='beg8.png')"""
  
  
  
  #Create Carl
  
  carl = Dino(x_0 = 20, y_0 = 385)
  objects.append(carl)
  
  space.bind('<Up>', 
          lambda event: carl.jump(dt, g))
  """space.bind('<Down>', 
         lambda event: carl.move(0, 20))"""
  space.bind('<Left>', 
         lambda event: carl.change_left_flag(1))
  space.bind('<Right>', 
         lambda event: carl.change_right_flag(1))
  space.bind('<KeyRelease-Left>', 
         lambda event: carl.change_left_flag(0))
  space.bind('<KeyRelease-Right>', 
         lambda event: carl.change_right_flag(0))    
  
  
  animation()
  root.mainloop()
  

if __name__== "__main__":
  open_menu()
