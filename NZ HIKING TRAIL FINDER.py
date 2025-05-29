import tkinter as tk

# Predefined NZ Hiking Trails
hiking_data = {
    "North Island": {
        "Easy": ["Cathedral Cove Walk - 2km", "Te Mata Peak Walk - 1.5km", "Waitakere Ranges - 3km"],
        "Medium": ["Tongariro Alpine Crossing - 19.4km", "Mount Taranaki Summit Track - 16km", "Cape Reinga Coastal Walk - 12km"],
        "Hard": ["Pinnacles Track - 26km", "Lake Waikaremoana Great Walk - 46km", "Northern Circuit - 50km"]
    },
    "South Island": {
        "Easy": ["Hooker Valley Track - 5km", "Kaikoura Peninsula Walk - 4km", "Queenstown Hill Track - 3.5km"],
        "Medium": ["Routeburn Track - 32km", "Abel Tasman Coast Track - 60km", "Kepler Track - 60km"],
        "Hard": ["Milford Track - 53km", "Rakiura Track - 38km", "Paparoa Track - 55km"]
    }
}

# Function to Display Hiking Trails
def show_hiking_trail():
    region = region_var.get()
    difficulty = difficulty_var.get()

    if region in hiking_data and difficulty in hiking_data[region]:
        trails = "\n".join(hiking_data[region][difficulty])
        result_label.config(text=f"{difficulty} trails in {region}:\n{trails}")
    else:
        result_label.config(text="No matching hiking trail found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Hiking Trail Finder")
root.geometry("400x300")

# Dropdown for Region Selection
tk.Label(root, text="Select a region:").pack(pady=5)
region_var = tk.StringVar(root)
region_var.set("North Island")
region_menu = tk.OptionMenu(root, region_var, *hiking_data.keys())
region_menu.pack(pady=5)

# Dropdown for Difficulty Level
tk.Label(root, text="Select difficulty level:").pack(pady=5)
difficulty_var = tk.StringVar(root)
difficulty_var.set("Easy")
difficulty_menu = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard")
difficulty_menu.pack(pady=5)

# Button to Get Hiking Trails
tk.Button(root, text="Find Trails", command=show_hiking_trail).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()