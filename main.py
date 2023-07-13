from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# WORK_MIN = 1
# SHORT_BREAK_MIN = 0.5
# LONG_BREAK_MIN = 0.5
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    checkmark_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    # count_down(25 * 60)

    if reps % 2 == 1:
        timer_label.config(text="Work", fg=RED)
        count_down(work_secs)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(long_break_secs)
    else:
        timer_label.config(text="Break", fg=GREEN)
        count_down(short_break_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins, secs = count // 60, count % 60
    mins_secs = f"{mins:02d}:{secs:02d}"
    canvas.itemconfig(timer_text, text=mins_secs)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = reps // 2
        checkmark_label.config(text=checkmark*work_sessions)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

# tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# start button
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

# reset button
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

# checkmarks
checkmark = "✔"
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "normal"))
checkmark_label.grid(row=3, column=1)

window.mainloop()
