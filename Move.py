import tkinter as tk
import random
import time

win = tk.Tk()

win.attributes('-alpha', 0.0)
win.iconify()

window = tk.Toplevel(win)
window.overrideredirect(1)

photo = tk.PhotoImage(file="porygon.png")
label = tk.Label(window, image=photo, borderwidth=0, highlightthickness=0)
label.configure(highlightthickness=0, bd=0)
label.pack()

def move_porygon():
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    x, y = window.winfo_x() + dx, window.winfo_y() + dy
    window.geometry(f"+{x}+{y}")
    window.after(50, move_porygon)  # Use 'after' for smoother animation

# Bind events for dragging
start_x, start_y = 0, 0
def on_drag(event):
    move_porygon()

def start_drag(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

label.bind("<B1-Motion>", on_drag)
label.bind("<Button-1>", start_drag)

# Start the movement
move_porygon()

win.mainloop()
