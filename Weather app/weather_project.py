import requests
import tkinter as tk
from tkinter import messagebox

#logic
def search_location():
    city = search_location_E.get()
    api_key = 'a177176b2cc25ab21b1de779ecf9387f' 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        temperature_label.config(text=f"Temperature: {data['main']['temp']} °C")
        humidity_label.config(text=f"Humidity: {data['main']['humidity']} %")
        wind_Speed_label.config(text=f"Wind Speed: {data['wind']['speed']} m/s")
        pressure_label.config(text=f"Pressure: {data['main']['pressure']} hPa")
        
        if 'rain' in data:
            precipitation_label.config(text=f"Precipitation: {data['rain']['1h']} mm")
        else:
            precipitation_label.config(text="Precipitation: None")
    
    except:
         messagebox.showerror("Error", "Unable to search weather data. try again.")
            
            
 
window = tk.Tk()
window.title("Weather Forcast")
window.minsize(height=400, width=600)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)



#search box
frame = tk.Frame()
frame.grid(sticky= "n")
frame.grid(column=1, row=0, sticky="n")

search_location_L = tk.Label(frame, text="Location: ")
search_location_L.config(font=("Helvetica", 12, "bold"))

search_location_L.grid(column=0, row=0, padx=5, pady=5)
search_location_E= tk.Entry(frame)
search_location_E.grid(column=1, row=0, padx=5, pady=5)

#search button
frame_button = tk.Frame(frame, relief=tk.RAISED)
frame_button.grid(column=2, row=0, sticky="nw")
search_button = tk.Button(frame_button, text="Search", command=search_location)
search_button.grid(column=0, row=0, sticky="nw", padx=5, pady=5)

#information
frame_information = tk.Frame(window)
frame_information.grid(column= 0, row=1)

temperature_label = tk.Label(frame_information, text="Temperature: ")
temperature_label.grid(column=0, row=0, sticky="w", padx=20, pady=20)
temperature_label.config(font=("Helvetica", 12, "bold"))

humidity_label = tk.Label(frame_information, text="humidity: ")
humidity_label.grid(column=0, row=1, sticky="w", padx=20, pady=20)
humidity_label.config(font=("Helvetica", 12, "bold"))


wind_Speed_label = tk.Label(frame_information, text="wind Speed: ")
wind_Speed_label.grid(column=0, row=2, sticky="w", padx=20, pady=20)
wind_Speed_label.config(font=("Helvetica", 12, "bold"))


pressure_label = tk.Label(frame_information, text="pressure: ")
pressure_label.grid(column=0, row=3, sticky="w", padx=20, pady=20)
pressure_label.config(font=("Helvetica", 12, "bold"))


precipitation_label = tk.Label(frame_information, text="precipitation: ")
precipitation_label.grid(column=0, row=4, sticky="w", padx=20, pady=20)
precipitation_label.config(font=("Helvetica", 12, "bold"))




window.mainloop()




# api_key = "a177176b2cc25ab21b1de779ecf9387f"
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

