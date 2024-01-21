import tkinter as tk
import random

class DraggableWindow(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.overrideredirect(True)
        self.offset_x = 0
        self.offset_y = 0

        self.bind("<ButtonPress-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def on_drag_motion(self, event):
        x = self.winfo_pointerx() - self.offset_x
        y = self.winfo_pointery() - self.offset_y
        self.geometry(f"+{x}+{y}")

def smooth_movement(window, target_x, target_y, speed_factor):
    current_x, current_y = window.winfo_x(), window.winfo_y()
    dx = target_x - current_x
    dy = target_y - current_y

    new_x = current_x + int(dx * speed_factor)
    new_y = current_y + int(dy * speed_factor)

    window.geometry(f"+{new_x}+{new_y}")

    if abs(new_x - target_x) > 1 or abs(new_y - target_y) > 1:
        window.after(10, lambda: smooth_movement(window, target_x, target_y, speed_factor))

win = tk.Tk()
win.attributes('-alpha', 0.0)
win.iconify()

window = DraggableWindow(win)
window.attributes('-topmost', True)

photo = tk.PhotoImage(file="porygon.png")
label = tk.Label(window, image=photo, borderwidth=0, highlightthickness=0)
label.configure(highlightthickness=0, bd=0)
label.pack()

speed_factor = 0.05

def move_porygon():
    target_x = random.randint(0, win.winfo_screenwidth() - window.winfo_reqwidth())
    target_y = random.randint(0, win.winfo_screenheight() - window.winfo_reqheight())

    smooth_movement(window, target_x, target_y, speed_factor)

    win.after(2000, move_porygon)  # Change the delay as needed

move_porygon()

win.mainloop()
