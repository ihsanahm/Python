from tkinter import*
import tkinter as tk
from geopy.geocoders import nominatim
from tkinter import ttk ,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root =Tk()
root.title("Weather App")
root.geometry("900x550+250+20")
root.resizable(False,False)

search_image=PhotoImage( file = "D:\Python repository\projectsofPthons\search.png")
myimge=Label(image=search_image)
myimge.place(x=20,y=20)


textfield=tk.Entry(root,justify="center",width=18,font=("poppins",26,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=48,y=37)

textfield.focus()

search_Icon=PhotoImage(file="D:\Python repository\projectsofPthons\search_icon.png")
myIcon=Button(image=search_Icon,borderwidth=0,cursor="hand2",bg="#404040")
myIcon.place(x=400,y=31.5)

Logo_image=PhotoImage( file = "D:\Python repository\projectsofPthons\logo.png")
myLogo=Label(image=Logo_image)
myLogo.place(x=180,y=130)

Button_image = PhotoImage(file="D:\\Python repository\\projectsofPthons\\NewBox.png")

myButton=Label(image=Button_image)
myButton.pack(padx=5,pady=5,side=BOTTOM)


root.mainloop()


