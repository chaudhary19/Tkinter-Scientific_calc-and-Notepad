from tkinter import *
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import askopenfilename,askopenfile,asksaveasfile,asksaveasfilename

def new():
    global file
    root.title('Untitled - Notepad')
    file=None
    Textarea.delete(1.0, END)

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text documents','*.txt')])

        if file=='':
            file=None
        else:
            #Save as a new file
            f=open(file, 'w')
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad ")

    else:
        # Save the new file
        f = open(file, 'w')
        f.write(Textarea.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + " - Notepad ")

def Open():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text documents','*.txt')])
    if file=='':
        file=None
    else:
        root.title(os.path.basename(file+" - Notepad"))
        Textarea.delete(1.0, END)
        f=open(file, 'r')
        Textarea.insert(1.0, f.read())
        f.close()



def cut():
    Textarea.event_generate(('<<Cut>>'))

def copy():
    Textarea.event_generate(('<<Copy>>'))

def paste():
    Textarea.event_generate(('<<Paste>>'))

def view_help():
    tmsg.showinfo('help'," We will contact you soon")

def about_notepad():
    tmsg.showinfo('About Notepad','This Notepad is created by Mayank Chaudhary @chaudhary_19')

def Appquit():
    root.destroy()

# Right Click Menu Function
def rightClickMenu(event):
    global menu
    menu = Menu(root, tearoff = 0)
    menu.add_command(label = "Cut")
    menu.add_command(label = "Copy")
    menu.add_command(label = "Paste")

def showRightClickMenu(event):
    eventWidget = event.widget
    menu.entryconfigure(
        "Cut",
        command=lambda: eventWidget.event_generate("<<Cut>>")
    )
    menu.entryconfigure(
        "Copy",
        command=lambda: eventWidget.event_generate("<<Copy>>")
    )
    menu.entryconfigure(
        "Paste",
        command=lambda: eventWidget.event_generate("<<Paste>>")
    )
    menu.tk.call("tk_popup", menu, event.x_root, event.y_root)


root=Tk()
root.geometry('688x700')
# I m not going to use minsize & maxsize here...
root.title('Untitled - Notepad')
# root.wm_iconbitmap('calculator.png')

#Calling Right Click Menu
rightClickMenu(root)

menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
m1.add_command(label='New',command=new)
m1.add_command(label='Save',command=save)
m1.add_command(label='Open',command=Open)
m1.add_separator()
m1.add_command(label='Exit',command=Appquit)

root.config(menu=menubar)
menubar.add_cascade(label='File',menu=m1)

m2=Menu(menubar,tearoff=0)
m2.add_command(label='Cut',command=cut)
m2.add_command(label='Copy',command=copy)
m2.add_command(label='Paste',command=paste)

root.config(menu=menubar)
menubar.add_cascade(label='Edit',menu=m2)

m3=Menu(menubar,tearoff=0)
m3.add_command(label='View Help',command=view_help)
m3.add_command(label='About Notepad',command=about_notepad)
root.config(menu=menubar)
menubar.add_cascade(label='Help',menu=m3)

Textarea=Text(root,font='lucida 13')
file=None
Textarea.pack(expand=True,fill=BOTH)

# Binding Right Click Menu to Right button (Mouse)
root.bind_class("Text", "<Button-3><ButtonRelease-3>", showRightClickMenu)

scrollbar=Scrollbar(Textarea)
scrollbar.pack(side=RIGHT,fill=Y)
Textarea.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Textarea.yview)




root.mainloop()
