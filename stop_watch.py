import tkinter
import time

INTERVAL = 10
start_time = 0
start_flag = False
after_id = 0

def update_time():
    global start_time
    global app, label
    global after_id

    after_id = app.after(INTERVAL, update_time)
    now_time = time.time()
    elapsed_time = now_time - start_time
    elapsed_time_str = '{:.2f}'.format(elapsed_time)
    label.config(text=elapsed_time_str)

def start():
    global app
    global start_flag
    global start_time
    global after_id

    if not start_flag:
        start_flag = True
        start_time = time.time()
        after_id = app.after(INTERVAL, update_time)

def stop():
    global start_flag
    global after_id

    if start_flag:
        app.after_cancel(after_id)
        start_flag = False

app = tkinter.Tk()
app.title('ストップウォッチ')
app.geometry("250x150")
app.resizable(0, 0)
label = tkinter.Label(app, text='0.00', width=6, font=("", 50, "bold"),)
label.pack(padx=10, pady=10)

start_bt = tkinter.Button(app, text="Start", command=start, activebackground='yellow', width=14)
start_bt.pack(fill='x', padx=10, side='left')

stop_bt = tkinter.Button(app, text="Stop", command=stop, activebackground='yellow', width=14)
stop_bt.pack(fill='x', padx=10, side='left')

app.mainloop()