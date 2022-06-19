import tkinter as tk
from tkinter import messagebox as msb

R = 1
C = 1
correct = 0

def show():
    print(left_hand.get())

def send():
    global correct
    correct = 0
    if ans1.get() == 3:
        correct = correct + 1
    if ans2.get() == 2:
        correct = correct + 1
    # print(correct)
    msb.showinfo('Grade', f"Your grade in this exam is {correct*50}")
    # res = msb.askyesnocancel("title", "This is text")
    # if res == True:
    #     print('yes ra feshar dadid')
    # elif res == False:
    #     print('no ra feshar dadid')
    # elif res == None:
    #     print('cancel ra feshar dadid')

root = tk.Tk()
root.geometry('450x200')

left_hand = tk.IntVar()
ans1 = tk.IntVar()
ans2 = tk.IntVar()
cb_left_hand = tk.Checkbutton(root, text='left handed'
                , variable=left_hand, command=show)
rb_answer_1 = tk.Radiobutton(root, text="Rasht"     ,variable=ans1, value=1)
rb_answer_2 = tk.Radiobutton(root, text="Mashhad"   ,variable=ans1, value=2)
rb_answer_3 = tk.Radiobutton(root, text="Tehran"    ,variable=ans1, value=3)
rb_answer_4 = tk.Radiobutton(root, text="Isfahan"   ,variable=ans1, value=4)
lbl_q1 = tk.Label(root, text='1) What is the Capital city of Irasdafkl;fjlksdajfn?')
rb_answer2_1 = tk.Radiobutton(root, text="100000km2"    ,variable=ans2, value=1)
rb_answer2_2 = tk.Radiobutton(root, text="1600000km2"   ,variable=ans2, value=2)
rb_answer2_3 = tk.Radiobutton(root, text="5000km2"      ,variable=ans2, value=3)
rb_answer2_4 = tk.Radiobutton(root, text="3000km2"      ,variable=ans2, value=4)
lbl_q2 = tk.Label(root, text='2) Area of Iran?')
btn_send = tk.Button(root, text="Send", command=send)
btn_exit = tk.Button(root, text="Exit", command=root.destroy)


cb_left_hand.grid(row=R, column=C)
lbl_q1.grid(row=R+1, column=C, columnspan=4, sticky='w')
rb_answer_1.grid(row=R+2, column=C, sticky='w')
rb_answer_2.grid(row=R+2, column=C+1, sticky='w')
rb_answer_3.grid(row=R+2, column=C+2, sticky='w')
rb_answer_4.grid(row=R+2, column=C+3, sticky='w')
lbl_q2.grid(row=R+3, column=C, columnspan=4, sticky='w')
rb_answer2_1.grid(row=R+4, column=C, sticky='w')
rb_answer2_2.grid(row=R+4, column=C+1, sticky='w')
rb_answer2_3.grid(row=R+4, column=C+2, sticky='w')
rb_answer2_4.grid(row=R+4, column=C+3, sticky='w')
btn_send.grid(row=R+5, column=C, columnspan=2, pady=20)
btn_exit.grid(row=R+5, column=C+2, columnspan=2, pady=20)


root.mainloop()