import tkinter
import ttkbootstrap as ttk
import traininfo


window = ttk.Window(themename="darkly")
window.geometry("500x500")
window.title("Class Information.")

class_input = ttk.Entry(window, font=("Arial", 12))
class_input.pack(pady=5)


def change_info():
    summary = traininfo.get_train_summary(class_input.get())
    information_box.config(text=summary)


get_info_button = ttk.Button(window, text="Get info!", command=change_info)
get_info_button.pack(pady=5)

information_box = ttk.Label(window, text="Enter a class to get information.", wraplength=470, font=("Arial", 10))
information_box.pack(pady=5)

warning_label = ttk.Label(window, text="Warning: Summaries may contain minimal error.", font=("Arial", 10), foreground="dark red")
warning_label.pack()
warning_label.place(relx=0.5, rely=0.95, anchor="center")

tkinter.mainloop()
