import datetime
import threading
import time
import tkinter

def view_time():
    while True:
        now = datetime.datetime.now()
        time_str = "{:02}:{:02}:{:02}".format(now.hour, now.minute, now.second)
        app.delete("all")
        app.create_text(160, 80, text=time_str, font=(None,48))
        time.sleep(1)

app = tkinter.Canvas(width=320, height=160)
app.pack()
app.create_text(10, 10, text='text')

t = threading.Thread(target=view_time, daemon=True)
t.start()

app.mainloop()