import tkinter as tk

# Predefined NZ Road Accident Data (Example)
accident_data = {
    "North Island": {
        "Minor": {"Urban Roads": "📊 200 incidents/year", "Highways": "📊 150 incidents/year", "Rural Roads": "📊 80 incidents/year"},
        "Moderate": {"Urban Roads": "📊 120 incidents/year", "Highways": "📊 90 incidents/year", "Rural Roads": "📊 50 incidents/year"},
        "Major": {"Urban Roads": "📊 30 incidents/year", "Highways": "📊 20 incidents/year", "Rural Roads": "📊 10 incidents/year"}
    },
    "South Island": {
        "Minor": {"Urban Roads": "📊 100 incidents/year", "Highways": "📊 80 incidents/year", "Rural Roads": "📊 50 incidents/year"},
        "Moderate": {"Urban Roads": "📊 80 incidents/year", "Highways": "📊 70 incidents/year", "Rural Roads": "📊 40 incidents/year"},
        "Major": {"Urban Roads": "📊 20 incidents/year", "Highways": "📊 15 incidents/year", "Rural Roads": "📊 8 incidents/year"}
    }
}

# Function to Display Road Accident Data
def show_accident_data():
    region = region_var.get()
    severity = severity_var.get()
    road_type = road_type_var.get()

    if region in accident_data and severity in accident_data[region] and road_type in accident_data[region][severity]:
        stats = accident_data[region][severity][road_type]
        result_label.config(text=f"{severity} accidents on {road_type} in {region}:\n{stats}")
    else:
        result_label.config(text="No matching accident data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Road Accident Analyzer")
root.geometry("400x300")

# Dropdown for Region Selection
tk.Label(root, text="Select region:").pack(pady=5)
region_var = tk.StringVar(root)
region_var.set("North Island")
region_menu = tk.OptionMenu(root, region_var, *accident_data.keys())
region_menu.pack(pady=5)

# Dropdown for Severity
tk.Label(root, text="Select severity level:").pack(pady=5)
severity_var = tk.StringVar(root)
severity_var.set("Minor")
severity_menu = tk.OptionMenu(root, severity_var, "Minor", "Moderate", "Major")
severity_menu.pack(pady=5)

# Dropdown for Road Type
tk.Label(root, text="Select road type:").pack(pady=5)
road_type_var = tk.StringVar(root)
road_type_var.set("Urban Roads")
road_type_menu = tk.OptionMenu(root, road_type_var, "Urban Roads", "Highways", "Rural Roads")
road_type_menu.pack(pady=5)

# Button to Display Accident Data
tk.Button(root, text="Show Accident Stats", command=show_accident_data).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()