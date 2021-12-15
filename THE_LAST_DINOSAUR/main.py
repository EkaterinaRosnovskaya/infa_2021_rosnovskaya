from tkinter import *
from objects import *
from PIL import ImageTk, Image

from random import *
"""не получилось сделать меню когда оно было в другом модуле поэтому так прости :(((("""
player_name = None
i = 0
length = 0
g = -10
dt = 1
j = 0
o = 0

dead = False
players = []
background = []
spaceships = []
enemies = []
objects = []
floors = []
background_x = 0
under_x = 0
carl_home = []
root, space = None, None

root3, root8 = None,None
remember_name = None


"""menu"""
def start():
    global root

    widget_list = root.winfo_children()

    for item in widget_list:
        if item.winfo_children():
            widget_list.extend(item.winfo_children())

    for item in widget_list:
        item.pack_forget()

    main(root,player_name)

def take_name():
    global name, player_name
    player_name = name.get()


def reopen_menu2():
    global root, space
    widget_list = root.winfo_children()

    for item in widget_list:
        if item.winfo_children():
            widget_list.extend(item.winfo_children())

    for item in widget_list:
        item.pack_forget()
    part_menu()
    



  
def open_menu2():
    global name, root,root3

    root3 = Tk()
    root3.withdraw()
    root = Toplevel()
    root.geometry("720x480+100+10")
    part_menu()
    


def part_menu():
    global name, root
    path = 'dinosaures2.jpg'
    
    image = Image.open(path)

    image = ImageTk.PhotoImage(image)

    pic = Canvas(root, width=720, height=480)
    pic.pack(side="top", fill="both", expand="no")

    pic.create_image(0, 0, anchor="nw", image=image)

    pic.create_text(360, 100, text="The last dinosaur", fill="Yellow", font="Verdana 30")
    pic.create_text(360, 140, text="Enter you name", fill="Yellow", font="Verdana 15")
    pic.create_text(150, 20, text=" ^--| Click here to read the instructions or quit", fill="Yellow", font="Verdana 10")
    mainmenu = Menu(root) 
    root.config(menu=mainmenu)

    new_button = Button(root, text = "New game", background="#555",
                        foreground="#ccc", padx="2",pady="2",font="8",command = start)

    pic.create_window((120, 400), anchor="nw", window=new_button)


    continue_button = Button(root, text = "Continue ", background="#555",
                        foreground="#ccc", padx="2",pady="2",font="8")
    pic.create_window((480, 400), anchor="nw", window=continue_button)

    enter_button = Button(root, text = " <= ", background="#555",
                        foreground="#ccc", padx="2",pady="2",font="1", command = take_name)
    pic.create_window((420, 185), anchor="nw",width=25,height = 17, window = enter_button)


    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="HELP", command = send_help)
    helpmenu.add_command(label="Quit", command = kill_game)

    mainmenu.add_cascade(label="Addition",
                         menu=helpmenu)

    name = StringVar()
     
    name_entry = Entry(root, textvariable=name)
    name_entry.place(relx=.5, rely=.4, anchor="c")
    root.mainloop()

def send_help():
    root8 = Toplevel()
    root8.geometry("720x240+100+10")
    path = 'tutorial.png'
    
    image = Image.open(path)

    image = ImageTk.PhotoImage(image)

    pic = Canvas(root8, width=360, height=240)
    pic.pack(side="top", fill="both", expand="no")

    pic.create_image(0, 0, anchor="nw", image=image)
    root8.mainloop()


def kill_game():
    root3.destroy()

"""main"""


