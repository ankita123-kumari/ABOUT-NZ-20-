import tkinter as tk

# Predefined NZ Event Data
event_data = {
    "Auckland": {
        "Concert": ["Coldplay - Eden Park (June 15)", "Taylor Swift - Mt Smart Stadium (Nov 20)"],
        "Sports": ["All Blacks vs Australia - Eden Park (July 5)", "NZ Warriors vs Storm - Mt Smart (Aug 10)"],
        "Festival": ["Auckland Lantern Festival (Feb 25)", "Diwali Festival (Oct 14)"],
    },
    "Wellington": {
        "Concert": ["Ed Sheeran - Sky Stadium (May 10)", "Six60 - TSB Arena (Aug 30)"],
        "Sports": ["Phoenix vs Sydney FC - Sky Stadium (Sept 18)", "Super Rugby Final - Sky Stadium (June 8)"],
        "Festival": ["NZ Fringe Festival (Mar 12)", "Wellington Jazz Festival (Sept 3)"],
    },
    "Christchurch": {
        "Concert": ["Pink - Orangetheory Stadium (Dec 5)", "Imagine Dragons - Christchurch Arena (Oct 7)"],
        "Sports": ["Crusaders vs Blues - Orangetheory (May 28)", "NZ Cricket T20 - Hagley Oval (Nov 22)"],
        "Festival": ["Christchurch Food Festival (July 9)", "South Island Wine & Cheese Fest (Dec 1)"],
    }
}

# Function to Display Events
def show_events():
    city = city_var.get()
    event_type = event_var.get()

    if city in event_data and event_type in event_data[city]:
        events = "\n".join(event_data[city][event_type])
        result_label.config(text=f"{event_type} events in {city}:\n{events}")
    else:
        result_label.config(text="No event data available for this selection.")

# GUI Setup
root = tk.Tk()
root.title("NZ Event Finder")
root.geometry("400x300")

# Dropdown for City Selection
tk.Label(root, text="Select a city:").pack(pady=5)
city_var = tk.StringVar(root)
city_var.set("Auckland")
city_menu = tk.OptionMenu(root, city_var, *event_data.keys())
city_menu.pack(pady=5)

# Dropdown for Event Type
tk.Label(root, text="Select event type:").pack(pady=5)
event_var = tk.StringVar(root)
event_var.set("Concert")
event_menu = tk.OptionMenu(root, event_var, "Concert", "Sports", "Festival")
event_menu.pack(pady=5)

# Button to Get Events
tk.Button(root, text="Show Events", command=show_events).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()