from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x550+250+20")
root.resizable(False, False)

# Function to get weather
def getWeather():
    city = textfield.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name!")
        return
    try:
        # Initialize geolocator and find city coordinates
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        
        if not location:
            messagebox.showerror("Error", f"City '{city}' not found!")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(f"Timezone: {result}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Correcting image paths
search_image = PhotoImage(file=r"D:/Python repository/projectsofPthons/search.png")
myimge = Label(image=search_image)
myimge.place(x=20, y=20)

textfield = tk.Entry(
    root, justify="center", width=18, font=("poppins", 26, "bold"),
    bg="#404040", border=0, fg="white"
)
textfield.place(x=48, y=37)
textfield.focus()

search_Icon = PhotoImage(file=r"D:/Python repository/projectsofPthons/search_icon.png")
myIcon = Button(
    image=search_Icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather
)
myIcon.place(x=400, y=31.5)

Logo_image = PhotoImage(file=r"D:/Python repository/projectsofPthons/logo.png")
myLogo = Label(image=Logo_image)
myLogo.place(x=180, y=130)

Button_image = PhotoImage(file=r"D:/Python repository/projectsofPthons/NewBox.png")
myButton = Label(image=Button_image)
myButton.pack(padx=5, pady=5, side=BOTTOM)

# Adding labels
Label(root, text="WIN", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white").place(x=120, y=460)
Label(root, text="HUMINTY", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white").place(x=250, y=460)
Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white").place(x=430, y=460)
Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white").place(x=650, y=460)

# Placeholder labels
t = Label(font=("arial", 70, "bold"), fg="#ee666d").place(x=430, y=150)
w = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef").place(x=130, y=490)
h = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef").place(x=280, y=490)
d = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef").place(x=480, y=490)
p = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef").place(x=690, y=490)

root.mainloop()
