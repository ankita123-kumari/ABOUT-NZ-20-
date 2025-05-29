import tkinter as tk

# Predefined NZ Digital Accessibility Data (Example)
accessibility_data = {
    "Government": {
        "WCAG 2.0": {"Basic": "Meets basic text contrast requirements", "Standard": "Includes alt text for images", "Advanced": "Fully compliant with screen readers"},
        "WCAG 2.1": {"Basic": "Keyboard navigation supported", "Standard": "ARIA labels implemented", "Advanced": "Enhanced accessibility for all users"},
        "NZ Web Standards": {"Basic": "Follows NZ accessibility guidelines", "Standard": "Optimized for mobile users", "Advanced": "Full compliance with NZ digital laws"}
    },
    "E-commerce": {
        "WCAG 2.0": {"Basic": "Readable fonts and colors", "Standard": "Accessible checkout process", "Advanced": "Full support for assistive technologies"},
        "WCAG 2.1": {"Basic": "Keyboard shortcuts enabled", "Standard": "Improved navigation for users", "Advanced": "AI-powered accessibility enhancements"},
        "NZ Web Standards": {"Basic": "Meets NZ accessibility rules", "Standard": "Optimized for all devices", "Advanced": "Certified for full accessibility compliance"}
    }
}

# Function to Display Accessibility Evaluation
def show_accessibility():
    website_type = website_var.get()
    standard = standard_var.get()
    compliance = compliance_var.get()

    if website_type in accessibility_data and standard in accessibility_data[website_type] and compliance in accessibility_data[website_type][standard]:
        accessibility_info = accessibility_data[website_type][standard][compliance]
        result_label.config(text=f"{compliance} compliance for {website_type} ({standard} standard):\n{accessibility_info}")
    else:
        result_label.config(text="No matching accessibility data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Digital Accessibility Checker")
root.geometry("400x300")

# Dropdown for Website Type Selection
tk.Label(root, text="Select website type:").pack(pady=5)
website_var = tk.StringVar(root)
website_var.set("Government")
website_menu = tk.OptionMenu(root, website_var, *accessibility_data.keys())
website_menu.pack(pady=5)

# Dropdown for Accessibility Standard
tk.Label(root, text="Select accessibility standard:").pack(pady=5)
standard_var = tk.StringVar(root)
standard_var.set("WCAG 2.0")
standard_menu = tk.OptionMenu(root, standard_var, "WCAG 2.0", "WCAG 2.1", "NZ Web Standards")
standard_menu.pack(pady=5)

# Dropdown for Compliance Level
tk.Label(root, text="Select compliance level:").pack(pady=5)
compliance_var = tk.StringVar(root)
compliance_var.set("Basic")
compliance_menu = tk.OptionMenu(root, compliance_var, "Basic", "Standard", "Advanced")
compliance_menu.pack(pady=5)

# Button to Evaluate Accessibility
tk.Button(root, text="Check Accessibility", command=show_accessibility).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()