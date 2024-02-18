
from tkinter import *
import tkinter.font as font

#functions
#0
def display_0():
    k1=dis.get()
    k1=k1+'0'
    dis.delete(0,END)
    dis.insert(0,k1)
#1
def display_1():
    k1=dis.get()
    k1=k1+'1'
    dis.delete(0,END)
    dis.insert(0,k1)
#2
def display_2():
    k1=dis.get()
    k1=k1+'2'
    dis.delete(0,END)
    dis.insert(0,k1)
#3
def display_3():
    k1=dis.get()
    k1=k1+'3'
    dis.delete(0,END)
    dis.insert(0,k1)
#4
def display_4():
    k1=dis.get()
    k1=k1+'4'
    dis.delete(0,END)
    dis.insert(0,k1)
#5
def display_5():
    k1=dis.get()
    k1=k1+'5'
    dis.delete(0,END)
    dis.insert(0,k1)
#6
def display_6():
    k1=dis.get()
    k1=k1+'6'
    dis.delete(0,END)
    dis.insert(0,k1)
#7
def display_7():
    k1=dis.get()
    k1=k1+'7'
    dis.delete(0,END)
    dis.insert(0,k1)
#8
def display_8():
    k1=dis.get()
    k1=k1+'8'
    dis.delete(0,END)
    dis.insert(0,k1)
#9
def display_9():
    k1=dis.get()
    k1=k1+'9'
    dis.delete(0,END)
    dis.insert(0,k1)
#+
def display_sum():
    k1=dis.get()
    if len(k1)>0 and k1.find('+')==-1 and k1.find('-')==-1 and k1.find('*')==-1 and k1.find('/')==-1:
        k1=k1+'+'
        dis.delete(0, END)
        dis.insert(0,k1)
#-
def display_min():
    k1=dis.get()
    if len(k1)>0 and k1.find('+')==-1 and k1.find('-')==-1 and k1.find('*')==-1 and k1.find('/')==-1:
        k1=k1+'-'
        dis.delete(0, END)
        dis.insert(0,k1)
#*
def display_mul():
    k1=dis.get()
    if len(k1) > 0 and k1.find('+') == -1 and k1.find('-') == -1 and k1.find('*') == -1 and k1.find('/') == -1:
        k1=k1+'*'
        dis.delete(0, END)
        dis.insert(0,k1)
#/
def display_div():
    k1=dis.get()
    if len(k1) > 0 and k1.find('+') == -1 and k1.find('-') == -1 and k1.find('*') == -1 and k1.find('/') == -1:
        k1=k1+'/'
        dis.delete(0, END)
        dis.insert(0,k1)
#.
def display_dot():
    k1=dis.get()
    if k1.find('+')==-1 and k1.find('-') == -1 and k1.find('*') == -1 and k1.find('/') == -1:
        if k1.find('.')==-1:
            k1=k1+'.'
            dis.delete(0, END)
            dis.insert(0,k1)
    else:
        if k1.find('+')!=-1:
            f1=k1.find('+')
        if k1.find('-') != -1:
            f1 = k1.find('-')
        if k1.find('*') != -1:
            f1 = k1.find('*')
        if k1.find('/') != -1:
            f1 = k1.find('/')
        if k1[f1:len(k1)].find('.')==-1:
            k1 = k1 + '.'
            dis.delete(0, END)
            dis.insert(0, k1)
#Clear
def display_clear():
    k1=dis.get()
    k2=str()
    if len(k1)>0:
        for i in range(len(k1)-1):
            k2=k2+k1[i]
    dis.delete(0, END)
    dis.insert(0, k2)
#equ
def display_equ():
    k1=dis.get()
    if len(k1)>0:
        if k1.find('+')!=-1 or k1.find('-')!=-1 or k1.find('*')!=-1 or k1.find('/')!=-1:
            k3 = float()
            if '+' in k1:
                f1=k1.find('+')
                k3=float(k1[0:f1])+float(k1[f1+1:len(k1)+1])
            if '-' in k1:
                f1 = k1.find('-')
                k3 = float(k1[0:f1]) - float(k1[f1+1:len(k1) + 1])
            if '*' in k1:
                f1 = k1.find('*')
                k3 = float(k1[0:f1]) * float(k1[f1+1:len(k1) + 1])
            if '/' in k1:
                f1 = k1.find('/')
                k3 = float(k1[0:f1]) / float(k1[f1+1:len(k1) + 1])
            dis.delete(0, END)
            dis.insert(0, k3)


window=Tk()
# add widgets here
window.title('HM calculator')
window.geometry("200x260+100+200")

#Location variables
k_y=int(-40)
ks=int(0)  #auxiliary variable for counting the number of symbols(+,-,*,/)

#Switch "0"
B_0=Button(window, text="0", fg='blue', width='4',height='2',command=display_0)
B_0.place(x=55, y=k_y+250)
#Switch "1"
B_1=Button(window, text='1', fg='blue', width='4', height='2',command=display_1)
B_1.place(x=10,y=k_y+205)
#Switch "2"
B_2=Button(window, text='2', fg='blue', width='4', height='2',command=display_2)
B_2.place(x=55,y=k_y+205)
#Switch "3"
B_3=Button(window, text='3', fg='blue', width='4', height='2',command=display_3)
B_3.place(x=100,y=k_y+205)
#Switch "4"
B_4=Button(window, text='4', fg='blue', width='4', height='2',command=display_4)
B_4.place(x=10,y=k_y+160)
#Switch "5"
B_5=Button(window, text='5', fg='blue', width='4', height='2',command=display_5)
B_5.place(x=55,y=k_y+160)
#Switch "6"
B_6=Button(window, text='6', fg='blue', width='4', height='2',command=display_6)
B_6.place(x=100,y=k_y+160)
#Switch "7"
B_7=Button(window, text='7', fg='blue', width='4', height='2',command=display_7)
B_7.place(x=10,y=k_y+115)
#Switch "8"
B_8=Button(window, text='8', fg='blue', width='4', height='2',command=display_8)
B_8.place(x=55,y=k_y+115)
#Switch "9"
B_9=Button(window, text='9', fg='blue', width='4', height='2',command=display_9)
B_9.place(x=100,y=k_y+115)
#Switch "+"
B_sum=Button(window, text='+', fg='blue', width='4', height='2',command=display_sum)
B_sum.place(x=145,y=k_y+205)
#Switch "-"
B_min=Button(window, text='-', fg='blue', width='4', height='2',command=display_min)
B_min.place(x=145,y=k_y+160)
#Switch "*"
B_mul=Button(window, text='*', fg='blue', width='4', height='2',command=display_mul)
B_mul.place(x=145,y=k_y+115)
#Switch "="
B_equ=Button(window, text='=', fg='blue', width='4', height='2',command=display_equ)
B_equ.place(x=145,y=k_y+250)
#Switch "."
B_dot=Button(window, text='.', fg='blue', width='4', height='2',command=display_dot)
B_dot.place(x=100,y=k_y+250)
#Switch "/"
B_div=Button(window, text='/', fg='blue', width='4', height='2',command=display_div)
B_div.place(x=145,y=k_y+70)
#Switch clear
B_clear=Button(window, text='Clear', fg='blue', width='4',height='2', command=display_clear)
B_clear.place(x=100,y=k_y+70)
#Display
dis=Entry(window, font=("Helvetica",12))
dis.place(x=10, y=k_y+45)



window.mainloop()
