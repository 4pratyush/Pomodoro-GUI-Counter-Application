import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#829460"
YELLOW = "#FFF5E4"
FONT_NAME = "Courier"
WORK_MIN = 35
SHORT_BREAK_MIN = 15
LONG_BREAK_MIN = 25
Rep = 0
Check = ""
timer_nullifier = None

# ---GUI---
window = tkinter.Tk()
window.title("Pratyush's Pomodoro Project")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)
check_mark = tkinter.Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


def start_timer():
    global Check
    global Rep  # this line imports the Rep function from the global to the local,but we can't change it in the same line
    Rep = Rep + 1
    study = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN
    if Rep == 8:
        Rep = 0
        Check = ""
        check_mark.config(text=Check)
        count_down(long_break)
        title_label.config(text="Take a tea break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50))
    elif (Rep % 2) == 0:
        count_down(short_break)
        title_label.config(text="Listen music Bro", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
    elif (Rep % 2) != 0:
        count_down(study)
        title_label.config(text="Work Pratyush", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))


def end_timer():
    global Rep
    global Check
    Rep = 0
    Check = ""
    terminator = -1
    check_mark.config(text=Check)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    count_down(terminator)
    canvas.itemconfig(timer_text, text="00:00")


start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=end_timer)
reset_button.grid(row=3, column=2)


def count_down(count):
    global Rep
    global Check
    global timer_nullifier
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer_nullifier = window.after(1000, count_down,
                                       count - 1)  # count-1 is the value that would pe passed to the called function.
    elif count == 0:
        if Rep % 2 != 0:
            Check = Check + "✔️"
            check_mark.config(text=Check)
        start_timer()
    if count == -1:
        window.after_cancel(timer_nullifier)


window.mainloop()
