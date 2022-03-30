from tkinter import *  
import os,sys
import tkinter 
from PIL import Image, ImageTk
import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

GPIO.setup (22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup (23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup (24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup (25, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def my_callback(channel):
  print ( "falling edge detected on 22" )
  sys.exit()

GPIO.add_event_detect(22,GPIO.FALLING,callback=my_callback, bouncetime=300)


class TailRecurseException:
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(g):

  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException:
            args = e.args
            kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func


def increment_value_of_x_by_1():
    global x
    global manual_button
    if manual_button == 1:
        x=x+1
        print("Next button is pressed")

    if x>=no_of_files-1:
        x=0


def decrement_value_of_x_by_1():
    global x
    global manual_button
    if manual_button == 1:
        x=x-1
        print("previous button is pressed")

    if x<0:
        x=no_of_files-2


@tail_call_optimized
def Manual_Mode():
  global tkimg1
  global x
  global manual_button
  global dummy
  dummy=0
  manual_button = GPIO.input(25)
  if GPIO.input(23) == 1:
    increment_value_of_x_by_1()
    dummy=1
  if GPIO.input(24) == 1:
    decrement_value_of_x_by_1()
    dummy=1
  if GPIO.input(25) == 1:
    if x<0:
      x=no_of_files-2
    if x>=no_of_files-1:
      x=0
  if x<0:
    x=no_of_files-2
  if x>=no_of_files-1:
    x=0
  if GPIO.input(25) == 0:
    im=Image.open(dirlist[x])
    im=im.resize((w,h))

    tkimg1 = ImageTk.PhotoImage(im)
    label.config( image = tkimg1)
    root.title(dirlist[x])
    label.after(8000, Manual_Mode)
    print("Auto Mode")
    x=x+1
  else:
    if dummy==1:
      im=Image.open(dirlist[x])
      t=im.size
      im=im.resize((w,h))
      tkimg1 = ImageTk.PhotoImage(im)
      label.config( image = tkimg1)
      root.title(dirlist[x])
      label.after(50, Manual_Mode)
      
    else:
      Manual_Mode()
############################################################
x=0
path='/home/pi/imageshare/Slide_Show/'
image_files_dummy =os.listdir(path)
no_of_images=len(image_files_dummy)
no_of_files=no_of_images
for m in range(0,no_of_files-1):
  image_files_dummy[m]=str(m+1)+'.jpg'
  print(m)
print(image_files_dummy)


foo='01234 '
twod_list = []
for i in range (0,no_of_images-1):
    image_files=[]
    for j in range(0,no_of_images-1):
        image_files.append(foo)
    twod_list.append(image_files)
for m in range(0,no_of_images-1):
    image_files[m]=path+image_files_dummy[m]
dirlist=image_files


root = Tk()         
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

im = Image.open(dirlist[x])
im=im.resize((w,h))
x=x+1
tkimg1 = ImageTk.PhotoImage(im)
label =  tkinter.Label(root, image=tkimg1)
label.pack()
label.after(7000, Manual_Mode)   
root.mainloop()

                                                               