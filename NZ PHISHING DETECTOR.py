import tkinter as tk

# Predefined Phishing Risk Data (Example Ratings)
phishing_data = {
    "Banking": {
        "Low": {"Basic Check": "Safe - Verified banking site", "Deep Scan": "SSL secured, no red flags", "AI Detection": "No phishing indicators detected"},
        "Medium": {"Basic Check": "Suspicious - Not well known", "Deep Scan": "No SSL, possible risk", "AI Detection": "Potential phishing link"},
        "High": {"Basic Check": "Dangerous - Unverified site", "Deep Scan": "Fake URL structure found", "AI Detection": "High phishing probability"}
    },
    "Shopping": {
        "Low": {"Basic Check": "Safe - Trusted store", "Deep Scan": "Secure payment gateway detected", "AI Detection": "No risk identified"},
        "Medium": {"Basic Check": "Suspicious - Unknown seller", "Deep Scan": "No HTTPS encryption", "AI Detection": "Possible scam"},
        "High": {"Basic Check": "Dangerous - Fraud risk", "Deep Scan": "Multiple user complaints", "AI Detection": "Likely scam website"}
    }
}

# Function to Detect Phishing Risk
def detect_phishing():
    website_type = website_var.get()
    security_level = security_var.get()
    method = method_var.get()

    if website_type in phishing_data and security_level in phishing_data[website_type] and method in phishing_data[website_type][security_level]:
        risk_result = phishing_data[website_type][security_level][method]
        result_label.config(text=f"{security_level} risk for {website_type} ({method} analysis):\n{risk_result}")
    else:
        result_label.config(text="No matching phishing data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Phishing Detector")
root.geometry("400x300")

# Dropdown for Website Type Selection
tk.Label(root, text="Select website type:").pack(pady=5)
website_var = tk.StringVar(root)
website_var.set("Banking")
website_menu = tk.OptionMenu(root, website_var, *phishing_data.keys())
website_menu.pack(pady=5)

# Dropdown for Security Level
tk.Label(root, text="Select security rating:").pack(pady=5)
security_var = tk.StringVar(root)
security_var.set("Low")
security_menu = tk.OptionMenu(root, security_var, "Low", "Medium", "High")
security_menu.pack(pady=5)

# Dropdown for Analysis Method
tk.Label(root, text="Select risk analysis method:").pack(pady=5)
method_var = tk.StringVar(root)
method_var.set("Basic Check")
method_menu = tk.OptionMenu(root, method_var, "Basic Check", "Deep Scan", "AI Detection")
method_menu.pack(pady=5)

# Button to Detect Phishing
tk.Button(root, text="Check Website", command=detect_phishing).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()