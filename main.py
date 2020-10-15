import tkinter as tk

options = ['A', 'B', 'C']


def record_selection(option):
    return(option)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text=options[1],
                   fg="red",
                   command=record_selection(options[1]))
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text=options[2],
                   command=record_selection(options[2]))
slogan.pack(side=tk.LEFT)

root.mainloop()
