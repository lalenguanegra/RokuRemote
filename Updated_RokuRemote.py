import requests
import subprocess 
from subprocess import call
from tkinter import *
import webbrowser
window = Tk()
root = Tk()
frame = Frame(root)
frame.pack()
def OpenGithub():
    url = 'https://github.com/lalenguanegra/RokuRemote'
    webbrowser.open_new(url)
def OpenYoutube():
    request_url = "http://192.168.0.21:8060/launch/837"
    requests.post(request_url)
window.title("Sadie Socio's")
lbl = Button(window, text="Roku Remote", command=OpenGithub, width=50, font=("Arial Bold", 50))
window.wm_iconbitmap('drip.ico')
def OpenUp():
    request_url = "http://192.168.0.21:8060/keypress/Up"
    requests.post(request_url)
def OpenDown():
    request_url = "http://192.168.0.21:8060/keypress/Down"
    requests.post(request_url)
def OpenLeft():
    request_url = "http://192.168.0.21:8060/keypress/Left"
    requests.post(request_url)
def OpenRight():
    request_url = "http://192.168.0.21:8060/keypress/Right"
    requests.post(request_url)
def OpenBack():
    request_url = "http://192.168.0.21:8060/keypress/back"
    requests.post(request_url)
def OpenSelect():
    request_url = "http://192.168.0.21:8060/keypress/select"
    requests.post(request_url)
def OpenOn():
    request_url = "http://192.168.0.21:8060/keypress/poweron"
    requests.post(request_url)
def OpenOff():
    request_url = "http://192.168.0.21:8060/keypress/poweroff"
    requests.post(request_url)
def OpenPlayPause():
    request_url = "http://192.168.0.21:8060/keypress/play"
    requests.post(request_url)
def command():
    Toplevel(root)
root.title("")
b1 = Button(root, text="Youtube", command= OpenYoutube, height=1, width=8, font=("Arial Bold", 28))
b2 = Button(root, text="Up", command= OpenUp, height=1, width=8, font=("Arial Bold", 28))
b3 = Button(root, text="Down", command= OpenDown, height=1, width=8, font=("Arial Bold", 28))
b4 = Button(root, text="Left", command= OpenLeft, height=1, width=8, font=("Arial Bold", 28))
b5 = Button(root, text="Right", command= OpenRight, height=1, width=8, font=("Arial Bold", 28))
b6 = Button(root, text="Back", command= OpenBack, height=1, width=8, font=("Arial Bold", 28))
b7 = Button(root, text="Select", command= OpenSelect, height=1, width=8, font=("Arial Bold", 28))
b8 = Button(root, text="On", command= OpenOn, height=1, width=8, font=("Arial Bold", 28))
b9 = Button(root, text="Off", command= OpenOff, height=1, width=8, font=("Arial Bold", 28))
b10 = Button(root, text="PlayPause", command= OpenPlayPause, height=1, width=8, font=("Arial Bold", 28))
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
b10.pack()
lbl.pack()
b1.config(bg="#6600cc")
b2.config(bg="#9933ff")
b3.config(bg="#9933ff")
b4.config(bg="#b3003b")
b5.config(bg="#b3003b")
b6.config(bg="#1a1aff")
b7.config(bg="#00e600")
b8.config(bg="#b3003b")
b9.config(bg="#b3003b")
b10.config(bg="#8a00e6")
lbl.config(bg="#b3003b")
window.mainloop()
