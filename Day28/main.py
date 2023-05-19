import sys
import os
from tkinter import *
import math
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =  0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    main_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        main_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        main_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        main_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check.config(text=mark, fg=GREEN, bg=YELLOW)
        play_ringing_sound()

# ---------------------------- SOUND ------------------------------- #
def play_ringing_sound():
    pygame.mixer.init()
    sound_path = get_resource_path("bell.mp3")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Get the absolute path to the resource file
def get_resource_path(relative_path):
    """Get the absolute path to a resource file."""
    if getattr(sys, 'frozen', False):
        # Running as a bundle (PyInstaller executable)
        base_path = sys._MEIPASS
    else:
        # Running in a normal Python environment
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# Canvas "tomato"
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_path = get_resource_path("tomato.png")
tomato_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 138, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label "timer"
main_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
main_label.grid(column=1, row=0)

# Button start
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# Button reset
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

# Label with checks
check = Label()
check.grid(column=1, row=3)

# Initialize pygame for sound
pygame.init()

window.mainloop()
