from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import winsound
from PIL import *
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser
import threading
import time
import os

#start of GUI
root=tk.Tk()
root.title("TOOLKIT GUI program")
root.attributes("-fullscreen",True)

#notebook deployed
notebook = ttk.Notebook(root)
notebook.place(x=0,y=0)

#frames
frame1 = ttk.Frame(notebook,width=10000,height=900)

frame2 = ttk.Frame(notebook,width=10000,height=900)

frame3 = ttk.Frame(notebook,width=10000,height=900)

frame4 =  ttk.Frame(notebook,width=10000,height=900)

frame5 =  ttk.Frame(notebook,width=10000,height=900)

frame6 =  ttk.Frame(notebook,width=10000,height=900)

frame7 =  ttk.Frame(notebook,width=10000,height=900)

frame8 =  ttk.Frame(notebook,width=10000,height=900)

frame9 =  ttk.Frame(notebook,width=10000,height=900)

frame10 =  ttk.Frame(notebook,width=10000,height=900)

frame11 =  ttk.Frame(notebook,width=10000,height=900)

frame12 = ttk.Frame(notebook,width=10000,height=900)

frame13 = ttk.Frame(notebook,width=10000,height=900)

frame14 = ttk.Frame(notebook,width=10000,height=900)

#frames placed
frame1.place(x=0,y=0)

frame2.place(x=0,y=0)

frame3.place(x=0,y=0)

frame4.place(x=0,y=0)

frame5.place(x=0,y=0)

frame6.place(x=0,y=0)

frame7.place(x=0,y=0)

frame8.place(x=0,y=0)

frame9.place(x=0,y=0)

frame10.place(x=0,y=0)

frame11.place(x=0,y=0)

frame12.place(x=0,y=0)

frame13.place(x=0,y=0)

frame14.place(x=0,y=0)

#frames deployed
notebook.add(frame1, text='0')

notebook.add(frame2, text='1')

notebook.add(frame3, text='2')

notebook.add(frame4, text='3')

notebook.add(frame5, text='4')

notebook.add(frame6, text='5')

notebook.add(frame7, text='6')

notebook.add(frame8, text='7')

notebook.add(frame9, text='8')

notebook.add(frame10, text='9')

notebook.add(frame11, text='10')

notebook.add(frame12, text='11')

notebook.add(frame13, text='12')

notebook.add(frame14, text='13')



#hiding the tab tiles



#functions
def video():
    import pygame
    import moviepy.editor

    pygame.init()
    video = moviepy.editor.VideoFileClip("video11.mp4")
    video.preview()
    pygame.quit()
    notebook.select(1)

def video2():
    import pygame
    import moviepy.editor

    pygame.init()
    video = moviepy.editor.VideoFileClip("video11.mp4")
    video.preview()
    pygame.quit()
    notebook.select(1)

def tools():
    notebook.select(2)

def med():
    notebook.select(10)

def mainmenu():
    notebook.select(1)

def tool1():
    notebook.select(3)

def tool2():
    notebook.select(4)

def tool3():
    notebook.select(5)

def tool4():
    notebook.select(6)

def tool5():
    notebook.select(7)

def tool6():
    notebook.select(8)

from threading import Thread

def game():
    os.system('game1.py')


def game3():
    os.system('game3.py')

def game2():
    notebook.select(11)
    local_time=0
    root.after(20000, run_timer)
def dele():
    labele.place_forget()
def dele2():
    labele2.place_forget()

def run_timer():
    global count
    if count<60:
        global labele
        labele = tk.Label(frame12, text="YOU LOST!!!!")

        labele.place(x='650',y='200')
        time.sleep(1)
        notebook.select(4)
        import pygame
        import moviepy.editor

        pygame.init()
        video = moviepy.editor.VideoFileClip("video21.mp4")
        video.preview()
        pygame.quit()
        root.after(800,dele)
    elif count>=60:
        global labele2
        labele2 = tk.Label(frame12, text="YOU WON!!!!")

        labele2.place(x='650',y='200')
        time.sleep(1)
        notebook.select(4)
        root.after(800,dele2)
    root.after(800,rate)
    count=0
            


