import tkinter as tk
R = 1
C = 1
root = tk.Tk()
root.geometry('400x400')
root.title('Calculator')
btn0 = tk.Button(root, text=0, font=('', 16))
btn1 = tk.Button(root, text=1, font=('', 16))
btn2 = tk.Button(root, text=2, font=('', 16))
btn3 = tk.Button(root, text=3, font=('', 16))
btn4 = tk.Button(root, text=4, font=('', 16))
btn5 = tk.Button(root, text=5, font=('', 16))
btn6 = tk.Button(root, text=6, font=('', 16))
btn7 = tk.Button(root, text=7, font=('', 16))
btn8 = tk.Button(root, text=8, font=('', 16))
btn9 = tk.Button(root, text=9, font=('', 16))
btn7.grid(row=R, column=C)
btn8.grid(row=R, column=C+1)
btn9.grid(row=R, column=C+2)
btn4.grid(row=R+1, column=C)
btn5.grid(row=R+1, column=C+1)
btn6.grid(row=R+1, column=C+2)
tk.mainloop()