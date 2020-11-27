#!/usr/bin/env python3
from tkinter import *
from random import randint
from tkinter import messagebox
import time

root=Tk()
root.title("Flash Cards")
root.geometry("700x500")
root.resizable(False,False) #this avoids the program to being resizable
#root.iconbitmap("D:/Programming Stuff/Tkinter GUI Course/FlashCards App/rocket1.ico")

#initializing score values

#1 Add
val_add=IntVar(value=0);points_add=StringVar();points_add.set("Score: "+str(val_add.get()))
#2 subtract
val_subtract=IntVar(value=0);points_subtract=StringVar();points_subtract.set("Score: "+str(val_subtract.get()))
#3 multiply
val_multiply=IntVar(value=0);points_multiply=StringVar();points_multiply.set("Score: "+str(val_multiply.get()))
#4 divide
val_divide=IntVar(value=0);points_divide=StringVar();points_divide.set("Score: "+str(val_divide.get()))
#5 overall
val_total_score=IntVar(value=0)
val_total_score.set(val_add.get()+val_subtract.get()+val_multiply.get()+val_divide.get())
points_overall=StringVar()
points_overall.set("Total Score: "+str(val_total_score.get())+"\t\tAdd:"+str(val_add.get())+"    \t\tSubtract:"+str(val_subtract.get())+"\t\tmultiply:"+str(val_multiply.get())+"\t\tDivide:"+str(val_divide.get()))



#def all important functions

#function to check the answer is correct or not
def add_correct(event,num1,num2):

    correct=num1+num2
    #correct and incorrect message
    output_answer_correct=StringVar()
    output_answer_incorrect=StringVar()
    output_answer_correct.set("Correct "+ str(num1)+ " + " +str(num2)+ " = "+ str(correct))
    output_answer_incorrect.set("Incorrect "+ str(num1)+ " + " +str(num2)+ " = "+ str(correct)+ ", Not "+ answer_field.get())

    if (int(answer_field.get())==correct):
        add_correct_label.config(text=output_answer_correct.get(),bg="green")
        val_add.set(val_add.get()+1)
        points_add.set("Score: "+str(val_add.get()))
    else:
        add_correct_label.config(text=output_answer_incorrect.get(),bg="crimson")

    #clear the answer_field
    answer_field.delete(0,"end")

    #generate 2 new random numbers
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    add_flash.config(text=str(num_1.get())+" + "+ str(num_2.get()),font=("Tahoma",92))

def add():
    hide_frames()
    add_frame.pack(fill="both",expand=1)
    #updating statusbar value
    status.set("  Addition Cards")
    
    
    #creating random numbers
    global num_1
    global num_2
    num_1=IntVar()
    num_2=IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    

    #display random no in the screen
    score=Label(add_frame,textvariable=points_add,width=10).pack(anchor="w",pady=5,padx=3)

    global add_flash
    add_flash=Label(add_frame,text=str(num_1.get())+" + "+ str(num_2.get()),font=("Tahoma",92))
    add_flash.pack(pady=35)

    #Answer box
    global answer_field
    answer_field=Entry(add_frame,width=25)
    answer_field.bind("<Return>",lambda a:add_correct(a,num_1.get(),num_2.get()))
    answer_field.pack(pady=8)

    button=Button(add_frame,text="Answer")
    button.bind("<ButtonPress-1>",lambda a: add_correct(a,num_1.get(),num_2.get()))
    button.pack(pady=20)

    #display correct and incorrect answer
    global add_correct_label
    add_correct_label=Label(add_frame,text="",bg="#069") 
    add_correct_label.pack(pady=8)
    
def subtract_correct(event,num1,num2):

    correct=num1-num2
    #correct and incorrect message
    output_answer_correct=StringVar()
    output_answer_incorrect=StringVar()
    output_answer_correct.set("Correct "+ str(num1)+ " - " +str(num2)+ " = "+ str(correct))
    output_answer_incorrect.set("Incorrect "+ str(num1)+ " - " +str(num2)+ " = "+ str(correct)+ ", Not "+ answer_field.get())

    if (int(answer_field.get())==correct):
        subtract_correct_label.config(text=output_answer_correct.get(),bg="green")
        val_subtract.set(val_subtract.get()+1)
        points_subtract.set("Score: "+str(val_subtract.get()))
    else:
        subtract_correct_label.config(text=output_answer_incorrect.get(),bg="crimson")

    #clear the answer_field
    answer_field.delete(0,"end")

    #generate 2 new random numbers
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))

    if (num_2.get()>num_1.get()):
        temp=num_1.get()
        num_1.set(num_2.get())
        num_2.set(temp)

    subtract_flash.config(text=str(num_1.get())+" - "+ str(num_2.get()),font=("Tahoma",92))

