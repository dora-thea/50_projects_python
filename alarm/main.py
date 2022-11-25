import datetime
import time
import tkinter as tk
import winsound


def alarm():
    while True:
        hour = int(lbl_value_hours["text"])
        minute = int(lbl_value_minutes["text"])

        set_alarm_time = f"{hour}:{minute}:00"

        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break


def increase_hours():
    value = int(lbl_value_hours["text"])
    if value < 23:
        lbl_value_hours["text"] = f"{value + 1}"
    else:
        lbl_value_hours["text"] = "0"


def decrease_hours():
    value = int(lbl_value_hours["text"])
    if value > 0:
        lbl_value_hours["text"] = f"{value - 1}"
    else:
        lbl_value_hours["text"] = "23"


def increase_minutes():
    value = int(lbl_value_minutes["text"])
    if value < 59:
        lbl_value_minutes["text"] = f"{value + 1}"
    else:
        lbl_value_minutes["text"] = "0"


def decrease_minutes():
    value = int(lbl_value_minutes["text"])
    if value > 0:
        lbl_value_minutes["text"] = f"{value - 1}"
    else:
        lbl_value_minutes["text"] = "59"


# window settings

window = tk.Tk()
window.geometry("400x150")
window.title("Alarm Clock")

for c in range(5):
    window.columnconfigure(index=c, weight=1)
for r in range(4):
    window.rowconfigure(index=r, weight=1)

# main labels

lbl_alarm = tk.Label(window, text="Alarm", font="Helvetica 15", fg="steel blue")
alarm_setter = tk.Button(window, text="Set Alarm", font="Helvetica 10", command=alarm, background="light steel blue", foreground="white")

lbl_alarm.grid(row=0, column=1, columnspan=3, sticky="nsew")
alarm_setter.grid(row=4, column=1, columnspan=3, sticky="nsew")

lbl_time = tk.Label(master=window, text=":")
lbl_time.grid(row=1, column=2)

# buttons for interaction with hours

btn_decrease_hours = tk.Button(
    master=window,
    text="-",
    command=decrease_hours
)

btn_decrease_hours.grid(row=2, column=0, sticky="nsew")

lbl_value_hours = tk.Label(master=window, text=f'{datetime.datetime.now().strftime("%H")}')
lbl_value_hours.grid(row=1, column=0, columnspan=2)

btn_increase_hours = tk.Button(
    master=window,
    text="+",
    command=increase_hours
)

btn_increase_hours.grid(row=2, column=1, sticky="nsew")

# buttons for interaction with minutes

btn_decrease_minutes = tk.Button(
    master=window,
    text="-",
    command=decrease_minutes
)

btn_decrease_minutes.grid(row=2, column=3, sticky="nsew")

lbl_value_minutes = tk.Label(master=window, text=f'{(int(datetime.datetime.now().strftime("%M")) + 5) % 60}')
lbl_value_minutes.grid(row=1, column=3, columnspan=2)

btn_increase_minutes = tk.Button(
    master=window,
    text="+",
    command=increase_minutes
)

btn_increase_minutes.grid(row=2, column=4, sticky="nsew")

window.mainloop()
