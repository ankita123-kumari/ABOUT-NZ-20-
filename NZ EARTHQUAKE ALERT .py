import tkinter as tk

# Predefined NZ Earthquake Data (Example)
quake_data = {
    "North Island": {
        "Minor": {"Approximate": "Low risk - Mostly minor tremors", "Exact": "Last tremor: 2.1 magnitude"},
        "Moderate": {"Approximate": "Medium risk - Some moderate shakes", "Exact": "Last tremor: 4.5 magnitude"},
        "Major": {"Approximate": "High risk - Possible large quakes", "Exact": "Last tremor: 6.8 magnitude"}
    },
    "South Island": {
        "Minor": {"Approximate": "Low risk - Some minor activity", "Exact": "Last tremor: 2.5 magnitude"},
        "Moderate": {"Approximate": "Medium risk - Moderate quakes occur", "Exact": "Last tremor: 4.8 magnitude"},
        "Major": {"Approximate": "High risk - Earthquake-prone area", "Exact": "Last tremor: 7.2 magnitude"}
    }
}

# Function to Display Earthquake Data
def show_quake_data():
    region = region_var.get()
    severity = severity_var.get()
    accuracy = accuracy_var.get()

    if region in quake_data and severity in quake_data[region] and accuracy in quake_data[region][severity]:
        quake_info = quake_data[region][severity][accuracy]
        result_label.config(text=f"{severity} earthquake risk in {region}:\n{quake_info}")
    else:
        result_label.config(text="No matching earthquake data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Earthquake Alert System")
root.geometry("400x300")

# Dropdown for Region Selection
tk.Label(root, text="Select a region:").pack(pady=5)
region_var = tk.StringVar(root)
region_var.set("North Island")
region_menu = tk.OptionMenu(root, region_var, *quake_data.keys())
region_menu.pack(pady=5)

# Dropdown for Severity
tk.Label(root, text="Select severity level:").pack(pady=5)
severity_var = tk.StringVar(root)
severity_var.set("Minor")
severity_menu = tk.OptionMenu(root, severity_var, "Minor", "Moderate", "Major")
severity_menu.pack(pady=5)

# Dropdown for Accuracy
tk.Label(root, text="Select data accuracy:").pack(pady=5)
accuracy_var = tk.StringVar(root)
accuracy_var.set("Approximate")
accuracy_menu = tk.OptionMenu(root, accuracy_var, "Approximate", "Exact")
accuracy_menu.pack(pady=5)

# Button to Get Earthquake Data
tk.Button(root, text="Check Earthquake Risk", command=show_quake_data).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()