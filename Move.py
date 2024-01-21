import random
import tkinter as tk

win = tk.Tk()

win.attributes('-alpha', 0.0)
win.iconify()

window = tk.Toplevel(win)
window.geometry("500x500+100+100")
window.overrideredirect(1)

photo = tk.PhotoImage(file="porygon.png")

label = tk.Label(window, image=photo, borderwidth=0, highlightthickness=0)
label.configure(highlightthickness=0, bd=0)
label.pack()

def move_porygon():
    x = random.randint(0, 400)  # Adjusted the x-coordinate range to prevent going off-screen
    y = random.randint(0, 400)  # Adjusted the y-coordinate range to prevent going off-screen
    window.geometry("+%d+%d" % (x, y))
    window.after(50, move_porygon)

move_porygon()

win.mainloop()
