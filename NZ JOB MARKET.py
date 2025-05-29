import tkinter as tk

# Predefined NZ Job Market Data (Example)
job_data = {
    "IT": {
        "Entry Level": {"Full-Time": "Junior Developer - $60K", "Part-Time": "IT Support - $30K", "Remote": "Data Analyst - $50K"},
        "Mid-Level": {"Full-Time": "Software Engineer - $90K", "Part-Time": "UI/UX Designer - $60K", "Remote": "Cloud Engineer - $85K"},
        "Senior Level": {"Full-Time": "AI Specialist - $130K", "Part-Time": "Cybersecurity Lead - $110K", "Remote": "Tech Consultant - $120K"},
    },
    "Healthcare": {
        "Entry Level": {"Full-Time": "Nurse Assistant - $55K", "Part-Time": "Medical Receptionist - $35K", "Remote": "Telehealth Advisor - $45K"},
        "Mid-Level": {"Full-Time": "Registered Nurse - $80K", "Part-Time": "Physiotherapist - $75K", "Remote": "Healthcare Data Analyst - $70K"},
        "Senior Level": {"Full-Time": "Specialist Doctor - $150K", "Part-Time": "Hospital Director - $135K", "Remote": "Senior Health Consultant - $140K"},
    },
    "Engineering": {
        "Entry Level": {"Full-Time": "Civil Engineer Graduate - $65K", "Part-Time": "CAD Technician - $45K", "Remote": "Structural Analyst - $55K"},
        "Mid-Level": {"Full-Time": "Mechanical Engineer - $95K", "Part-Time": "Electrical Engineer - $85K", "Remote": "Project Engineer - $90K"},
        "Senior Level": {"Full-Time": "Senior Project Manager - $140K", "Part-Time": "Lead Consultant - $120K", "Remote": "Innovation Engineer - $125K"},
    }
}

# Function to Display Job Market Data
def show_jobs():
    industry = industry_var.get()
    level = level_var.get()
    job_type = job_type_var.get()

    if industry in job_data and level in job_data[industry] and job_type in job_data[industry][level]:
        job_info = job_data[industry][level][job_type]
        result_label.config(text=f"{level} jobs in {industry} ({job_type}):\n{job_info}")
    else:
        result_label.config(text="No matching job data found.")

# GUI Setup
root = tk.Tk()
root.title("NZ Job Market Analyzer")
root.geometry("400x300")

# Dropdown for Industry Selection
tk.Label(root, text="Select an industry:").pack(pady=5)
industry_var = tk.StringVar(root)
industry_var.set("IT")
industry_menu = tk.OptionMenu(root, industry_var, *job_data.keys())
industry_menu.pack(pady=5)

# Dropdown for Experience Level
tk.Label(root, text="Select salary level:").pack(pady=5)
level_var = tk.StringVar(root)
level_var.set("Entry Level")
level_menu = tk.OptionMenu(root, level_var, "Entry Level", "Mid-Level", "Senior Level")
level_menu.pack(pady=5)

# Dropdown for Job Type
tk.Label(root, text="Select job type:").pack(pady=5)
job_type_var = tk.StringVar(root)
job_type_var.set("Full-Time")
job_type_menu = tk.OptionMenu(root, job_type_var, "Full-Time", "Part-Time", "Remote")
job_type_menu.pack(pady=5)

# Button to Analyze Jobs
tk.Button(root, text="Find Jobs", command=show_jobs).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()