import tkinter as tk
import tkinter.messagebox as tkmsg

r=tk.Tk()
r.geometry('400x400')
r.title("Length Converter App")

def converter():
    inches=float(inch.get())
    centimeters=inches*2.54
    tkmsg.showinfo('Answer',f'{inches} inch is equal to {centimeters} centimeters')



inch=tk.Entry(r)
inch.pack(pady=10)
submit=tk.Button(r,text='Convert',command=converter).pack(pady=10)
r.mainloop()    