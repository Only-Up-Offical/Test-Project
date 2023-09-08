import tkinter as tk

def on_enter(event):
    button.config(bg="yellow")

def on_leave(event):
    button.config(bg="SystemButtonFace")  # Reset to the default background color

window = tk.Tk()
window.title("Hover Effect Example")

button = tk.Button(window, text="Hover Me")
button.pack()

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

window.mainloop()