import tkinter as tk

# Predefined NZ Housing Price Data (Example)
housing_data = {
    "Auckland": {
        "Apartment": {"Stable": "$750,000", "Rising": "$800,000", "Declining": "$700,000"},
        "House": {"Stable": "$1,200,000", "Rising": "$1,300,000", "Declining": "$1,100,000"},
        "Townhouse": {"Stable": "$900,000", "Rising": "$950,000", "Declining": "$850,000"}
    },
    "Wellington": {
        "Apartment": {"Stable": "$600,000", "Rising": "$650,000", "Declining": "$550,000"},
        "House": {"Stable": "$950,000", "Rising": "$1,000,000", "Declining": "$900,000"},
        "Townhouse": {"Stable": "$750,000", "Rising": "$800,000", "Declining": "$700,000"}
    },
    "Christchurch": {
        "Apartment": {"Stable": "$500,000", "Rising": "$550,000", "Declining": "$450,000"},
        "House": {"Stable": "$800,000", "Rising": "$850,000", "Declining": "$750,000"},
        "Townhouse": {"Stable": "$650,000", "Rising": "$700,000", "Declining": "$600,000"}
    }
}

# Function to Display Housing Price Predictions
def show_housing_price():
    location = location_var.get()
    property_type = property_var.get()
    trend = trend_var.get()

    if location in housing_data and property_type in housing_data[location] and trend in housing_data[location][property_type]:
        price_info = housing_data[location][property_type][trend]
        result_label.config(text=f"Estimated price for {property_type} in {location} ({trend} market):\n{price_info}")
    else:
        result_label.config(text="No matching housing price data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Housing Price Predictor")
root.geometry("400x300")

# Dropdown for Location Selection
tk.Label(root, text="Select location:").pack(pady=5)
location_var = tk.StringVar(root)
location_var.set("Auckland")
location_menu = tk.OptionMenu(root, location_var, *housing_data.keys())
location_menu.pack(pady=5)

# Dropdown for Property Type
tk.Label(root, text="Select property type:").pack(pady=5)
property_var = tk.StringVar(root)
property_var.set("Apartment")
property_menu = tk.OptionMenu(root, property_var, "Apartment", "House", "Townhouse")
property_menu.pack(pady=5)

# Dropdown for Market Trend
tk.Label(root, text="Select market trend:").pack(pady=5)
trend_var = tk.StringVar(root)
trend_var.set("Stable")
trend_menu = tk.OptionMenu(root, trend_var, "Stable", "Rising", "Declining")
trend_menu.pack(pady=5)

# Button to Predict Housing Price
tk.Button(root, text="Predict Price", command=show_housing_price).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()