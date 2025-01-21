from tkinter import *
import math

#constants
PINK = "#e2979c"
RED = "#FF6868"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
GRAY = "#EAE2C6"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_change = None

#Resetting of the timer
def reset_timer():
    global  reps
    window.after_cancel(timer_change)
    timer.config(text= "Timer")
    canvas_img.itemconfig(canvas_text,text = "00:00")
    check.config(text="✔")
    reps = 0

#Timer Mechanism
def start_count():
    global reps
    reps = reps + 1
    work =  WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        timer.config(text="Study", fg="green")
        count_down(work)

    elif reps % 8 == 0:
        timer.config(text="L.Break", fg=RED)
        count_down(long)

    else:
        timer.config(text="S.Break", fg=RED)
        count_down(short)



#Countdown Mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = "0"+str(count_sec)
    canvas_img.itemconfig(canvas_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer_change
        timer_change =window.after(2, count_down, count - 1)
    else:
        start_count()
        mark = " "
        working_reps = math.floor(reps / 2)
        for a in range(working_reps):
            mark += "✔"
        check.config(text=mark)



#Setting the UI

window = Tk()

window.title("Pomodoro Timer App")
window.config(padx= 110, pady=110, bg= GRAY)

timer = Label(text="Timer", fg= "green", font= ("Times New Roman", 40, "bold" ), bg= GRAY)
timer.config(pady= 20)
timer.grid(column = 1, row = 0)

canvas_img = canvas = Canvas(width=200, height=224, bg= GRAY, highlightthickness = 0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100,97,image = photo)
canvas_text = canvas.create_text(100, 115, text="00:00", font= ("Times New Roman", 40, "bold" ), fill= "Black")
canvas.grid(column= 1, row = 1)

start_button = Button(text="Start", fg= "green", bg= RED, font= ("Times New Roman", 15, "bold"), highlightthickness = 0, command=start_count)
start_button.grid(column = 0, row = 2)

reset_button = Button(text="Reset",fg= "green", bg= RED, font= ("Times New Roman", 15, "bold"), highlightthickness = 0, command = reset_timer)
reset_button.grid(column = 2, row = 2)

check = Label(text= "✔", fg= "green", bg = GRAY, font= ("Times New Roman", 10, "bold"), highlightthickness = 0)
check.config(padx= 10, pady= 10)
check.grid(column = 1, row = 3)


window.mainloop()