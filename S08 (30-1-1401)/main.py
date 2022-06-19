import tkinter as tk

R = 1
C = 1

def show():
    print(left_hand.get())

root = tk.Tk()
root.geometry('450x200')

left_hand = tk.IntVar()
cb_left_hand = tk.Checkbutton(root, text='left handed'
                , variable=left_hand, command=show)
rb_answer_1 = tk.Radiobutton(root, text="Rasht")
rb_answer_2 = tk.Radiobutton(root, text="Mashhad")
rb_answer_3 = tk.Radiobutton(root, text="Tehran")
rb_answer_4 = tk.Radiobutton(root, text="Isfahan")
lbl_q1 = tk.Label(root, text='1) Capital of Iran?')
rb_answer2_1 = tk.Radiobutton(root, text="100000km2")
rb_answer2_2 = tk.Radiobutton(root, text="1600000km2")
rb_answer2_3 = tk.Radiobutton(root, text="5000km2")
rb_answer2_4 = tk.Radiobutton(root, text="3000km2")
lbl_q2 = tk.Label(root, text='2) Area of Iran?')

cb_left_hand.grid(row=R, column=C)
lbl_q1.grid(row=R+1, column=C)
rb_answer_1.grid(row=R+2, column=C)
rb_answer_2.grid(row=R+2, column=C+1)
rb_answer_3.grid(row=R+2, column=C+2)
rb_answer_4.grid(row=R+2, column=C+3)
lbl_q2.grid(row=R+3, column=C)
rb_answer2_1.grid(row=R+4, column=C)
rb_answer2_2.grid(row=R+4, column=C+1)
rb_answer2_3.grid(row=R+4, column=C+2)
rb_answer2_4.grid(row=R+4, column=C+3)

root.mainloop()