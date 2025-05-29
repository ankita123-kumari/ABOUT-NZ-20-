import tkinter as tk

# Predefined NZ Road Trip Data
road_trip_data = {
    "North Island": {
        "Short": {"Scenic": "Auckland → Matamata → Hobbiton", "Adventure": "Taupo → Rotorua → Waitomo Caves", "Relaxation": "Coromandel → Hot Water Beach"},
        "Medium": {"Scenic": "Wellington → Napier → Taupo", "Adventure": "Bay of Plenty → Gisborne → Raglan", "Relaxation": "Northland → Bay of Islands"},
        "Long": {"Scenic": "Auckland → Wellington via East Coast", "Adventure": "Tongariro National Park → Taranaki → Wellington", "Relaxation": "Coastal Drive from Auckland → Cape Reinga"}
    },
    "South Island": {
        "Short": {"Scenic": "Christchurch → Arthur's Pass", "Adventure": "Queenstown → Wanaka → Mt Cook", "Relaxation": "Kaikoura → Hanmer Springs"},
        "Medium": {"Scenic": "West Coast Drive (Greymouth → Franz Josef → Milford Sound)", "Adventure": "Southern Alps → Fiordland", "Relaxation": "Nelson → Abel Tasman National Park"},
        "Long": {"Scenic": "Christchurch → Dunedin → Invercargill", "Adventure": "South Island Grand Tour (Christchurch → Queenstown → Fiordland)", "Relaxation": "Marlborough → Wine Country Tour"}
    }
}

# Function to Display Road Trip Info
def show_road_trip():
    region = region_var.get()
    duration = duration_var.get()
    travel_type = travel_type_var.get()

    if region in road_trip_data and duration in road_trip_data[region] and travel_type in road_trip_data[region][duration]:
        trip = road_trip_data[region][duration][travel_type]
        result_label.config(text=f"Recommended Route:\n{trip}")
    else:
        result_label.config(text="No matching road trip found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Road Trip Planner")
root.geometry("400x300")

# Dropdown for Region Selection
tk.Label(root, text="Select a region:").pack(pady=5)
region_var = tk.StringVar(root)
region_var.set("North Island")
region_menu = tk.OptionMenu(root, region_var, *road_trip_data.keys())
region_menu.pack(pady=5)

# Dropdown for Duration
tk.Label(root, text="Select trip duration:").pack(pady=5)
duration_var = tk.StringVar(root)
duration_var.set("Short")
duration_menu = tk.OptionMenu(root, duration_var, "Short", "Medium", "Long")
duration_menu.pack(pady=5)

# Dropdown for Travel Type
tk.Label(root, text="Select travel type:").pack(pady=5)
travel_type_var = tk.StringVar(root)
travel_type_var.set("Scenic")
travel_menu = tk.OptionMenu(root, travel_type_var, "Scenic", "Adventure", "Relaxation")
travel_menu.pack(pady=5)

# Button to Get Route
tk.Button(root, text="Find Route", command=show_road_trip).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()