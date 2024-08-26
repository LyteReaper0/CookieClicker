from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk


window = Tk()
window.geometry("600x600")
window.title("CookieClicker")
window.config(bg="#dbdbdb")


CookieCount = 0
def AddCookieClickCount():
        global CookieCount
        CookieCount += 1
        print("+1 Cookie")
        CookieCountDisplay.config(text=str(CookieCount))
        return CookieCount 

def PrintCookieCount():
        print(CookieCount)

introduction = Label(window,text="Click me!!!")
introduction.config(font=("Ink Free",24,"bold"))
introduction.config(bg="#dbdbdb")
introduction.pack()

CookieCountDisplay = Label(window,text=CookieCount)
CookieCountDisplay.pack()


CookieButtonIcon = ImageTk.PhotoImage(file="Assets\Cookie.png")
CookieButton = Button(window,image=CookieButtonIcon)
CookieButton.config(command=lambda:[AddCookieClickCount(), PrintCookieCount()])
CookieButton.config(activebackground="#f98a02")
CookieButton.config(bg="#dbdbdb")
CookieButton.pack()


cookieicon = ImageTk.PhotoImage(file="Assets\Cookie.png")
window.iconphoto(True,cookieicon)

window.mainloop()