#background #read for frame reference
img1=Image.open("button.png")
resize_img=img1.resize((1270,710))
img_1=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame1,image=img_1)
ImgLabel.img1=img_1
ImgLabel.place(x=0, y=0)

imgB=Image.open("mainmenu.jpeg")
resize_img=imgB.resize((1270,710))
img_B=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame2,image=img_B)
ImgLabel.imgB=img_B
ImgLabel.place(x=0, y=0)

#tools
imgB2=Image.open("tnm.jpeg")
resize_img=imgB2.resize((1270,710))
img_B2=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame3,image=img_B2)
ImgLabel.imgB2=img_B2
ImgLabel.place(x=0, y=0)

#medkit
imgB2=Image.open("tnm.jpeg")
resize_img=imgB2.resize((1270,710))
img_B2=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame11,image=img_B2)
ImgLabel.imgB2=img_B2
ImgLabel.place(x=0, y=0)


#tool1
imgB3=Image.open("tool1.jpeg")
resize_img=imgB3.resize((1270,710))
img_B3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame4,image=img_B3)
ImgLabel.img3=img_B3
ImgLabel.place(x=0, y=0)

#tool2
imgB3=Image.open("tool2.jpeg")
resize_img=imgB3.resize((1270,710))
img_B3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame5,image=img_B3)
ImgLabel.img3=img_B3
ImgLabel.place(x=0, y=0)

#tool3
imgB3=Image.open("tool3.jpeg")#here
resize_img=imgB3.resize((1270,710))
img_B3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame6,image=img_B3)
ImgLabel.img3=img_B3
ImgLabel.place(x=0, y=0)

#tool4
imgB3=Image.open("tool4.jpeg")
resize_img=imgB3.resize((1270,710))
img_B3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame7,image=img_B3)
ImgLabel.img3=img_B3
ImgLabel.place(x=0, y=0)

#tool5
imgB3=Image.open("tool5.jpeg")
resize_img=imgB3.resize((1270,710))
img_B3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame8,image=img_B3)
ImgLabel.img3=img_B3
ImgLabel.place(x=0, y=0)

#tool6
imgB3=Image.open("tool6.jpeg")
resize_img=imgB3.resize((1270,710))
img_B3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame9,image=img_B3)
ImgLabel.img3=img_B3
ImgLabel.place(x=0, y=0)


# Create the transparent button using the Label widget



#images
'''
img2=Image.open("gun.jpeg")
resize_img=img2.resize((300,400))
img_2=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame2,image=img_2)
ImgLabel.img2=img_2
ImgLabel.place(x=100, y=100)


img3=Image.open("gun.jpeg")
resize_img=img3.resize((300,400))
img_3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame2,image=img_3)
ImgLabel.img3=img_3
ImgLabel.place(x=500, y=100)

img4=Image.open("gun.jpeg")
resize_img=img4.resize((300,400))
img_4=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame2,image=img_4)
ImgLabel.img4=img_4
ImgLabel.place(x=900, y=100)

'''

#buttons
####main menu(frame 2)
button=Button(frame1,text="",width=8,height=3,bg="#ff0000",font= ('Helvetica 10 bold'),command=video)
button.place(x=590,y=460)

button=Button(frame2,text="<===tools",width=18,height=7,bg="blue",font= ('Helvetica 10 bold'),command=tools)
button.place(x=100,y=200)

button=Button(frame2,text="medkit===>",width=18,height=7,bg="blue",font= ('Helvetica 10 bold'),command=med)
button.place(x=1100,y=200)

###############tools(frame 3)(same for medkit(frame11))

img2=Image.open("gun.jpeg")
resize_img=img2.resize((275,400))
img_2=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame3,image=img_2)
ImgLabel.img2=img_2
ImgLabel.place(x=100, y=150)


img3=Image.open("arm.jpeg")
resize_img=img3.resize((250,350))
img_3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame3,image=img_3)
ImgLabel.img3=img_3
ImgLabel.place(x=515, y=175)

img4=Image.open("torch.jpeg")
resize_img=img4.resize((275,400))
img_4=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame3,image=img_4)
ImgLabel.img4=img_4
ImgLabel.place(x=900, y=150)

