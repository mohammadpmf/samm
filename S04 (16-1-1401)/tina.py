import tkinter as tk

root=tk.Tk()
root.title("tina window")
root.geometry("600x400+0+0")
root.resizable(0,0)
root.config(bg="black")
lbl_name=tk.Label(root,text="\n\nname:\n",bg="black",fg="pink",font='bold')
e_name=tk.Entry(root,bg="pink",fg="black",font='classic,8')
lbl_name2=tk.Label(root,text="\n\nlast name:\n",bg="black",fg="pink",font='bold')
e_name2=tk.Entry(root,bg="pink",fg="black",font='classic,8')
lbl_name.pack()
e_name.pack()
lbl_name2.pack()
e_name2.pack()



root.mainloop()