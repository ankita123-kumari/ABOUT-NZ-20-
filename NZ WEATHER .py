import tkinter as tk

# NZ Weather Data
weather_data = {
    "Auckland": {"temperature": 20, "condition": "Partly Cloudy"},
    "Wellington": {"temperature": 18, "condition": "Windy"},
    "Christchurch": {"temperature": 15, "condition": "Sunny"},
    "Dunedin": {"temperature": 12, "condition": "Rainy"},
}

# Function to Display Filtered Weather
def show_weather():
    city = city_var.get()
    condition = condition_var.get()

    if city in weather_data and (condition == "All" or weather_data[city]["condition"] == condition):
        result_label.config(text=f"Weather in {city}\nTemperature: {weather_data[city]['temperature']}°C\nCondition: {weather_data[city]['condition']}")
    else:
        result_label.config(text="Sorry, no matching weather data available.")

# GUI Setup
root = tk.Tk()
root.title("NZ Weather App")
root.geometry("350x250")

# Dropdown for City Selection
tk.Label(root, text="Select a NZ city:").pack(pady=5)
city_var = tk.StringVar(root)
city_var.set("Auckland")  # Default selection
city_menu = tk.OptionMenu(root, city_var, *weather_data.keys())
city_menu.pack(pady=5)

# Dropdown for Weather Type
tk.Label(root, text="Filter by Weather Type:").pack(pady=5)
condition_var = tk.StringVar(root)
condition_var.set("All")  # Default selection
condition_menu = tk.OptionMenu(root, condition_var, "All", "Sunny", "Rainy", "Windy", "Partly Cloudy")
condition_menu.pack(pady=5)

# Button to Get Weather
tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the App
root.mainloop()