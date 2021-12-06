from tkinter import *
from main import *
from objects import *
from PIL import ImageTk, Image
button_pressed = False

def start():
    global root

    widget_list = root.winfo_children()

    for item in widget_list:
        if item.winfo_children():
            widget_list.extend(item.winfo_children())

    for item in widget_list:
        item.pack_forget()
    
    main(root)

def take_name():
    global name
    player_name = name.get()
    print(player_name)


def open_menu():
    global name, root
    path = 'dinosaures.jpg'
    root3 = Tk()
    root3.withdraw()
    
    root = Toplevel()
    root.geometry("720x480+100+10")
    image = Image.open(path)
    width = 500
    ratio = (width / float(image.size[0]))
    height = int((float(image.size[1]) * float(ratio)))
    image = image.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    pic = Canvas(root, width=width, height=height)
    pic.pack(side="top", fill="both", expand="no")

    pic.create_image(0, 0, anchor="nw", image=image)

    pic.create_text(250, 50, text="The last dinosaur", fill="Yellow", font="Verdana 30")
    pic.create_text(250, 100, text="Enter you name", fill="Yellow", font="Verdana 15")
    mainmenu = Menu(root) 
    root.config(menu=mainmenu)

    new_button = Button(root, text = "New game", background="#555",
                        foreground="#ccc", padx="2",pady="2",font="8",command = start)

    pic.create_window((100, 250), anchor="nw", window=new_button)


    continue_button = Button(root, text = "Continue", background="#555",
                        foreground="#ccc", padx="2",pady="2",font="8")
    pic.create_window((300, 250), anchor="nw", window=continue_button)

    enter_button = Button(root, text = " <= ", background="#555",
                        foreground="#ccc", padx="2",pady="2",font="1", command = take_name)
    pic.create_window((310, 127), anchor="nw",width=25,height = 17, window =enter_button)


    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="HELP")
    helpmenu.add_command(label="About game")

    mainmenu.add_cascade(label="Addition",
                         menu=helpmenu)

    name = StringVar()
     
    name_entry = Entry(root, textvariable=name)
    name_entry.place(relx=.5, rely=.4, anchor="c")
    #print(game_started)
   # if game_started == True:
        #root2.destroy()

    root.mainloop()

