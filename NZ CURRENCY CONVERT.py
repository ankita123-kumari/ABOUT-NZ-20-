import tkinter as tk

# Predefined NZD Conversion Rates (Example)
currency_data = {
    "USD": {"Buy Rate": 0.62, "Sell Rate": 0.64},
    "EUR": {"Buy Rate": 0.58, "Sell Rate": 0.60},
    "GBP": {"Buy Rate": 0.50, "Sell Rate": 0.52},
    "AUD": {"Buy Rate": 0.92, "Sell Rate": 0.94}
}

# Function to Convert Currency
def convert_currency():
    currency = currency_var.get()
    conversion_type = conversion_var.get()
    accuracy = accuracy_var.get()
    
    if currency in currency_data and conversion_type in currency_data[currency]:
        rate = currency_data[currency][conversion_type]
        if accuracy == "Approximate":
            rate = round(rate, 1)
        result_label.config(text=f"1 NZD → {rate} {currency} ({conversion_type})")
    else:
        result_label.config(text="No matching currency data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Currency Converter")
root.geometry("400x300")

# Dropdown for Currency Selection
tk.Label(root, text="Select currency:").pack(pady=5)
currency_var = tk.StringVar(root)
currency_var.set("USD")
currency_menu = tk.OptionMenu(root, currency_var, *currency_data.keys())
currency_menu.pack(pady=5)

# Dropdown for Conversion Type
tk.Label(root, text="Select conversion type:").pack(pady=5)
conversion_var = tk.StringVar(root)
conversion_var.set("Buy Rate")
conversion_menu = tk.OptionMenu(root, conversion_var, "Buy Rate", "Sell Rate")
conversion_menu.pack(pady=5)

# Dropdown for Accuracy
tk.Label(root, text="Select conversion accuracy:").pack(pady=5)
accuracy_var = tk.StringVar(root)
accuracy_var.set("Approximate")
accuracy_menu = tk.OptionMenu(root, accuracy_var, "Approximate", "Exact")
accuracy_menu.pack(pady=5)

# Button to Convert
tk.Button(root, text="Convert Currency", command=convert_currency).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()