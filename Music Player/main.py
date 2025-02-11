# Sainofo Fanene
# Personal Project: Music Player
# Start Date: 8.17.24

# importing the required libraries
import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
import fnmatch
import os
import pygame
from pygame import mixer

# start of using "canvas" as a code name to set up window
canvas = tk.Tk()
# window title
canvas.title("Music Player")
# window size (length & width)
canvas.geometry("900x900")
# window background color
canvas.config(bg='black')

# location to find a list of songs
root_dir = r'C:\Users\nofof\PycharmProjects\MusicPlayer\MusicPlaylist'
pattern = "*.mp3"

pygame.mixer.init()

# adding images for the buttons on interface display
repeat_image = tk.PhotoImage(file="repeat_button.png")
prev_image = tk.PhotoImage(file="prev_button.png")
stop_image = tk.PhotoImage(file="stop_button.png")
play_image = tk.PhotoImage(file="play_button.png")
pause_image = tk.PhotoImage(file="pause_button.png")
skip_next_image = tk.PhotoImage(file="skip_next_button.png")
shuffle_image = tk.PhotoImage(file="shuffle_button.png")

# functions
def load_music():
    file = filedialog.askopenfilename(initialdir=root_dir, filetypes=[("*.mp3")])
    if file:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

def select():
    Label.config(text=listBox.get("anchor"))
    mixer.music.load(root_dir + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    Label.config(text=next_song_name)

    mixer.music.load(root_dir + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate((next_song))
    listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    Label.config(text=next_song_name)

    mixer.music.load(root_dir + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pause_button["text"] == "pause":
        mixer.music.pause()
        pause_button["text"] = "play"
    else:
        mixer.music.unpause()
        pause_button["text"] = "pause"
    
# creating a playlist
listBox = tk.Listbox(canvas, fg="magenta", bg="black", width=100, font=("ds_digital",28))
listBox.pack(padx=15, pady=15)

# setting up label for the list of songs
Label = tk.Label(canvas, text=' ', bg='black', fg='pink', font=("ds_digital",28))
# padding label
Label.pack(pady=15)

# "top" as the variable for labels in horizontal order
top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

# music playing buttons display
prev_button = tk.Button(canvas, text="previous", image=prev_image, bg='black', borderwidth=0, command=play_prev)
prev_button.pack(pady=15, in_=top, side='left')

stop_button = tk.Button(canvas, text="stop", image=stop_image, bg='black', borderwidth=0, command=stop)
stop_button.pack(pady=15, in_=top, side='left')

play_button = tk.Button(canvas, text="play", image=play_image, bg='black', borderwidth=0, command=select)
play_button.pack(pady=15, in_=top, side='left')

pause_button = tk.Button(canvas, text="pause", image=pause_image, bg='black', borderwidth=0, command=pause_song)
pause_button.pack(pady=15, in_=top, side='left')

skip_next_button = tk.Button(canvas, text="skip/next", image=skip_next_image, bg='black', borderwidth=0, command=play_next)
skip_next_button.pack(pady=15, in_=top, side='left')

# volume control and display
# volume_slider = ttk.Scale

# song progress bar


# creating a for-loop 
for root, dirs, files in os.walk(root_dir):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

# window display
canvas.mainloop()