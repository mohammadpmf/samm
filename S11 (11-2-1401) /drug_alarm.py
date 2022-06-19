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
def start(n):
    h = int(spin_h_1.get())
    m = int(spin_m_1.get())
    s = int(spin_s_1.get())
    while not(h == 0 and m == 0 and s == 0):
        # t1.set(f"{h:02}:{m:02}:{s:02}")
        t1.set("{:02}:{:02}:{:02}".format(h, m, s))
        root.update()
        sleep(1)
        s = s - 1


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