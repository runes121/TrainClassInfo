import tkinter
import ttkbootstrap as ttk
import wikipedia


window = ttk.Window(themename="darkly")
window.geometry("500x500")
window.title("Class Information.")

class_input = ttk.Entry(window, font=("Arial", 12))
class_input.pack(pady=5)


def change_info():
    print(f"Searching for: British Rail Class {class_input.get()}")
    summary = wikipedia.summary(f"British Rail Class {class_input.get()}", sentences=2, auto_suggest=False, redirect=False)
    information_box.config(text=summary)


get_info_button = ttk.Button(window, text="Get info!", command=change_info)
get_info_button.pack(pady=5)

information_box = ttk.Label(window, text="Enter a class to get information.", wraplength=470, font=("Arial", 13))
information_box.pack(pady=5)

warning_label = ttk.Label(window, text="Warning: Summaries may contain minimal error.", font=("Arial", 10), foreground="dark red")
warning_label.pack()
warning_label.place(relx=0.5, rely=0.95, anchor="center")

tkinter.mainloop()
