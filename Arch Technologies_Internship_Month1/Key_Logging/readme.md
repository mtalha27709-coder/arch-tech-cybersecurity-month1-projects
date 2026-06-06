# Key Logging Simulation (Safe Environment) using Python

---

## ???📌 Project Overview

This project demonstrates a safe and educational simulation of a key logging system using Python and Tkinter. The application captures user-provided input through a graphical interface and stores the data locally with timestamps.

The purpose of this project is to understand how keystroke logging works, explore its cybersecurity implications, and learn about the risks associated with unauthorized monitoring tools in a controlled environment.

---


## ???⚠️ Important:
 This project was developed strictly for educational and cybersecurity awareness purposes. It does not perform hidden monitoring, background tracking, or malicious activities.

---


## ???🎯 Objective
Understand the concept of keystroke logging
Learn how user input can be captured and recorded
Explore cybersecurity risks associated with keyloggers
Develop a safe educational simulation using Python
Improve Python GUI development skills
Raise awareness about privacy and security threats

---



## ???🛠️ Tools & Technologies Used
Python 3
Tkinter Library
VS Code
File Handling
Datetime Module

---



## ???⚙️ Features


User-friendly graphical interface
Text input collection
Timestamp recording
Local log file generation
Educational demonstration of key logging concepts
Safe and controlled implementation

---



## ???📂 Project Structure
Key-Logging-Simulation/
│
├── screenshots/
├── log.txt
├── keylogger_simulation.py
└── README.md

---




## ???🧠 Methodology


Create a GUI application using Tkinter
Add a text input area for user interaction
Capture manually entered text
Record timestamps for each entry
Save collected data into a local text file
Analyze how logging mechanisms work
Study security risks and prevention methods


---


## ???💻 Python Code
import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("Safe Key Logger Simulation")
window.geometry("400x300")

label = tk.Label(window, text="Type something below:")
label.pack(pady=10)

text_box = tk.Text(window, height=10, width=40)
text_box.pack()

def save_input():
    data = text_box.get("1.0", tk.END)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a") as file:
        file.write(f"Time: {time}\n")
        file.write(f"User Input: {data}\n")
        file.write("-" * 40 + "\n")

button = tk.Button(window, text="Save Input", command=save_input)
button.pack(pady=10)

window.mainloop()

---


## ???🔍 Code Explanation
Tk() creates the application window
Text() provides a text input area
datetime.now() generates timestamps
open() writes user input to a log file
Button() triggers the save function
User entries are stored locally for educational analysis

---


## ???⚠️ Security Risks of Real-World Keyloggers

Password theft
Sensitive information leakage
Privacy violations
Credential harvesting
Unauthorized system monitoring

---


## ???🛡️ Prevention Methods

Use trusted software only
Keep antivirus software updated
Enable firewall protection
Avoid suspicious downloads
Use multi-factor authentication (MFA)
Regularly monitor system activity


---

## ???✅ Results

The project successfully demonstrated how user input can be captured and stored within a controlled environment. It provided valuable insights into key logging concepts, cybersecurity risks, and defensive security practices.
---


## ???📚 Learning Outcomes


Understanding key logging concepts
Python GUI development using Tkinter
File handling and data storage
Cybersecurity risk awareness
Security best practices
Practical Python programming experience

---
## ???🚀 Future Improvements
Export logs to CSV format
Search and filter recorded entries
Add log encryption
Improve GUI design
Implement user authentication
Generate activity reports
---

## ???📸 Screenshots

---

## ???▶️ How to Run
Run the Program
py keylogger_simulation.py

---

## ???👨‍💻 Author

Muhammad Talha

Cybersecurity & Network Security Enthusiast