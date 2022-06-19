import tkinter as tk
def change():
    temp = int(spin_temp.get())
    # print(temp, type(temp))
    if temp < 10:
        lbl_status.config(bg='light blue')
        status.set("Heater is On")
    elif temp < 28:
        lbl_status.config(bg='light green')
        status.set("Fan and heater are Off")
    else:
        lbl_status.config(bg='red')
        status.set("Fan is On")
root = tk.Tk()
root.geometry('250x200')
spin_temp = tk.Spinbox(root, from_=5, to=40, state='readonly'
                        , justify='center', width=5, command=change) # wrap=True
status = tk.StringVar()
lbl_status = tk.Label(root, textvariable=status)
spin_temp.grid(row=1, column=1, padx=10, pady=80)
lbl_status.grid(row=1, column=2, padx=10, pady=80)
root.mainloop()