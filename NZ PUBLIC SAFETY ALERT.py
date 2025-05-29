import tkinter as tk

# Predefined NZ Public Safety Alert Data (Example)
alert_data = {
    "Weather": {
        "Low": {"North Island": "Light rain expected in Auckland", "South Island": "Mild winds near Christchurch", "All NZ": "No major weather concerns"},
        "Medium": {"North Island": "Heavy rain warning for Wellington", "South Island": "Strong winds near Dunedin", "All NZ": "Moderate weather risks"},
        "High": {"North Island": "Cyclone alert for Bay of Plenty", "South Island": "Snowstorm warning for Queenstown", "All NZ": "Severe weather conditions"}
    },
    "Crime": {
        "Low": {"North Island": "Minor theft reported in Hamilton", "South Island": "Small-scale fraud cases in Nelson", "All NZ": "General safety advisory"},
        "Medium": {"North Island": "Burglary spike in Auckland suburbs", "South Island": "Increased vehicle thefts in Christchurch", "All NZ": "Stay alert in public areas"},
        "High": {"North Island": "Armed robbery reported in Wellington", "South Island": "Major crime incident in Invercargill", "All NZ": "Emergency law enforcement advisory"}
    }
}

# Function to Display Public Safety Alerts
def show_alert():
    alert_type = alert_var.get()
    severity = severity_var.get()
    region = region_var.get()

    if alert_type in alert_data and severity in alert_data[alert_type] and region in alert_data[alert_type][severity]:
        alert_info = alert_data[alert_type][severity][region]
        result_label.config(text=f"{severity} alert for {alert_type} in {region}:\n{alert_info}")
    else:
        result_label.config(text="No matching alert data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Public Safety Alert System")
root.geometry("400x300")

# Dropdown for Alert Type Selection
tk.Label(root, text="Select alert type:").pack(pady=5)
alert_var = tk.StringVar(root)
alert_var.set("Weather")
alert_menu = tk.OptionMenu(root, alert_var, *alert_data.keys())
alert_menu.pack(pady=5)

# Dropdown for Severity Level
tk.Label(root, text="Select severity level:").pack(pady=5)
severity_var = tk.StringVar(root)
severity_var.set("Low")
severity_menu = tk.OptionMenu(root, severity_var, "Low", "Medium", "High")
severity_menu.pack(pady=5)

# Dropdown for Affected Region
tk.Label(root, text="Select affected region:").pack(pady=5)
region_var = tk.StringVar(root)
region_var.set("North Island")
region_menu = tk.OptionMenu(root, region_var, "North Island", "South Island", "All NZ")
region_menu.pack(pady=5)

# Button to Display Alerts
tk.Button(root, text="Check Alerts", command=show_alert).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()