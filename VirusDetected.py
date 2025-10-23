import tkinter as tk
from tkinter import messagebox
from time import sleep
import tkinter.ttk as ttk

r=tk.Tk()
r.title('Virus Scanner')
r.geometry('300x200')

def scanVIR():
    # r.destroy()
    messagebox.showinfo('Scanning','Scanning for viruses....\nplease wait....')
    sleep(2)
    messagebox.showerror('Virus Detected!','Hey There,\nA virus has been detected with name of TrojanVirus.exe')
    messagebox.askquestion("Deletion",'Would you like to delete it?')
    # sleep(3)
    root=tk.Tk()
    root.title("Deletion Progress")
    root.geometry('200x100')
    

    progress=ttk.Progressbar(root, orient = 'horizontal',
              length = 100, mode = 'determinate')
    def Bar():
        progress['value'] = 20
        root.update_idletasks()
        sleep(2)

        progress['value'] = 40
        root.update_idletasks()
        sleep(1)

        progress['value'] = 50
        root.update_idletasks()
        sleep(1)

        progress['value'] = 60
        root.update_idletasks()
        sleep(2)

        progress['value'] = 80
        root.update_idletasks()
        sleep(1)
        progress['value'] = 100
        sleep(1.5)
        r.destroy

    showProgress=tk.Button(root,text='Start Deletion Process',command=Bar)
    progress.pack(pady = 10)
    showProgress.pack(pady=10)
    

    root.mainloop()
    messagebox.showinfo('Successfuly deleted','Succesfully deleted the virus with name TrojanVirus.exe')

def scanner():
    r.destroy()
    scanVIR()

startScan=tk.Button(r,text='Start Scanning process',command=scanner)
startScan.pack(pady=10)
r.mainloop()