def animation():
  global root, space, objects, background, g, dt, i, j, floors, carl_home, dead
  global enemies, spaceships, background_x, under_x, o


  i+=1
  
  space.delete("all")
  
  
  if i>30 and j==0:
    space.create_image(600 - 2.5*i %855, 240, image=background[0])
    space.create_image(600 - 5*i %855, 240, image=background[1])
    background_x = 600 - 2.5*i %855
    under_x = 600 - 5*i %855    
  elif i<=30 and (j==0):
    space.create_image(600 - 2.5 * 30 %855, 240, image=background[0])
    space.create_image(600 - 5 * 30 %855, 240, image=background[1])
  elif not(j==0):
    space.create_image(background_x, 240, image=background[0])
    space.create_image(under_x, 240, image=background[1])   
  
  for obj in objects:

    if (obj.type_ == "floor"):
      
      if i>30 and j==0:
        obj.x -= 5
      if j<=21:
        space.create_image(obj.x + obj.length/2, obj.y+10, image = obj.pic)
      if obj.x + obj.length < 0:
        obj.x = 720
      if obj.number == 1:
        obj.free_mind(floors[1], floors[2], carl_home[0])
      
      
    elif (obj.type_ == "egg"):
      if i>30 and j==0:
        obj.egg_motion(dt)
        if 1 <= i% 10 <= 2:
          space.create_image(obj.x, obj.y, image=obj.img1)
        elif 3 <= i% 10 <= 4:
          space.create_image(obj.x, obj.y, image=obj.img2)
        elif 5 <= i% 10 <= 6:
          space.create_image(obj.x, obj.y, image=obj.img3)
        elif 7 <= i% 10 <= 8:
          space.create_image(obj.x, obj.y, image=obj.img4)
        elif 9 == i% 10 or 0 == i% 10 :
          space.create_image(obj.x, obj.y, image=obj.img5)
        obj.getting_egg(carl_home[0])
        
    elif (obj.type_ == "heal"):
        if i>30 and j==0:
          obj.heal_motion(dt)
          if 1 <= i% 15 <= 5:
            space.create_image(obj.x, obj.y, image=obj.img1)
          elif 6 <= i% 15 <= 10:
            space.create_image(obj.x, obj.y, image=obj.img2)
          elif 11 <= i% 15 or 0 == i%15:
            space.create_image(obj.x, obj.y, image=obj.img3)
          obj.getting_heal(carl_home[0])    
        
    elif obj.type_ == "meteor":
      if i>100:
        if j==0:
          obj.move(dt,-0.2)
        for floor in floors:
          obj.explosion(floor, 385)
          if j==0:
            space.create_image(obj.x, obj.y, image=obj.pic)
          
    elif obj.type_ == "spaceship":
      if i%300 == 6:
        obj.gap = randint(300, 600)      
      if i > 20 and j==0:
        obj.move(dt)
        obj.change_bomb_flag()
        if 1 <= i% 36 <= 3:
          space.create_image(obj.x, obj.y, image=obj.img1)
        elif 4 <= i% 36 <= 6:
          space.create_image(obj.x, obj.y, image=obj.img2)
        elif 7 <= i% 36 <= 9:
          space.create_image(obj.x, obj.y, image=obj.img3)
        elif 10 <= i% 36 <= 12:
          space.create_image(obj.x, obj.y, image=obj.img4)
        elif 13 <= i% 36 <= 15:
          space.create_image(obj.x, obj.y, image=obj.img5)
        elif 16 <= i% 36 <= 18:
          space.create_image(obj.x, obj.y, image=obj.img6)
        elif 19 <= i% 36 <= 21:
          space.create_image(obj.x, obj.y, image=obj.img7)
        elif 22 <= i% 36 <= 24:
          space.create_image(obj.x, obj.y, image=obj.img8)
        elif 25 <= i% 36 <= 27:
          space.create_image(obj.x, obj.y, image=obj.img9)
        elif 28 <= i% 36 <= 30:
          space.create_image(obj.x, obj.y, image=obj.img10)
        elif 31 <= i% 36 <= 33:
          space.create_image(obj.x, obj.y, image=obj.img11)
        elif 34 <= i% 36 or i%36 == 0:
          space.create_image(obj.x, obj.y, image=obj.img12)        
        
    elif obj.type_ == "bullet":
      obj.change_flag(spaceships[0])
      
      if obj.flag == 1:
        obj.fall(dt, spaceships[0])
        
        if obj.y <= 300:
          if 0<= i%6 <=2:
            space.create_image(obj.x, obj.y, image=obj.img1)
          elif 3<= i%6 <=5:
            space.create_image(obj.x, obj.y, image=obj.img2)
            
        elif 300 < obj.y <= 370:
          space.create_image(obj.x, obj.y, image=obj.boom1)
          
        elif 370 < obj.y <= 400:
          if 0<= i%6 <=2:
            space.create_image(obj.x, obj.y, image=obj.boom2)
          elif 3<= i%6 <=5:
            space.create_image(obj.x, obj.y, image=obj.boom3)        
          
      
      elif obj.flag == 0:
        obj.x = -100
        obj.y = 50
        obj.deltax = 0
        obj.vy = randint(10, 20)
      
    elif (obj.type_ == "dino"):
      o = obj.eggs_number
      space.create_text(580, 75, text=str(o), fill="White", font="Verdana 12")
      if obj.lives <= 0:
        j+=1
        if j<=21:
          if 1 <= j% 28 <=4:
            space.create_image(obj.x, obj.y, image=obj.death1)
          elif 5 <= j% 28 <=8:
            space.create_image(obj.x, obj.y, image=obj.death2)
          elif 9 <= j% 28 <= 12:
            space.create_image(obj.x, obj.y, image=obj.death3)
          elif 13 <= j% 28 <= 16:
            space.create_image(obj.x, obj.y, image=obj.death4)
          elif 17 <= j% 28 <= 20:
            space.create_image(obj.x, obj.y, image=obj.death5)
          elif 21 <= j% 28 <= 24:
            space.create_image(obj.x, obj.y, image=obj.death6) 
          elif 25 <= j% 28 or j% 28 == 0:
            space.create_image(obj.x, obj.y, image=obj.death7)
            
        elif j>21:
          dead = True
          write_to_file(remember_name)
          space.delete("all")
          space.create_image(360, 240, image=obj.after_death)
          return_button = Button(root, text = "Back to menu ", background="#555",
                                    foreground="#ccc", padx="2",pady="2",font="8",command = reopen_menu)
          space.create_window((280, 400), anchor="nw", window=return_button)

      
      elif obj.lives > 0:
        if i % 5 == 0:
          for enemy in enemies:
            obj.death(enemy)
        for t in range(obj.lives):
          if i % 16 == 1 or i % 16 == 2:
            space.create_image(80+20*t, 50, image=obj.heart_img1)
          elif i% 16 == 3 or i % 16 == 4:
            space.create_image(80+20*t, 50, image=obj.heart_img2)
          elif i% 16 == 5 or i % 16 == 6:
            space.create_image(80+20*t, 50, image=obj.heart_img3)
          elif i% 16 == 7 or i % 16 == 8:
            space.create_image(80+20*t, 50, image=obj.heart_img4)
          elif i% 16 == 9 or i % 16 == 10:
            space.create_image(80+20*t, 50, image=obj.heart_img5)
          elif i% 16 == 11 or i % 16 == 12:
            space.create_image(80+20*t, 50, image=obj.heart_img6) 
          elif i% 16 == 13 or i % 16 == 14:
            space.create_image(80+20*t, 50, image=obj.heart_img7)
          elif i% 16 == 15 or i % 16 == 0:
            space.create_image(80+20*t, 50, image=obj.heart_img8)
            
            
        if i>30:
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
        elif i<=30:
          if 1<= i <= 3:
            space.create_image(obj.x, obj.y, image=obj.birth1)
          elif 4<= i <= 6:
            space.create_image(obj.x, obj.y, image=obj.birth2)
          elif 7<= i <= 9:
            space.create_image(obj.x, obj.y, image=obj.birth3)
          elif 10<= i <= 12:
            space.create_image(obj.x, obj.y, image=obj.birth4)
          elif 13<= i <= 15:
            space.create_image(obj.x, obj.y, image=obj.birth5)
          elif 16<= i <= 18:
            space.create_image(obj.x, obj.y, image=obj.birth6) 
          elif 19<= i <= 21:
            space.create_image(obj.x, obj.y, image=obj.birth7)
          elif 22<= i <= 24:
            space.create_image(obj.x, obj.y, image=obj.birth8)
          elif 25<= i <= 27:
            space.create_image(obj.x, obj.y, image=obj.birth9)
          elif 28<= i <= 30:
            space.create_image(obj.x, obj.y, image=obj.birth10)        
         
          
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
      
        
        if obj.jump_flag == 0 and obj.start_y == 275:
          obj.y == 275      
        
        if obj.fall_flag == 1 and obj.y < obj.start_y:
          obj.fall(dt,g)
          if obj.y >= obj.start_y:
            obj.fall_flag = 0
            obj.fall_vy = 0
          
        
        if obj.start_y == 385 and obj.y > 385:
          obj.y = 385
        elif obj.start_y == 275 and obj.y > 275:
          obj.y = 275
          
          if obj.start_y == 300 and obj.y > 300:
            obj.y = 300
            
    
      
    
       
  if j<=21:   
    space.create_text(40, 50, text="Lives:", fill="White", font="Verdana 12")
    space.create_text(500, 50, text="Eggs:", fill="White", font="Verdana 12")
    space.create_image(550, 50, image=background[2])



  if dead == False:  
    space.after(40, animation)


