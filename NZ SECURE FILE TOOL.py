import tkinter as tk
import base64

# Simple File Encryption Data (Example Methods)
encryption_methods = {
    "AES": {"Low": "Basic AES encryption applied", "Medium": "256-bit AES encryption used", "High": "AES with multi-layer security"},
    "RSA": {"Low": "Basic RSA encryption applied", "Medium": "2048-bit RSA encryption used", "High": "RSA with advanced cryptography"},
    "Base64": {"Low": "Base64 encoding applied", "Medium": "Enhanced Base64 security used", "High": "Multi-step Base64 encoding"}
}

# Function to Encrypt Data
def encrypt_data():
    file_type = file_type_var.get()
    encryption_method = encryption_method_var.get()
    encryption_strength = encryption_strength_var.get()

    if encryption_method in encryption_methods and encryption_strength in encryption_methods[encryption_method]:
        encryption_status = encryption_methods[encryption_method][encryption_strength]
        result_label.config(text=f"{file_type} encryption status ({encryption_method} - {encryption_strength}):\n{encryption_status}")
    else:
        result_label.config(text="No matching encryption method found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Secure File Encryption Tool")
root.geometry("400x300")

# Dropdown for File Type Selection
tk.Label(root, text="Select file type:").pack(pady=5)
file_type_var = tk.StringVar(root)
file_type_var.set("Text File")
file_type_menu = tk.OptionMenu(root, file_type_var, "Text File", "PDF", "Image")
file_type_menu.pack(pady=5)

# Dropdown for Encryption Method
tk.Label(root, text="Select encryption method:").pack(pady=5)
encryption_method_var = tk.StringVar(root)
encryption_method_var.set("AES")
encryption_method_menu = tk.OptionMenu(root, encryption_method_var, "AES", "RSA", "Base64")
encryption_method_menu.pack(pady=5)

# Dropdown for Encryption Strength
tk.Label(root, text="Select encryption strength:").pack(pady=5)
encryption_strength_var = tk.StringVar(root)
encryption_strength_var.set("Low")
encryption_strength_menu = tk.OptionMenu(root, encryption_strength_var, "Low", "Medium", "High")
encryption_strength_menu.pack(pady=5)

# Button to Encrypt File
tk.Button(root, text="Encrypt File", command=encrypt_data).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()