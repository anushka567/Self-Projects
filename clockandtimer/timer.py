from tkinter import *
import time
import sys
import random

t=0

root=Tk()
root.title('My Time')
root.iconbitmap('./OIP.ico')
root.geometry("600x400")

def clock():
  hour=time.strftime("%I")  #current hour
  minute=time.strftime("%M")
  second=time.strftime("%S")
  am_or_pm=time.strftime("%p")
  day=time.strftime("%A")
  timezone=time.strftime("%Z")
  my_label.config(text=hour+":"+minute+":"+second+" "+am_or_pm)
  my_label.after(1000,clock)

  my_label2.config(text=day+" ,"+timezone)
def update():
  my_label.config(text="New Text")


my_label=Label(root,text="",font=("Helvetica",48),fg="green",bg="black")
my_label.pack(pady=20)
#my_label.after(5000,update)
my_label2 = Label(root, text="", font=("Helvetica", 16))
my_label2.pack(pady=10)
clock()



def set_timer():
  global t
  t=t+int(e1.get())
  return t

def countdown():
  global t
  if t>0:
    l1.config(text=str(t)+" sec remaining")
    t=t-1
    l1.after(1000,countdown)
  elif t==0:
    l1.config(text="TIME UP!")


l1 = Label(root, text="CountDown Timer", font=("Helevetica", 24))
l1.pack(pady=10)
times=StringVar()
e1=Entry(root,textvariable=times)
e1.pack(pady=10)

b1=Button(root,text="SET",width=20,command=set_timer)
b1.pack(pady=10)

b2=Button(root,text="START",width=20,command=countdown)
b2.pack(pady=10)
root.mainloop()