def reopen_menu():
    global player_name, i, length, j, o, dead,under_x
    global background_x, root, space,remember_name,root4
    player_name = None
    space,root4,remember_name, root8= None,None,None, None
    dead = False
    i = 0
    length = 0
    j = 0
    o = 0
    background_x = 0
    under_x = 0

    players.clear()
    background.clear()
    spaceships.clear()
    enemies.clear()
    objects.clear()
    floors.clear()
    carl_home.clear()
    
    reopen_menu2()


  
def write_to_file(remember_name):
  global o

  f1 = open("leader_board.txt", "r")
  lines = f1.readlines()
  played_before = False 
  better_than_somebody = False 

  for line in lines:
      if len(line) < 2:
          break
      line = line.split()
      name_local = line[0]
      if (name_local == remember_name):
          played_before = True
      score_local = int(line[2])
      if (o > score_local):
          better_than_somebody = True
      players.append((name_local, score_local))
      

  if better_than_somebody:
      if played_before:
          index = -1
          for k in range(len(players)):
              if (remember_name == players[k][0]):
                  index = k       
          if (players[index][1] < o):
              players[index] = (remember_name , o)
              
 
      else:
          min_ = min([x[1] for x in players])
          index = -1
          for k in range(len(players)):
              if players[k][1] == min_:
                  index = k
          players[index] = (remember_name, o)
          
  f1.close()    

  f = open('leader_board.txt','w')
  for n in range(5):
      f.write(str(players[n][0]))
      f.write(' : ')
      f.write(str(players[n][1]))
      f.write('\n')
  f.close()


  f = open('leader_board.txt','r')
  print(*f)
  f.close()