button=Button(frame3,text="tool1",width=34,height=3,bg="blue",font= ('Helvetica 10 bold'),command=tool1)
button.place(x=100,y=550)

button=Button(frame3,text="tool2",width=31,height=3,bg="blue",font= ('Helvetica 10 bold'),command=tool2)
button.place(x=515,y=525)

button=Button(frame3,text="tool3",width=34,height=3,bg="blue",font= ('Helvetica 10 bold'),command=tool3)
button.place(x=900,y=550)


button=Button(frame3,text="<===",width=6,height=3,bg="blue",font= ('Helvetica 10 bold'),command=mainmenu)
button.place(x=0,y=330)


#######medkit(frame11)


img2=Image.open("pill.jpeg")
resize_img=img2.resize((275,400))
img_2=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame11,image=img_2)
ImgLabel.img2=img_2
ImgLabel.place(x=100, y=150)


img3=Image.open("inj.jpeg")
resize_img=img3.resize((250,350))
img_3=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame11,image=img_3)
ImgLabel.img3=img_3
ImgLabel.place(x=515, y=175)

img4=Image.open("bandaid.jpeg")
resize_img=img4.resize((275,400))
img_4=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame11,image=img_4)
ImgLabel.img4=img_4
ImgLabel.place(x=900, y=150)

button=Button(frame11,text="tool4",width=34,height=3,bg="blue",font= ('Helvetica 10 bold'),command=tool4)
button.place(x=100,y=550)

button=Button(frame11,text="tool5",width=31,height=3,bg="blue",font= ('Helvetica 10 bold'),command=tool5)
button.place(x=515,y=525)

button=Button(frame11,text="tool6",width=34,height=3,bg="blue",font= ('Helvetica 10 bold'),command=tool6)
button.place(x=900,y=550)

button=Button(frame11,text="<===",width=6,height=3,bg="blue",font= ('Helvetica 10 bold'),command=mainmenu)
button.place(x=0,y=330)


#####tool1
button=Button(frame4,text="===>",width=6,height=3,bg="blue",font= ('Helvetica 10 bold'),command=mainmenu)
button.place(x=1150,y=320)

button=Button(frame4,text="game",width=12,height=6,bg="blue",font= ('Helvetica 10 bold'),command=game)
button.place(x=1080,y=450)

####tool2

button=Button(frame5,text="===>",width=6,height=3,bg="blue",font= ('Helvetica 10 bold'),command=mainmenu)
button.place(x=1150,y=320)

button=Button(frame5,text="game",width=12,height=6,bg="blue",font= ('Helvetica 10 bold'),command=game2)
button.place(x=1080,y=450)


####tool3
button=Button(frame6,text="===>",width=6,height=3,bg="blue",font= ('Helvetica 10 bold'),command=mainmenu)
button.place(x=1150,y=320)

button=Button(frame6,text="game",width=12,height=6,bg="blue",font= ('Helvetica 10 bold'),command=game3)
button.place(x=1080,y=450)

###tool4
button=Button(frame7,text="===>",width=6,height=3,bg="blue",font= ('Helvetica 10 bold'),command=mainmenu)
button.place(x=1150,y=320)

###tool5
button=Button(frame8,text="===>",width=6,height=3,bg="blue",font= ('Helvetica 10 bold'),command=mainmenu)
button.place(x=1150,y=320)


###tool6
button=Button(frame9,text="===>",width=6,height=3,bg="blue",font= ('Helvetica 10 bold'),command=mainmenu)
button.place(x=1150,y=320)


####################game###############
def clicked(): # without event because I use `command=` instead of `bind`
    global count

    count = count + 1
    global labelp
    
    labelp = tk.Label(frame12, text="you clicked: {}".format(count),font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')

    labelp.place(x='500',y='450')


label2= tk.Label(frame12, text="you need to click the button 60 times or else you will drifted in space" ,font=('LucidaConsole 22 bold'),borderwidth=2,bd=2,fg='red')
label2.place(x='200',y='150')
button=Button(frame12,text="click",width=32,height=12,bg="blue",font= ('Helvetica 10 bold'),command=clicked)
button.place(x=500,y=200)

count = 0

def rate():
    labelp.place_forget()

