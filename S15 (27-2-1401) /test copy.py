from tkinter import *
import pygame

player = pygame.mixer
player.init()
player.music.load("1.wav")
player.music.play()
root = Tk()

mainloop()