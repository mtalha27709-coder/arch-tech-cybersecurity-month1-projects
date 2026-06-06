import tkinter as tk
from datetime import datetime

# window creat
window = tk.Tk()
window.title("Safe Key Logger Simulation")
window.geometry("400x300")

# label
label = tk.Label(window, text="Type something below:")
label.pack(pady=10)

# text box
text_box = tk.Text(window, height=10, width=40)
text_box.pack()

# function to save input
def save_input():
    data = text_box.get("1.0", tk.END)

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a") as file:
        file.write(f"Time: {time}\n")
        file.write(f"User Input: {data}\n")
        file.write("-" * 40 + "\n")

    status_label.config(text="Saved successfully!")

# button
button = tk.Button(window, text="Save Input", command=save_input)
button.pack(pady=10)

# status
status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()