def subtract():
    hide_frames()
    subtract_frame.pack(fill="both",expand=1)
    #updating statusbar value
    status.set("  Subtraction Cards")
    
    #creating random numbers
    global num_1
    global num_2
    num_1=IntVar()
    num_2=IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    
    #Condition to avoid negaetive answer by swaping numbers
    if (num_2.get()>num_1.get()):
        temp=num_1.get()
        num_1.set(num_2.get())
        num_2.set(temp)


    #display random no in the screen
    score=Label(subtract_frame,textvariable=points_subtract,width=10).pack(anchor="w",pady=5,padx=3)

    global subtract_flash
    subtract_flash=Label(subtract_frame,text=str(num_1.get())+" - "+ str(num_2.get()),font=("Tahoma",92))
    subtract_flash.pack(pady=35)

    #Answer box
    global answer_field
    answer_field=Entry(subtract_frame,width=25)
    answer_field.bind("<Return>",lambda a: subtract_correct(a,num_1.get(),num_2.get()))
    answer_field.pack(pady=8)

    button=Button(subtract_frame,text="Answer")
    button.bind("<ButtonPress-1>",lambda a: subtract_correct(a,num_1.get(),num_2.get()))
    button.pack(pady=20)

    #display correct and incorrect answer
    global subtract_correct_label
    subtract_correct_label=Label(subtract_frame,text="",bg="#069") 
    subtract_correct_label.pack(pady=8)



def multiply_correct(event,num1,num2):

    correct=num1*num2
    #correct and incorrect message
    output_answer_correct=StringVar()
    output_answer_incorrect=StringVar()
    output_answer_correct.set("Correct "+ str(num1)+ " x " +str(num2)+ " = "+ str(correct))
    output_answer_incorrect.set("Incorrect "+ str(num1)+ " x " +str(num2)+ " = "+ str(correct)+ ", Not "+ answer_field.get())

    if (int(answer_field.get())==correct):
        multiply_correct_label.config(text=output_answer_correct.get(),bg="green")
        val_multiply.set(val_multiply.get()+1)
        points_multiply.set("Score: "+str(val_multiply.get()))
    else:
        multiply_correct_label.config(text=output_answer_incorrect.get(),bg="crimson")

    #clear the answer_field
    answer_field.delete(0,"end")

    #generate 2 new random numbers
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    multiply_flash.config(text=str(num_1.get())+" x "+ str(num_2.get()),font=("Tahoma",92))

def multiply():
    hide_frames()
    multiply_frame.pack(fill="both",expand=1)
    #updating statusbar value
    status.set("  Multiplication Cards")
    
    #creating random numbers
    global num_1
    global num_2
    num_1=IntVar()
    num_2=IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    

    #display random no in the screen
    score=Label(multiply_frame,textvariable=points_multiply,width=10).pack(anchor="w",pady=5,padx=3)

    global multiply_flash
    multiply_flash=Label(multiply_frame,text=str(num_1.get())+" x "+ str(num_2.get()),font=("Tahoma",92))
    multiply_flash.pack(pady=35)

    #Answer box
    global answer_field
    answer_field=Entry(multiply_frame,width=25)
    answer_field.bind("<Return>",lambda a: multiply_correct(a,num_1.get(),num_2.get()))
    answer_field.pack(pady=8)

    button=Button(multiply_frame,text="Answer")
    button.bind("<ButtonPress-1>",lambda a: multiply_correct(a,num_1.get(),num_2.get()))
    button.pack(pady=20)

    #display correct and incorrect answer
    global multiply_correct_label
    multiply_correct_label=Label(multiply_frame,text="",bg="#069") 
    multiply_correct_label.pack(pady=8)


def divide_correct(event,num1,num2):

    correct=round(num1/num2,2)
    #correct and incorrect message
    output_answer_correct=StringVar()
    output_answer_incorrect=StringVar()
    output_answer_correct.set("Correct "+ str(num1)+ " ÷ " +str(num2)+ " = "+ str(correct))
    output_answer_incorrect.set("Incorrect "+ str(num1)+ " ÷ " +str(num2)+ " = "+ str(correct)+ ", Not "+ answer_field.get())

    if (float(answer_field.get())==correct):
        divide_correct_label.config(text=output_answer_correct.get(),bg="green")
        val_divide.set(val_divide.get()+1)
        points_divide.set("Score: "+str(val_divide.get()))
    else:
        divide_correct_label.config(text=output_answer_incorrect.get(),bg="crimson")

    #clear the answer_field
    answer_field.delete(0,"end")

    #generate 2 new random numbers
    num_1.set(randint(0,100))
    num_2.set(randint(1,100))
    divide_flash.config(text=str(num_1.get())+" ÷ "+ str(num_2.get()),font=("Tahoma",92))