def main(rt, player_name):
  global root, space, objects, background,remember_name

  remember_name = player_name

  root = rt

  space = tk.Canvas(root, width=720, height=480, bg='black')
  space.focus_set()
  space.pack()

  background.append(tk.PhotoImage(file='Background_up.png'))
  background.append(tk.PhotoImage(file='Background_down.png'))
  background.append(tk.PhotoImage(file='egg_icon.png'))


  
  
  
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

  meteor = Meteors()
  objects.append(meteor)
  enemies.append(meteor)

  spaceship = Aliens()
  objects.append(spaceship)
  enemies.append(spaceship)
  spaceships.append(spaceship)

  space_bullet = Bullets()
  objects.append(space_bullet)
  enemies.append(space_bullet)
  
  egg = Egg()
  objects.append(egg)
  
  heal = Heal()
  objects.append(heal)
  

  

  
  space.bind('<Up>', 
         lambda event: carl.change_jump_flag(1))
  space.bind('<Left>', 
         lambda event: carl.change_left_flag(1))
  space.bind('<Right>', 
         lambda event: carl.change_right_flag(1))
  space.bind('<KeyRelease-Left>', 
         lambda event: carl.change_left_flag(0))
  space.bind('<KeyRelease-Right>', 
         lambda event: carl.change_right_flag(0))    
  
  
  animation()




if __name__== "__main__":
  open_menu2()
  



