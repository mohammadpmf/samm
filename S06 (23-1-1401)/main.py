import tkinter as tk

root = tk.Tk()
root.title('Mohammad Window')
root.geometry("600x400+100+200")
root.resizable(0, 0)
root.config(bg='light blue')
lbl_name = tk.Label(root, text="Man Mohammad Hastam",
                        bg='light blue', fg='blue',
                        font=('B Nazanin', 20))
e_name = tk.Entry(root, bg="cyan", fg='red', font=('B Nazanin', 20), show='*')
lbl_name.pack()
e_name.pack()

root.mainloop()