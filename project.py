import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import random
import difflib
from difflib import SequenceMatcher
root=tk.Tk()
root.geometry ("1000x800")
img=PhotoImage(file='typing.png')
Label(root,image=img).pack()
frame1= Frame(root)
frame1.pack()
frame2= Frame(root)
frame2.pack()
root.title("Typing Speed Test")

string = Entry(frame2,bg='grey',bd=5,font='times',fg='black')
def printValue():
    global W,T,A,S
    timeEnd = time.time()
    stg = string.get()
    words= float ((len(stg))/5)
    timeTaken = timeEnd-timeStart
    speed = words/(timeTaken/60)
    try:
        W.destroy()
        T.destroy()
        A.destroy()
        S.destroy()
    except:
        pass
    W = tk.Label(frame2, text=f"Words: {words}")
    W.pack()
    T = tk.Label(frame2, text=f"Time: {round(timeTaken, 2)} secs")
    T.pack()
    A = tk.Label(frame2, text=f"Accuracy: {round((SequenceMatcher(a=rnd, b=stg).ratio())*100, 2)} %")
    A.pack()
    S = tk.Label(frame2, text=f"Speed: {round(speed, 2)} words/min")
    S.pack()

def change_to_frame2():
    frame2.pack(fill='both', expand=1)
    frame1.forget()
    ready= tk.Label(frame2, text="Start Typing!!!!", fg="red", font=("times",30))
    ready.pack()

x= tk.Label(frame1, text="Welcome to Typing Speed Test!",fg='red',font=("times",50))
x.pack()
y=tk.Label(frame1, text="How would you like to start practicing?",fg='blue',font=("times",30))
y.pack()
       
btn=IntVar()

def check_box ():
    global rnd, timeStart
    if l.get()==1:
        change_to_frame2()
        letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        rnd=random.choice(letters)
        
        string.pack()
        r=tk.Label (frame2, text=rnd,font=("times",16))
        r.pack()
        timeStart = time.time()
        tk.Button(frame2,text="Submit",command=printValue).pack()
    elif s.get()==1:
        change_to_frame2()
        sent= ['This is uet lahore','I am a computer engineer','Wisdom is easily acquired when hiding under the bed with a saucepan on your head','Computer engineers are the best','Life has been a lot tougher these days','Mitochondria is the powerhouse of the cell','She sells she shells by the sea shore']
        rnd=random.choice(sent)
        
        string.pack()
        o=tk.Label(frame2, text=rnd,font=("times",16))
        o.pack()
        timeStart = time.time()
        btn= tk.Button(frame2,text="Submit",command=printValue).pack()
        
l= IntVar()
lc= Checkbutton(frame1, text="Letters",onvalue=1,offvalue=0,command=check_box, variable=l,bg="light blue",font=("times",20)).pack()
s= IntVar()
sc=Checkbutton(frame1, text="Sentences",onvalue=1, offvalue=0,command=check_box, variable=s,bg="light blue",font=("times",20)).pack()
root.mainloop()
   
