import tkinter as tk
import random

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
    
    # Get the current window position
    current_x, current_y = window.winfo_x(), window.winfo_y()
    
    # Calculate the new position
    new_x, new_y = current_x + dx, current_y + dy
    
    # Get desktop width and height
    desktop_width = win.winfo_screenwidth()
    desktop_height = win.winfo_screenheight()
    
    # Ensure the new position stays within desktop borders
    new_x = max(0, min(new_x, desktop_width - window.winfo_width()))
    new_y = max(0, min(new_y, desktop_height - window.winfo_height()))
    
    # Set the new position
    window.geometry(f"+{new_x}+{new_y}")
    
    win.after(50, move_porygon)  # Use 'after' for smoother animation

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
