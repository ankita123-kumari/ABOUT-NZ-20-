import tkinter as tk

# Predefined Public Transport Data
transport_data = {
    "Auckland": {
        "Bus": ["Route 18 - City to New Lynn", "Route 70 - Britomart to Botany"],
        "Train": ["Western Line - Swanson to Britomart", "Southern Line - Papakura to Britomart"],
    },
    "Wellington": {
        "Bus": ["Route 1 - Johnsonville to Island Bay", "Route 7 - Brooklyn to City"],
        "Train": ["Kapiti Line - Waikanae to Wellington", "Hutt Valley Line - Upper Hutt to Wellington"],
    },
    "Christchurch": {
        "Bus": ["Route 3 - Airport to Sumner", "Route 60 - Riccarton to Ferrymead"],
        "Train": ["Coastal Pacific - Christchurch to Picton"],
    }
}

# Function to Display Transport Info
def show_transport():
    city = city_var.get()
    transport_type = transport_var.get()

    if city in transport_data and transport_type in transport_data[city]:
        routes = "\n".join(transport_data[city][transport_type])
        result_label.config(text=f"{transport_type} routes in {city}:\n{routes}")
    else:
        result_label.config(text="No transport data available for this selection.")

# GUI Setup
root = tk.Tk()
root.title("NZ Public Transport Tracker")
root.geometry("400x300")

# Dropdown for City Selection
tk.Label(root, text="Select a city:").pack(pady=5)
city_var = tk.StringVar(root)
city_var.set("Auckland")
city_menu = tk.OptionMenu(root, city_var, *transport_data.keys())
city_menu.pack(pady=5)

# Dropdown for Transport Type
tk.Label(root, text="Select transport type:").pack(pady=5)
transport_var = tk.StringVar(root)
transport_var.set("Bus")
transport_menu = tk.OptionMenu(root, transport_var, "Bus", "Train")
transport_menu.pack(pady=5)

# Button to Get Routes
tk.Button(root, text="Show Routes", command=show_transport).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()