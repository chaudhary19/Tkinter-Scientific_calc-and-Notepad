from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
from math import sin,cos,tan,log


def getvals(event):
    value = event.widget.cget('text')
    if value=='Clr':
        sc_variable.set('')
    elif value=='=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
        except Exception as e:
            sc_variable.set('Error - Wait for 3 sec')
            screen.update()
            status_var.set('Preparing...')
            screen.update()
            time.sleep(3)
            sc_variable.set('')
            screen.update()
            status_var.set('Ready..')
            screen.update()

    else:
        sc_variable.set(f'{sc_variable.get()}{value}')



def term_of_use():
    tmsg.showinfo('Terms of Use ','IF YOU LIVE IN (OR IF YOUR PRINCIPAL PLACE OF BUSINESS IS IN) THE UNITED STATES, PLEASE READ THE BINDING ARBITRATION CLAUSE AND CLASS ACTION WAIVER IN SECTION 11. IT AFFECTS HOW DISPUTES ARE RESOLVED.')

def send_feedback():
    ans=tmsg.askquestion('Feedback Hub','Was your experience good with us ? ')
    if ans=='yes':
        tmsg.showinfo('Feedback','Please Rate us on PlayStore')
    else:
        tmsg.showinfo('Feedback','We will contact you soon to know about your bad experience')

root=Tk()
canvas_width=555
canvas_height=620
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
root.title('CalCulator @ Chaudhary_19')
root.wm_iconbitmap('calculator.png')




my_menu=Menu(root)
m1=Menu(my_menu,tearoff=0,fg='red')
m1.add_command(label='Terms of Use',command=term_of_use)
m1.add_command(label='Send Feedback',command=send_feedback)
root.config(menu=my_menu)
my_menu.add_cascade(label=' About ',menu=m1)
my_menu.add_command(label='Exit',command=quit)


sc_variable=StringVar()
screen=Entry(root,textvariable=sc_variable,font='lucida 35 bold',fg='yellow',bg='black')
screen.pack(pady=10)


f=Frame(root,padx=20,pady=20)
f.pack()
b1=Button(f,text='7',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b1.pack(side=LEFT,padx=5)
b2=Button(f,text='8',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b2.pack(side=LEFT,padx=5)
b3=Button(f,text='9',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b3.pack(side=LEFT,padx=5)
b4=Button(f,text='*',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b4.pack(side=LEFT,padx=5)
b5=Button(f,text='sin',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b5.pack(side=LEFT,padx=5)
b6=Button(f,text='(',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b6.pack(side=LEFT,padx=5)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)


f=Frame(root,padx=20,pady=20)
f.pack()
b1=Button(f,text='4',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b1.pack(side=LEFT,padx=5)
b2=Button(f,text='5',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b2.pack(side=LEFT,padx=5)
b3=Button(f,text='6',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b3.pack(side=LEFT,padx=5)
b4=Button(f,text='-',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b4.pack(side=LEFT,padx=5)
b5=Button(f,text='cos',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b5.pack(side=LEFT,padx=5)
b6=Button(f,text=')',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b6.pack(side=LEFT,padx=5)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)

f=Frame(root,padx=20,pady=20)
f.pack()
b1=Button(f,text='1',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b1.pack(side=LEFT,padx=5)
b2=Button(f,text='2',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b2.pack(side=LEFT,padx=5)
b3=Button(f,text='3',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b3.pack(side=LEFT,padx=5)
b4=Button(f,text='+',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b4.pack(side=LEFT,padx=5)
b5=Button(f,text='tan',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b5.pack(side=LEFT,padx=5)
b6=Button(f,text='%',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b6.pack(side=LEFT,padx=5)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)

f=Frame(root,padx=20,pady=20)
f.pack()
b1=Button(f,text='.',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b1.pack(side=LEFT,padx=5)
b2=Button(f,text='0',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b2.pack(side=LEFT,padx=5)
b3=Button(f,text='=',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b3.pack(side=LEFT,padx=5)
b4=Button(f,text='/',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b4.pack(side=LEFT,padx=5)
b5=Button(f,text='Clr',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b5.pack(side=LEFT,padx=5)
b6=Button(f,text='log',font='lucida 30 bold',padx=5,borderwidth=3,fg='yellow',bg='black')
b6.pack(side=LEFT,padx=5)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)

status_var=StringVar()
status_var.set('Ready..')
Label(root,textvariable=status_var,relief=SUNKEN,anchor='w',borderwidth=2,bg='yellow',fg='red').pack(side=BOTTOM,fill=X)

root.mainloop()