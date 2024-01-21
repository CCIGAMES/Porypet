import random
import tkinter as tk

win = tk.Tk()

win.attributes('-alpha', 0.0)
win.iconify()

# Create a Canvas to display the Porygon sprite
canvas = tk.Canvas(win, width=100, height=100, bd=0, highlightthickness=0)
canvas.pack()

# Load the Porygon sprite using tk.PhotoImage
porygon_image = tk.PhotoImage(file="porygon.png")

# Draw an image on the Canvas
porygon = canvas.create_image(0, 0, anchor=tk.NW, image=porygon_image)

def move_porygon():
    x = random.randint(0, 500)
    y = random.randint(0, 500)

    # Smoothly move the Porygon with tweening/glide effect
    coords = canvas.coords(porygon)
    start_x, start_y = coords[:2]  # Use only the first two values

    steps = 30  # Number of steps for tweening

    for i in range(1, steps + 1):
        new_x = start_x + (x - start_x) * i / steps
        new_y = start_y + (y - start_y) * i / steps
        canvas.coords(porygon, new_x, new_y)  # Update only x and y coordinates
        win.update()
        win.after(10)  # Adjust the delay for smooth animation

    # Set the final position
    canvas.coords(porygon, x, y)  # Update only x and y coordinates

    win.after(1000, move_porygon)  # Move Porygon every 1000 milliseconds

# Start the animation
move_porygon()

# Start the Tkinter event loop
win.mainloop()
