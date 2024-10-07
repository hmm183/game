import tkinter as tk
import subprocess
from time import time

def on_button_click():
    global click_count
    click_count += 1
    click_label.config(text=f"Clicks: {click_count}")

    if click_count < 60 and (time() - start_time) < 20:
        pass
    else:
        trigger_cmd()

def trigger_cmd():
    subprocess.run("your_cmd_here", shell=True)

click_count = 0
start_time = 0


click_label = tk.Label(frame12, text="Clicks: 0")
click_label.pack()

button = tk.Button(frame12, text="Click Me", command=on_button_click)
button.pack()

def start_timer():
    global start_time
    start_time = time()

frame12.after(20000, trigger_cmd)  # 20 seconds timer
frame12.after(1000, start_timer)   # 1 second delay to start timer

frame12.mainloop()
