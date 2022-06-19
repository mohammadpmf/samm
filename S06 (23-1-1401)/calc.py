import tkinter as tk
R = 1
C = 1

def clear1():
    res = len(e_result.get())-1
    e_result.delete(res, tk.END)
    # e_result.delete(len(e_result.get())-1, tk.END)


def clear():
    e_result.delete(0, tk.END)

def equal():
    try:
        res = eval(e_result.get())
    except:
        res = "Error"
    clear()
    e_result.insert(0, res)

def add_n(n):
    e_result.insert(tk.END, n)
root = tk.Tk()
# root.geometry('400x400')
root.title('Calculator')
root.resizable(0, 0)
btn0 = tk.Button(root, text=0, font=('', 26), command=lambda: add_n(0))
btn1 = tk.Button(root, text=1, font=('', 26), command=lambda: add_n(1))
btn2 = tk.Button(root, text=2, font=('', 26), command=lambda: add_n(2))
btn3 = tk.Button(root, text=3, font=('', 26), command=lambda: add_n(3))
btn4 = tk.Button(root, text=4, font=('', 26), command=lambda: add_n(4))
btn5 = tk.Button(root, text=5, font=('', 26), command=lambda: add_n(5))
btn6 = tk.Button(root, text=6, font=('', 26), command=lambda: add_n(6))
btn7 = tk.Button(root, text=7, font=('', 26), command=lambda: add_n(7))
btn8 = tk.Button(root, text=8, font=('', 26), command=lambda: add_n(8))
btn9 = tk.Button(root, text=9, font=('', 26), command=lambda: add_n(9))
btnplus = tk.Button(root, text='+', bg='green', activebackground='light green', font=('', 26), command=lambda: add_n('+'))
btnminus = tk.Button(root, text='-', font=('', 26), command=lambda: add_n('-'))
btnmultiply = tk.Button(root, text='X', font=('', 26), command=lambda: add_n('*'))
btndevision = tk.Button(root, text='÷', font=('', 26), command=lambda: add_n('/'))
btnequal = tk.Button(root, text='=', font=('', 26), command=equal)
btnclear = tk.Button(root, text='C', font=('', 26), command=clear)
btndelete = tk.Button(root, text='⟵', font=('', 26), command=clear1)
btndot = tk.Button(root, text='.', font=('', 26), command=lambda: add_n('.'))
e_result = tk.Entry(root, font=('', 26))

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
print("OK")
tk.mainloop()