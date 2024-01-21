import time
import random
import tkinter as tk
from PIL import Image, ImageTk

def make_transparent(image_path):
    img = Image.open(image_path)
    img = img.convert("RGBA")

    # Extract the alpha channel
    alpha = img.split()[3]

    # Make the grey pixels transparent
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y))[:3] == (128, 128, 128):  # Adjust the RGB values for your grey color
                alpha.putpixel((x, y), 0)

    img.putalpha(alpha)
    return img

def set_window_shape(window, image):
    # Set the window size and shape based on the sprite dimensions
    window.geometry(f"{image.width}x{image.height}")

def move_porygon(dx, dy):
    x, y = window.winfo_x(), window.winfo_y()
    new_x, new_y = x + dx, y + dy
    window.geometry(f"+{new_x}+{new_y}")
    window.update()

def on_drag(event):
    move_porygon(event.x - start_x, event.y - start_y)

def start_drag(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

win = tk.Tk()

win.attributes('-alpha', 0.0)
win.iconify()

window = tk.Toplevel(win)
window.overrideredirect(1)

# Use the function to make the grey background transparent
porygon_img = make_transparent("porygon.png")

# Convert the image to PhotoImage
photo = ImageTk.PhotoImage(porygon_img)

# Set the window shape
set_window_shape(window, porygon_img)

label = tk.Label(window, image=photo, borderwidth=0, highlightthickness=0)
label.configure(highlightthickness=0, bd=0)
label.pack()

# Bind events for dragging
label.bind("<B1-Motion>", on_drag)
label.bind("<Button-1>", start_drag)

def animate_porygon():
    for _ in range(100):
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        move_porygon(dx, dy)
        time.sleep(0.05)

# Start the movement
animate_porygon()

win.mainloop()
