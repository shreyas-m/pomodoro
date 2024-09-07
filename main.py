from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.after_cancel(timer)
    timer_label.configure(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    canvas.itemconfigure(timer_text, text="00:00")
    global reps
    reps = 0
    counter["text"] = ""


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_berak_sec = LONG_BREAK_MIN * 60

    reps = reps % 8

    if reps == 7:
        countdown_timer(long_berak_sec)
        timer_label.configure(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown_timer(work_sec)
        timer_label.configure(text="Work", fg=GREEN)
    else:
        countdown_timer(short_break_sec)
        timer_label.configure(text="Break", fg=PINK)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_timer(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"

    canvas.itemconfigure(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = canvas.after(1000, countdown_timer, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        counter["text"] = marks


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=3, column=0)

counter = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
counter.grid(row=4, column=1)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=3, column=2)

window.mainloop()
