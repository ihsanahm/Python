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
root.geometry("800x400+250+100")
root.resizable(False,False)

search_image=PhotoImage("search.png")
myimge=Label(image=search_image)
myimge.place(x=20,y=20)



root.mainloop()

