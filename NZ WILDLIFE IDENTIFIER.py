import tkinter as tk

# Predefined NZ Wildlife Data (Example)
wildlife_data = {
    "Forest": {
        "Birds": {"Image Recognition": "Kākā - Native parrot", "Sound Analysis": "Tūī - Distinctive song", "Text Search": "Kererū - Wood pigeon"},
        "Mammals": {"Image Recognition": "Short-tailed Bat - NZ native", "Sound Analysis": "Possum - Common nocturnal mammal", "Text Search": "Stoat - Introduced predator"},
        "Reptiles": {"Image Recognition": "Tuatara - Ancient reptile", "Sound Analysis": "Gecko - NZ native species", "Text Search": "Skink - Found in bush areas"}
    },
    "Coastal": {
        "Birds": {"Image Recognition": "Pied Shag - Coastal bird", "Sound Analysis": "Little Blue Penguin - Nocturnal calls", "Text Search": "Red-billed Gull - Common seabird"},
        "Mammals": {"Image Recognition": "NZ Fur Seal - Marine mammal", "Sound Analysis": "Dolphins - Found near Bay of Islands", "Text Search": "Whales - Seasonal migration"},
        "Reptiles": {"Image Recognition": "Sea Turtle - Occasionally spotted", "Sound Analysis": "Marine Iguana - Rare sightings", "Text Search": "Coastal Skink - Found near beaches"}
    }
}

# Function to Display Wildlife Info
def show_wildlife_info():
    habitat = habitat_var.get()
    species = species_var.get()
    method = method_var.get()

    if habitat in wildlife_data and species in wildlife_data[habitat] and method in wildlife_data[habitat][species]:
        wildlife_info = wildlife_data[habitat][species][method]
        result_label.config(text=f"{species} identification in {habitat} ({method}):\n{wildlife_info}")
    else:
        result_label.config(text="No matching wildlife data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Wildlife Identifier")
root.geometry("400x300")

# Dropdown for Habitat Selection
tk.Label(root, text="Select habitat type:").pack(pady=5)
habitat_var = tk.StringVar(root)
habitat_var.set("Forest")
habitat_menu = tk.OptionMenu(root, habitat_var, *wildlife_data.keys())
habitat_menu.pack(pady=5)

# Dropdown for Species Category
tk.Label(root, text="Select species category:").pack(pady=5)
species_var = tk.StringVar(root)
species_var.set("Birds")
species_menu = tk.OptionMenu(root, species_var, "Birds", "Mammals", "Reptiles")
species_menu.pack(pady=5)

# Dropdown for Identification Method
tk.Label(root, text="Select identification method:").pack(pady=5)
method_var = tk.StringVar(root)
method_var.set("Image Recognition")
method_menu = tk.OptionMenu(root, method_var, "Image Recognition", "Sound Analysis", "Text Search")
method_menu.pack(pady=5)

# Button to Identify Wildlife
tk.Button(root, text="Identify Wildlife", command=show_wildlife_info).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()