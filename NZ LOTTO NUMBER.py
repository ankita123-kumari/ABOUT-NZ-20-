import tkinter as tk

# Predefined NZ Lotto Data (Example)
lotto_data = {
    "Powerball": [3, 7, 15, 20, 25, 33, 40, 45, 2, 14, 27],
    "Keno": [1, 5, 12, 18, 22, 30, 35, 41, 49, 55],
    "Bullseye": [6, 11, 19, 24, 31, 37, 42, 48, 53, 59]
}

# Function to Filter Numbers
def filter_numbers():
    game = game_var.get()
    filter_type = filter_var.get()

    if game in lotto_data:
        numbers = lotto_data[game]
        if filter_type == "Low (1-20)":
            filtered_numbers = [num for num in numbers if num <= 20]
        elif filter_type == "Medium (21-40)":
            filtered_numbers = [num for num in numbers if 21 <= num <= 40]
        elif filter_type == "High (41-60)":
            filtered_numbers = [num for num in numbers if num >= 41]
        else:
            filtered_numbers = numbers
        
        result_label.config(text=f"{game} Numbers ({filter_type}):\n{', '.join(map(str, filtered_numbers))}")
    else:
        result_label.config(text="No data available for this selection.")

# GUI Setup
root = tk.Tk()
root.title("NZ Lotto Number Analyzer")
root.geometry("400x300")

# Dropdown for Lotto Selection
tk.Label(root, text="Select a Lotto game:").pack(pady=5)
game_var = tk.StringVar(root)
game_var.set("Powerball")
game_menu = tk.OptionMenu(root, game_var, *lotto_data.keys())
game_menu.pack(pady=5)

# Dropdown for Filter Type
tk.Label(root, text="Filter by number range:").pack(pady=5)
filter_var = tk.StringVar(root)
filter_var.set("All")
filter_menu = tk.OptionMenu(root, filter_var, "All", "Low (1-20)", "Medium (21-40)", "High (41-60)")
filter_menu.pack(pady=5)

# Button to Get Numbers
tk.Button(root, text="Analyze Numbers", command=filter_numbers).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()