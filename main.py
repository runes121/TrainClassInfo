import json
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
    try:
        summary = wikipedia.summary(f"British Rail Class {class_input.get()}", sentences=2, auto_suggest=False, redirect=True)
        information_box.config(text=summary)
        with open(r"C:\Users\Admin\PycharmProjects\TrainClassInfo\offline.json", "r+") as f:
            data = json.load(f)
            if class_input.get() not in data:
                data[class_input.get()] = summary
            elif data[class_input.get()] != summary:
                data[class_input.get()] = summary
            json.dump(data, f, indent=4)
    except wikipedia.exceptions.PageError:
        information_box.config(text="Couldn't find class info. Does it even exist?")
    except Exception as e:
        information_box.config(text=f"An unknown error occurred. {e}")


get_info_button = ttk.Button(window, text="Get info!", command=change_info)
get_info_button.pack(pady=5)

information_box = ttk.Label(window, text="Enter a class to get information.", wraplength=470, font=("Arial", 13))
information_box.pack(pady=5)

wikipedia_credit = ttk.Label(window, text="Summaries taken from Wikipedia.", font=("Arial", 10))
wikipedia_credit.pack()
wikipedia_credit.place(relx=0.5, rely=0.95, anchor="center")

tkinter.mainloop()
