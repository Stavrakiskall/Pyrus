import time
import pyttsx3
import pyautogui
import tkinter as tk
import speech_recognition
import os
import sys
import winsound
from PIL import Image, ImageTk

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)

def speakText(command):
    engine = pyttsx3.init() 
    rate = engine.getProperty('rate') 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  
    engine.setProperty('rate',  rate-1000) 
    engine.say(command)
    engine.runAndWait()

def initiate(event):
    updateImg(1, 2)
    winsound.PlaySound(dir + '/noise1.wav', winsound.SND_FILENAME)
    updateImg(2, 3)
    updateImg(3, 2)
    updateImg(4, 3)
    updateImg(5, 3)
    winsound.PlaySound(dir + '/noise3.wav', winsound.SND_FILENAME)
    updateImg(7, 0.5)
    winsound.PlaySound(dir + '/noise2.wav', winsound.SND_FILENAME)
    updateImg(5, 0.3)
    winsound.PlaySound(dir + '/noise1.wav', winsound.SND_FILENAME)
    winsound.PlaySound(dir + '/noise3.wav', winsound.SND_FILENAME)
    updateImg(6, 3)
    winsound.PlaySound(dir + '/noise1.wav', winsound.SND_FILENAME)
    winsound.PlaySound(dir + '/noise3.wav', winsound.SND_FILENAME)
    winsound.PlaySound(dir + '/noise1.wav', winsound.SND_FILENAME)
    winsound.PlaySound(dir + '/noise2.wav', winsound.SND_FILENAME)
    speakText("Your pc will explode in")
    speakText("in 5")
    speakText("4")
    speakText("3")
    speakText("2")
    speakText("1")
    speakText("Explosion")
    os.system('shutdown -s')

def updateGif(imgNo, timeNo):
    imgName = dir+"/BSOD/bsodgif/frame_"+str(imgNo)+"_delay-0.05s.png"
    img = Image.open(imgName).resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)
    bglabel.configure(image = bg1, cursor = "none")
    bglabel.image = bg1
    window.update()
    time.sleep(timeNo)

def updateImg(imgNo, timeNo):
    imgName = dir+"/BSOD/bsod"+str(imgNo)+".png"
    img = Image.open(imgName).resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)
    bglabel.configure(image = bg1, cursor = 'none')
    bglabel.image = bg1
    window.update()
    time.sleep(timeNo)

time.sleep(1)
pyautogui.hotkey("win" , "d")
time.sleep(1)
ps = pyautogui.screenshot("desktop.png")

window = tk.Tk()
window.geometry("{}x{}+0+0".format(window.winfo_screenwidth() , window.winfo_screenheight()))

bg = tk.PhotoImage(file="desktop.png")
bglabel = tk.Label(window , image = bg, width= window.winfo_screenwidth() , height= window.winfo_screenheight())

bglabel.place (x = 0 , y = 0)

time.sleep(2)

bglabel.bind("<Button-1>" , initiate)
window.attributes("-fullscreen" , True)
window.attributes("-topmost", True)
window.bind()
window.update()

window.mainloop()
