import tkinter as tk

lives = 3
root = tk.Tk()
frame = tk.Frame(root)
canvas = tk.Canvas(frame, width=600, hieght=400, bg="#AAAAFF")
frame.pack()
canvas.pack()
root.title("BREAKOUT")
root.mainloop()