from tkinter import *
from tkinter import filedialog
import pygame
DEFAULT_VOLUME = 70

def load_file():
    global player
    # res = filedialog.askdirectory()
    # res = filedialog.askopenfile()  # کل اطلاعات مربوط به فایل و اسمش رو هم میده.
    res = filedialog.askopenfilename()  # اسم فایلی رو که انتخاب کردیم میده.
    # res = filedialog.askopenfilenames()  # اسم فایلهایی رو که انتخاب کردیم میده. البته اگه یه دونه هم باشه باید با اندیس 0 بهش دسترسی پیدا کنیم.
    # print (res)
    player.music.load(res)
    # player.music.load(res[0])
    # player.music.load('1.wav')
    # player.music.load('Yek Nafas Arezooye To (Homayoun Shajaryan).mp3')
    player.music.set_volume(DEFAULT_VOLUME/100)

def start():
    player.music.play()
def pause():
    player.music.pause()
def resume():
    player.music.unpause()
def stop():
    player.music.stop()
def change_volume(n): # خودش عدد انتخاب شده رو به عنوان یه متغیر به صورت استرینگ میفرسته.
    # print(n)
    player.music.set_volume(int(n)/100)
    # player.music.set_volume(volume.get()/100)


player = pygame.mixer
player.init()

root = Tk()
frame_up = Frame(root)
frame_down = Frame(root)
frame_up.pack(expand=1, fill='x')
frame_down.pack(expand=1, fill='x')
Button(frame_up, text='load file', command=load_file).pack(side='left', expand=1, fill='x')
Button(frame_up, text='start', command=start).pack(side='left', expand=1, fill='x')
Button(frame_up, text='pause', command=pause).pack(side='left', expand=1, fill='x')
Button(frame_up, text='resume', command=resume).pack(side='left', expand=1, fill='x')
Button(frame_up, text='stop', command=stop).pack(side='left', expand=1, fill='x')
Button(frame_up, text='exit', command=root.destroy).pack(side='left', expand=1, fill='x')
volume = Scale(frame_down, orient=HORIZONTAL, from_=0, to=100, command=change_volume, bg='dark cyan', fg='cyan', activebackground='orange')
volume.set(DEFAULT_VOLUME)
volume.pack(expand=1, fill='x')

mainloop()