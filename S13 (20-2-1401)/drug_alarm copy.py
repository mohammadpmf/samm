import threading
import tkinter as tk

root = tk.Tk()

lbl_frm1 = tk.LabelFrame(root, text='Amoxicilin')
lbl_frm2 = tk.LabelFrame(root, text='Antihistamine')
lbl_frm3 = tk.LabelFrame(root, text='Astaminophine')
lbl_frm1.grid(row=1, column=1, padx=5, pady=5)
lbl_frm2.grid(row=1, column=2, padx=5, pady=5)
lbl_frm3.grid(row=1, column=3, padx=5, pady=5)

spin_h_1 = tk.Spinbox(lbl_frm1, from_=0, to=23, width=2, state='readonly')
spin_m_1 = tk.Spinbox(lbl_frm1, from_=0, to=59, width=2, state='readonly')
spin_s_1 = tk.Spinbox(lbl_frm1, from_=0, to=59, width=2, state='readonly')
spin_h_2 = tk.Spinbox(lbl_frm2, from_=0, to=23, width=2, state='readonly')
spin_m_2 = tk.Spinbox(lbl_frm2, from_=0, to=59, width=2, state='readonly')
spin_s_2 = tk.Spinbox(lbl_frm2, from_=0, to=59, width=2, state='readonly')
spin_h_3 = tk.Spinbox(lbl_frm3, from_=0, to=23, width=2, state='readonly')
spin_m_3 = tk.Spinbox(lbl_frm3, from_=0, to=59, width=2, state='readonly')
spin_s_3 = tk.Spinbox(lbl_frm3, from_=0, to=59, width=2, state='readonly')
spin_h_1.grid(row=1, column=1)
spin_m_1.grid(row=1, column=2)
spin_s_1.grid(row=1, column=3)
spin_h_2.grid(row=1, column=1)
spin_m_2.grid(row=1, column=2)
spin_s_2.grid(row=1, column=3)
spin_h_3.grid(row=1, column=1)
spin_m_3.grid(row=1, column=2)
spin_s_3.grid(row=1, column=3)

t1 = tk.StringVar()
t2 = tk.StringVar()
t3 = tk.StringVar()
t1.set("00:00:00")
t2.set("00:00:00")
t3.set("00:00:00")
lbl_time_1 = tk.Label(lbl_frm1, textvariable=t1)
lbl_time_2 = tk.Label(lbl_frm2, textvariable=t2)
lbl_time_3 = tk.Label(lbl_frm3, textvariable=t3)
lbl_time_1.grid(row=2, column=1, columnspan=3)
lbl_time_2.grid(row=2, column=1, columnspan=3)
lbl_time_3.grid(row=2, column=1, columnspan=3)
from time import sleep

def count_down(n, h, m, s):
    while not(h == 0 and m == 0 and s == 0):
        # t1.set(f"{h:02}:{m:02}:{s:02}")
        if n==1:
            t1.set("{:02}:{:02}:{:02}".format(h, m, s))
        elif n==2:
            t2.set("{:02}:{:02}:{:02}".format(h, m, s))
        elif n==3:
            t3.set("{:02}:{:02}:{:02}".format(h, m, s))
        root.update()
        sleep(0.01)
        s = s - 1
        # s -= 1
        if s==-1:
            if m > 0:
                m = m - 1
                s = s + 60
            elif m==0:
                if h > 0:
                    h = h - 1
                    m = m + 59
                    s = s + 60
                elif h==0:
                    s = 0
    if n==1:
        t1.set("{:02}:{:02}:{:02}".format(h, m, s))
        btn_s_1.config(state='normal')
    elif n==2:
        t2.set("{:02}:{:02}:{:02}".format(h, m, s))
        btn_s_2.config(state='normal')
    elif n==3:
        t3.set("{:02}:{:02}:{:02}".format(h, m, s))
        btn_s_3.config(state='normal')

def start(n):
    if n == 1:
        h = int(spin_h_1.get())
        m = int(spin_m_1.get())
        s = int(spin_s_1.get())
        btn_s_1.config(state='disabled')
    elif n == 2:
        h = int(spin_h_2.get())
        m = int(spin_m_2.get())
        s = int(spin_s_2.get())
        btn_s_2.config(state='disabled')
    elif n == 3:
        h = int(spin_h_3.get())
        m = int(spin_m_3.get())
        s = int(spin_s_3.get())
        btn_s_3.config(state='disabled')
    t = threading.Thread(target=count_down, args=(n,h,m,s))
    t.setDaemon(True)
    t.start()
    
    

btn_s_1 = tk.Button(lbl_frm1, text="Start", command=lambda: start(1))
btn_s_2 = tk.Button(lbl_frm2, text="Start", command=lambda: start(2))
btn_s_3 = tk.Button(lbl_frm3, text="Start", command=lambda: start(3))
btn_s_1.grid(row=3, column=1)
btn_s_2.grid(row=3, column=1)
btn_s_3.grid(row=3, column=1)

btn_r_1 = tk.Button(lbl_frm1, text="Reset")
btn_r_2 = tk.Button(lbl_frm2, text="Reset")
btn_r_3 = tk.Button(lbl_frm3, text="Reset")
btn_r_1.grid(row=3, column=3)
btn_r_2.grid(row=3, column=3)
btn_r_3.grid(row=3, column=3)

root.mainloop()