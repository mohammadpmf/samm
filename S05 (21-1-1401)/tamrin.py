import tkinter as tk

root = tk.Tk()
root.geometry('800x600')

lbl_result = tk.Label(root, text='0', bg='white', anchor='w', font=('Arial', 24))
btn000 = tk.Button(root, text='000')
btn0 = tk.Button(root, text=0)
btn1 = tk.Button(root, text=1)
btn2 = tk.Button(root, text=2)
btn3 = tk.Button(root, text=3)
btn4 = tk.Button(root, text=4)
btn5 = tk.Button(root, text=5)
btn6 = tk.Button(root, text=6)
btn7 = tk.Button(root, text=7)
btn8 = tk.Button(root, text=8)
btn9 = tk.Button(root, text=9)

btn000.place(relx = 0.13, rely=0.88, relwidth=0.21, relheight=0.1)
btn0.place(relx = 0.02, rely=0.88, relwidth=0.1, relheight=0.1)
btn1.place(relx = 0.02, rely=0.77, relwidth=0.1, relheight=0.1)
btn2.place(relx = 0.13, rely=0.77, relwidth=0.1, relheight=0.1)
btn3.place(relx = 0.24, rely=0.77, relwidth=0.1, relheight=0.1)
btn4.place(relx = 0.02, rely=0.66, relwidth=0.1, relheight=0.1)
btn5.place(relx = 0.13, rely=0.66, relwidth=0.1, relheight=0.1)
btn6.place(relx = 0.24, rely=0.66, relwidth=0.1, relheight=0.1)
btn7.place(relx = 0.02, rely=0.55, relwidth=0.1, relheight=0.1)
btn8.place(relx = 0.13, rely=0.55, relwidth=0.1, relheight=0.1)
btn9.place(relx = 0.24, rely=0.55, relwidth=0.1, relheight=0.1)
lbl_result.place(relx = 0.02, rely=0.44, relwidth=0.32, relheight=0.1)

root.mainloop()