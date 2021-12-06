import tkinter as tk
from objects import *
from menu import *
from random import *

i = 0
length = 0
g = -10
dt = 1
background = []
objects = []
floors = []
carl_home = []
root, space = None, None
player_name = None
#game_started = False

def animation():
  global root, space, objects, background, g, dt, i, floors, carl_home

  i+=1
  
  space.delete("all")
  
  space.create_image(600 - 2.5*i %855, 240, image=background[0])
  space.create_image(600 - 5*i %855, 240, image=background[1])
     
  
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

      for floor in floors:
        
      
       obj.change_of_level_test(floor)
       if obj.start_y <= floor.y and obj.y <= floor.y:
         obj.return_of_level_test(floor)
         obj.return_of_level_test_1(floor)
         
       else:
         floor.fall_flag = 0
        
       

      if obj.jump_flag == 1:
        obj.jump(dt, g)
        if obj.y >= obj.start_y:
          obj.jump_flag = 0
          obj.vy = 50
      elif obj.jump_flag == 0:
        pass
      
      if obj.fall_flag == 1 and obj.y < obj.start_y:
        obj.fall(dt,g)
        if obj.y >= obj.start_y:
          obj.fall_flag = 0
          obj.fall_vy = 0
        
      
      if obj.start_y == 385 and obj.y > 385:
        obj.y = 385
        
        if obj.start_y == 300 and obj.y > 300:
          obj.y = 300      
      
      
    
    elif (obj.type_ == "floor"):
      
      obj.x -= 5
      space.create_image(obj.x + obj.length/2, obj.y+15, image = obj.pic)
      if obj.x + obj.length < 0:
        obj.x = 720
      if obj.number == 1:
        obj.free_mind(floors[1], floors[2], carl_home[0])
      
      

    
  space.after(40, animation)



def main(rt):
  global root, space, objects, background, player_name
  #game_started = True
  #теперь оба окна не главные и чтобы игра кончилась надо чето сделать но я устал поэтому потом 
  #root = tk.Toplevel()
  #root.geometry("720x480+100+100")
  #root.title("The Last Dinosaur")

  root = rt
  
  space = tk.Canvas(root, width=720, height=480, bg='black')
  space.focus_set()
  space.pack()

  background.append(tk.PhotoImage(file='Background_up.png'))
  background.append(tk.PhotoImage(file='Background_down.png'))
  
  
  
  
  #Create Carl
  
  carl = Dino(x_0 = 20, y_0 = 385)
  objects.append(carl)
  carl_home.append(carl)

  floor1 = Floor(1)
  objects.append(floor1)
  floors.append(floor1)

  floor2 = Floor(2)
  objects.append(floor2)
  floors.append(floor2)

  floor3 = Floor(3)
  objects.append(floor3)
  floors.append(floor3)



  
  space.bind('<Up>', 
          lambda event: carl.change_jump_flag(1))
  #space.bind('<Up>', 
          #lambda event: carl.change_of_level_and_jump(dt, g,))
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
  #root.mainloop()
  

if __name__== "__main__":
  open_menu()
