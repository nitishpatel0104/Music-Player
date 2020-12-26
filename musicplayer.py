import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Creating application window
musicplayer = tkr.Tk()

# Setting the title name
musicplayer.title("Music Player")

#Setting the dimension
musicplayer.geometry("450x350")

directory = askdirectory()

os.chdir(directory)

songlist = os.listdir()

playlist = tkr.Listbox(musicplayer, font = "Cambria 14 bold", bg = "cyan2", selectmode = tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

# Function to play the song
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# Function to Stop the music
def stop():
    pygame.mixer.music.stop()

# Function to Pause the music
def pause():
    pygame.mixer.music.pause()

# Function to Resume the music
def resume():
    pygame.mixer.music.unpause()

Button_play = tkr.Button(musicplayer, height=4, width=5, text="Play Music", font="Cambria 15 bold", command=play, bg="lime green", fg="black")
Button_stop = tkr.Button(musicplayer, height=4, width=5, text="Stop Music", font="Cambria 15 bold", command=stop, bg="red", fg="black")
Button_pause = tkr.Button(musicplayer, height=4, width=5, text="Pause Music", font="Cambria 15 bold", command=pause, bg="yellow", fg="black")
Button_resume = tkr.Button(musicplayer, height=4, width=5, text="Resume Music", font="Cambria 15 bold", command=resume, bg="yellow", fg="black")

Button_play.pack(fill="x")
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Cambria 12 bold", textvariable=var)

musicplayer.mainloop()