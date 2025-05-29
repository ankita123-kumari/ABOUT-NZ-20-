import tkinter as tk

# Predefined NZ Surf Data
surf_data = {
    "North Island": {
        "Beginner-friendly": {"Small": "Piha Beach - 0.5m waves", "Medium": "Mount Maunganui - 1.5m waves", "Large": "Muriwai Beach - 2.5m waves"},
        "Advanced": {"Small": "Raglan - 1m waves", "Medium": "Taranaki - 2m waves", "Large": "Shipwreck Bay - 3m waves"}
    },
    "South Island": {
        "Beginner-friendly": {"Small": "Sumner Beach - 0.3m waves", "Medium": "Christchurch - 1.2m waves", "Large": "Kaikoura - 2m waves"},
        "Advanced": {"Small": "Westport - 1m waves", "Medium": "Fiordland - 2m waves", "Large": "Southland - 3.5m waves"}
    }
}

# Function to Display Surf Info
def show_surf_report():
    region = region_var.get()
    beach_type = beach_type_var.get()
    wave_size = wave_size_var.get()

    if region in surf_data and beach_type in surf_data[region] and wave_size in surf_data[region][beach_type]:
        surf_report = surf_data[region][beach_type][wave_size]
        result_label.config(text=f"Recommended Surf Spot:\n{surf_report}")
    else:
        result_label.config(text="No matching surf report found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Surf Report")
root.geometry("400x300")

# Dropdown for Region Selection
tk.Label(root, text="Select a region:").pack(pady=5)
region_var = tk.StringVar(root)
region_var.set("North Island")
region_menu = tk.OptionMenu(root, region_var, *surf_data.keys())
region_menu.pack(pady=5)

# Dropdown for Beach Type
tk.Label(root, text="Select beach type:").pack(pady=5)
beach_type_var = tk.StringVar(root)
beach_type_var.set("Beginner-friendly")
beach_type_menu = tk.OptionMenu(root, beach_type_var, "Beginner-friendly", "Advanced")
beach_type_menu.pack(pady=5)

# Dropdown for Wave Size
tk.Label(root, text="Select wave height:").pack(pady=5)
wave_size_var = tk.StringVar(root)
wave_size_var.set("Small")
wave_size_menu = tk.OptionMenu(root, wave_size_var, "Small", "Medium", "Large")
wave_size_menu.pack(pady=5)

# Button to Get Surf Report
tk.Button(root, text="Get Surf Report", command=show_surf_report).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()