def divide():
    hide_frames()
    divide_frame.pack(fill="both",expand=1)

    #updating statusbar value
    status.set("  Division Cards")
    
    #creating random numbers
    global num_1
    global num_2
    num_1=IntVar()
    num_2=IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(1,100))
    
    #display random no in the screen
    score=Label(divide_frame,textvariable=points_divide,width=10).pack(anchor="w",pady=5,padx=3)

    global divide_flash
    divide_flash=Label(divide_frame,text=str(num_1.get())+" ÷ "+ str(num_2.get()),font=("Tahoma",92)) # to type ÷ Symbol turn on caps lock press/hold
    divide_flash.pack(pady=35)                                                                             # alt and type 0247 with numpad

    #Answer box
    global answer_field
    answer_field=Entry(divide_frame,width=35)
    answer_field.bind("<Return>",lambda a: divide_correct(a,num_1.get(),num_2.get()))
    answer_field.pack(pady=8)

    button=Button(divide_frame,text="Answer")
    button.bind("<ButtonPress-1>",lambda a: divide_correct(a,num_1.get(),num_2.get()))
    button.pack(pady=20)

    #display correct and incorrect answer
    global divide_correct_label
    divide_correct_label=Label(divide_frame,text="" ,bg="#069") 
    divide_correct_label.pack(pady=8)

#About message-boxes
def About1():
    messagebox.showinfo("About","Developer:\tRAVINDER SINGH \n\nInstitution:\tAIT Pune\n\nYear & Branch:\tFE E&TC")
def About2():
    messagebox.showinfo("Version","Product:     Flash Cards App \n\nBuild:\t   2020.H.5296.Q1\n\nUser:\t   Registered")

def home_Menu():
    hide_frames()
    start_frame.pack(fill="both",expand=1)
    #updating statusbar value
    status.set("  HOME ")
    
    val_total_score.set(val_add.get()+val_subtract.get()+val_multiply.get()+val_divide.get())
    points_overall.set("Total Score: "+str(val_total_score.get())+"\t\tAdd:"+str(val_add.get())+"    \t\tSubtract:"+str(val_subtract.get())+"\t\tmultiply:"+str(val_multiply.get())+"\t\tDivide:"+str(val_divide.get()))

    

def hide_frames():
    #destroying individual children widgets
    for widget in add_frame.winfo_children():
        widget.destroy()
    
    for widget in subtract_frame.winfo_children():
        widget.destroy()
    
    for widget in multiply_frame.winfo_children():
        widget.destroy()
    
    for widget in divide_frame.winfo_children():
        widget.destroy()

    #hide all frames
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()
    start_frame.pack_forget()

#Adding a menu bar
my_menu=Menu(root)
root.config(menu=my_menu)

#ceating Home Menu
home=Menu(my_menu)
my_menu.add_cascade(label="Home",menu=home)
home.add_command(label="Go to Home",command=home_Menu)


#create menu items
math_menu=Menu(my_menu)
my_menu.add_cascade(label="Math Cards",menu=math_menu)
math_menu.add_command(label="Add",command=add)
math_menu.add_command(label="Subtract",command=subtract)
math_menu.add_command(label="Multiply",command=multiply)
math_menu.add_command(label="Divide",command=divide)
math_menu.add_separator()
math_menu.add_command(label="Quit",command=root.quit)

#creating about menu
about=Menu(my_menu)
my_menu.add_cascade(label="About",menu=about)
about.add_command(label="Developer Info",comman=About1)
about.add_command(label="Product Info",comman=About2)

#create frames
add_frame=Frame(root,height=500,width=700,bg="#069")
subtract_frame=Frame(root,height=500,width=700,bg="#069")
multiply_frame=Frame(root,height=500,width=700,bg="#069")
divide_frame=Frame(root,height=500,width=700,bg="#069")

#score label to display to user


#create start frame

start_frame=Frame(root,height=500,width=700,bg="#069")
start_frame.pack(fill="both",expand=1)

#adding overall score daisply
total_score=Label(start_frame,textvariable=points_overall,width=70,anchor="w")
total_score.pack(anchor="w",pady=10,padx=3,fill="x")

welcom_labl=Label(start_frame,text="Welcome FlashCard User",font=("Helvetica",42),bg="#069",fg="gold",relief="raised",width=100).pack(pady=25)
add_button=Button(start_frame,text="Addition Maths FlashCard",command=add,width=35).pack(pady=10)
subtract_button=Button(start_frame,text="Subtraction Maths FlashCard",command=subtract,width=35).pack(pady=10)
multiply_button=Button(start_frame,text="Multiplication Maths FlashCard",command=multiply,width=35).pack(pady=10)
division_button=Button(start_frame,text="Division Maths FlashCard",command=divide,width=35).pack(pady=10)

#status Bar
global status
status=StringVar(value="  HOME")
status_bar= Label(root,textvariable=status,bd=1,relief=SUNKEN,anchor=W)
status_bar.pack(side=BOTTOM, fill=X)


root.mainloop()










