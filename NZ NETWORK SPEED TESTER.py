import tkinter as tk
import random

# Predefined Network Speed Data (Example)
speed_data = {
    "WiFi": {"Basic": "Download: 40 Mbps, Upload: 10 Mbps", "Standard": "Download: 50 Mbps, Upload: 15 Mbps", "High Precision": "Download: 55 Mbps, Upload: 20 Mbps"},
    "Ethernet": {"Basic": "Download: 80 Mbps, Upload: 30 Mbps", "Standard": "Download: 90 Mbps, Upload: 40 Mbps", "High Precision": "Download: 95 Mbps, Upload: 45 Mbps"},
    "Mobile Data": {"Basic": "Download: 15 Mbps, Upload: 5 Mbps", "Standard": "Download: 20 Mbps, Upload: 7 Mbps", "High Precision": "Download: 25 Mbps, Upload: 10 Mbps"}
}

# Function to Simulate Speed Test
def run_speed_test():
    connection = connection_var.get()
    accuracy = accuracy_var.get()
    
    if connection in speed_data and accuracy in speed_data[connection]:
        speed_result = speed_data[connection][accuracy]
        result_label.config(text=f"{connection} Speed Test ({accuracy} Accuracy):\n{speed_result}")
    else:
        result_label.config(text="No matching speed test data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Network Speed Tester")
root.geometry("400x300")

# Dropdown for Connection Type Selection
tk.Label(root, text="Select connection type:").pack(pady=5)
connection_var = tk.StringVar(root)
connection_var.set("WiFi")
connection_menu = tk.OptionMenu(root, connection_var, *speed_data.keys())
connection_menu.pack(pady=5)

# Dropdown for Test Accuracy
tk.Label(root, text="Select test accuracy:").pack(pady=5)
accuracy_var = tk.StringVar(root)
accuracy_var.set("Basic")
accuracy_menu = tk.OptionMenu(root, accuracy_var, "Basic", "Standard", "High Precision")
accuracy_menu.pack(pady=5)

# Button to Run Speed Test
tk.Button(root, text="Run Speed Test", command=run_speed_test).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()