import time
import random
import tkinter as tk
from Pillow import Image, ImageTk

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

win = tk.Tk()

win.attributes('-alpha', 0.0)
win.iconify()

window = tk.Toplevel(win)
window.geometry("500x500+100+100")
window.overrideredirect(1)

# Use the function to make the grey background transparent
porygon_img = make_transparent("porygon.png")
photo = ImageTk.PhotoImage(porygon_img)

label = tk.Label(window, image=photo, borderwidth=0, highlightthickness=0)
label.configure(highlightthickness=0, bd=0)
label.pack()

def move_porygon(dx, dy):
    x, y = window.winfo_x(), window.winfo_y()
    new_x, new_y = x + dx, y + dy
    window.geometry("+%d+%d" % (new_x, new_y))
    window.update()

def animate_porygon():
    for _ in range(100):
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        move_porygon(dx, dy)
        time.sleep(0.05)

# Start the movement
animate_porygon()

win.mainloop()
