from tkinter import *#type:ignore


r=Tk()
r.title('Event Handler')
r.geometry('400x500')

def SayPressed(event):
    print("You clicked")

buttonVAR=Button(r,text='Press')
buttonVAR.bind('<Button-1>', SayPressed)

buttonVAR.pack(pady=10)

def KeyPressed(event):#type:ignore
    print(f'You pressed {event.char}')#type:ignore

r.bind('<Key>', KeyPressed)#type:ignore
r.mainloop()