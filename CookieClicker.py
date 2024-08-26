from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk

window = ctk.CTk()
window.geometry("520x540")
window.title("CookieClicker")
#window.config(bg="")

ctk.set_appearance_mode("dark")

StartFrame = ctk.CTkFrame(window, width=520, height=540, fg_color="transparent")
StartFrame.pack()
        

MainFrame = ctk.CTkFrame(window, width=520, height=540, fg_color="transparent")


def StartGame():
        StartFrame.pack_forget()
        MainFrame.pack()

def BackToMainMenu():
        MainFrame.pack_forget()
        StartFrame.pack()

CookieCount = 0
def AddCookieClickCount():
        global CookieCount
        CookieCount += 1
        print("+1 Cookie")
        CookieCountDisplay.configure(text=str(CookieCount))
        return CookieCount 


def PrintCookieCount():
        print(CookieCount)

#Save/Load System
def Save():
        f = open("Saves\save1", W)
        f.write(str(CookieCount))
        f.close()

def Load():
         global CookieCount
         f = open("Saves\save1", "r")
         ToBeLoadedCookie = f.readline()
         CookieCount = int(ToBeLoadedCookie)
         CookieCountDisplay.configure(text=(CookieCount))
         return CookieCount


introduction = ctk.CTkLabel(MainFrame,text="Click me!!!")
introduction.configure(font=("Ink Free",22,"bold"))
introduction.pack()

CookieCountDisplay = ctk.CTkLabel(MainFrame,text=CookieCount)
CookieCountDisplay.pack()

#Cookie button
CookieButtonIcon = ImageTk.PhotoImage(file="Assets\Cookie.png")
CookieButton = ctk.CTkButton(MainFrame,image=CookieButtonIcon,text="")
CookieButton.configure(command=lambda:[AddCookieClickCount(), PrintCookieCount()])
CookieButton.configure(hover_color="#1e1e1e") #1e1e1e
CookieButton.configure(fg_color="#242424") #242424
CookieButton.pack()
#Start image
StartMenuImage = ctk.CTkLabel(StartFrame,image=CookieButtonIcon,text="")
StartMenuImage.pack()
#Save button
SaveButton = ctk.CTkButton(MainFrame,text="Save",corner_radius=15)
SaveButton.configure(command=Save)
SaveButton.pack()
#Load button
LoadButton = ctk.CTkButton(MainFrame,text="Load",corner_radius=15)
LoadButton.configure(command=Load)
LoadButton.pack()
#Return to menu button
ReturnToMenuButton = ctk.CTkButton(MainFrame,text="Return to main menu",corner_radius=15)
ReturnToMenuButton.configure(command=BackToMainMenu)
ReturnToMenuButton.pack()
#Start button
StartButton = ctk.CTkButton(StartFrame,text="Start",corner_radius=15)
StartButton.configure(command=StartGame)
StartButton.pack()
#Load button
LoadButton_StartFrame = ctk.CTkButton(StartFrame,text="Load Save",corner_radius=15)
LoadButton_StartFrame.configure(command=lambda:[StartGame(), Load()])
LoadButton_StartFrame.pack()


#window_iconimage = ImageTk.PhotoImage(file="Assets\Cookie.png")
#window.iconphoto(window_iconimage, "Assets\Cookie.png") 

window.mainloop()