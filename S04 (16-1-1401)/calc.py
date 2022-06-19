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
btnplus = tk.Button(root, text='+', font=('', 16))
btnminus = tk.Button(root, text='-', font=('', 16))
btnmultiply = tk.Button(root, text='X', font=('', 16))
btndevision = tk.Button(root, text='÷', font=('', 16))
btnequal = tk.Button(root, text='=', font=('', 16))
btnclear = tk.Button(root, text='C', font=('', 16))
btndelete = tk.Button(root, text='⟵', font=('', 16))
btndot = tk.Button(root, text='.', font=('', 16))
e_result = tk.Entry(root, font=('', 16))

btn7.grid(row=R, column=C, sticky='news')
btn8.grid(row=R, column=C+1, sticky='news')
btn9.grid(row=R, column=C+2, sticky='news')
btn4.grid(row=R+1, column=C, sticky='news')
btn5.grid(row=R+1, column=C+1, sticky='news')
btn6.grid(row=R+1, column=C+2, sticky='news')
btn1.grid(row=R+2, column=C, sticky='news')
btn2.grid(row=R+2, column=C+1, sticky='news')
btn3.grid(row=R+2, column=C+2, sticky='news')
btn0.grid(row=R+3, column=C, sticky='news')
btnequal.grid(row=R+3, column=C+1, columnspan=2, sticky='news')
btnplus.grid(row=R, rowspan=2, column=C+3, sticky='news')
btnminus.grid(row=R+2, column=C+3, sticky='news')
btndelete.grid(row=R, column=C+4, sticky='news')
btnclear.grid(row=R+1, column=C+4, sticky='news')
btnmultiply.grid(row=R+2, column=C+4, sticky='news')
btndevision.grid(row=R+3, column=C+4, sticky='news')
btndot.grid(row=R+3, column=C+3, sticky='news')
e_result.grid(row=R-1, column=C, columnspan=5, sticky='news')

tk.mainloop()