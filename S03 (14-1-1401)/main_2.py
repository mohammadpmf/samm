import tkinter as tk

def save():
    name = e_name.get()
    if name == "":
        return
    family = e_family.get()
    f = open(name, 'w')
    f.write(f"Name: {name}\nFamily: {family}")
    f.close()

root = tk.Tk()
root.title('Mohammad Window')
root.geometry("600x400+100+200")
# root.resizable(0, 0)
root.config(bg='light blue')
#######################  defining widgets  ####################
lbl_name = tk.Label(root, text="Name: ", bg='light blue', fg='blue',
                        font=('B Nazanin', 20))
e_name = tk.Entry(root, bg="cyan", fg='red', font=('B Nazanin', 20))
lbl_family = tk.Label(root, text="Family: ", bg='light blue', fg='blue',
                        font=('B Nazanin', 20))
e_family = tk.Entry(root, bg="cyan", fg='red', font=('B Nazanin', 20))
btn_save = tk.Button(root, bg='pink', pady=30, padx=30, text='Save',
font=('B Nazanin', 20), command=save)
btn_exit = tk.Button(root, bg='pink', pady=30, padx=30, text='Exit',
font=('B Nazanin', 20), command=exit)
##############################################################


#######################  packing widgets  ####################
# lbl_name.pack()
# e_name.pack()
# lbl_family.pack(expand=1, fill='both')
# e_family.pack()
# btn_save.pack(pady=20)
# btn_exit.pack()
##############################################################

#######################  placing widgets  ####################
# lbl_name.place(x=0, y=0)
# e_name.place(x=100, y=0)
# lbl_family.place(x=0, y=50)
# e_family.place(x=100, y=50)
# btn_save.place(x=35, y=90, width=120, height=120)
# btn_exit.place(x=35, y=220, width=120, height=120)
##############################################################

#######################  gridding widgets  ####################
lbl_name.grid(row=1, column=1, padx=100, pady=20)
e_name.grid(row=1, column=2)
lbl_family.grid(row=2, column=1)
e_family.grid(row=2, column=2)
btn_save.grid(row=3, column=1)
btn_exit.grid(row=3, column=2, sticky='ew')
##############################################################


root.mainloop()