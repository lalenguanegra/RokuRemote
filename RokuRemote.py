import subprocess 
from subprocess import call
from tkinter import *
import webbrowser
window = Tk()
root = Tk()
frame = Frame(root)
frame.pack()
def OpenYoutube():
    subprocess.call("Youtube.py", shell=True)
window.title("Sadie Socio's")
lbl = Label(window, text="Roku Remote", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.wm_iconbitmap('drip.ico')
def OpenUp():
    subprocess.call("Up.py", shell=True)
def OpenDown():
    subprocess.call("Down.py", shell=True)
def OpenLeft():
    subprocess.call("Left.py", shell=True)
def OpenRight():
    subprocess.call("Right.py", shell=True)
def OpenBack():
    subprocess.call("Back.py", shell=True)
def OpenSelect():
    subprocess.call("Select.py", shell=True)
def OpenOn():
    subprocess.call("PowerOn.py", shell=True)
def OpenOff():
    subprocess.call("PowerOff.py", shell=True)
def command():
    Toplevel(root)
root.title("")
b1 = Button(root, text="Youtube", command= OpenYoutube, height=1, width=8, font=("Arial Bold", 30))
b2 = Button(root, text="Up", command= OpenUp, height=1, width=8, font=("Arial Bold", 30))
b3 = Button(root, text="Down", command= OpenDown, height=1, width=8, font=("Arial Bold", 30))
b4 = Button(root, text="Left", command= OpenLeft, height=1, width=8, font=("Arial Bold", 30))
b5 = Button(root, text="Right", command= OpenRight, height=1, width=8, font=("Arial Bold", 30))
b6 = Button(root, text="Back", command= OpenBack, height=1, width=8, font=("Arial Bold", 30))
b7 = Button(root, text="Select", command= OpenSelect, height=1, width=8, font=("Arial Bold", 30))
b8 = Button(root, text="On", command= OpenOn, height=1, width=8, font=("Arial Bold", 30))
b9 = Button(root, text="Off", command= OpenOff, height=1, width=8, font=("Arial Bold", 30))
root.wm_iconbitmap('drip.ico')
window.geometry("500x100+300+300")
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
b9.pack()
window.mainloop()