# -*- coding: utf-8 -*-
# @author: Batuhan Gürses

from tkinter import *
from get_window import title_of_window
from search_find_lyric import lyric_main

class SpotiLyric:
    """
        Example use of:
            - SpotiLyric()
    """
    def __init__(self):
        self.temp_song_name = ' ' # temporary variable for catch to changing song.
        # tkinter window settings
        self.top = Tk()
        self.top.attributes('-topmost', 1)
        self.scroll = Scrollbar(self.top)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.width = self.top.winfo_screenwidth()
        self.height = self.top.winfo_screenheight()
        self.top.geometry("480x{}+{}+0".format(self.height, self.width))

        # text settings
        self.text = Text(self.top, font=('Helvetica', 12))
        self.text.tag_configure('bold', font=('Helvetica',16, 'bold'))
        self.text.tag_configure('tiny', font=('Helvetica',10, 'italic'))
        self.text['bg'] = '#FFF'
        self.text['fg'] = '#222'
        # main run
        self.run()
        self.top.mainloop()

    def add_lyric_to_tk(self, song_name, lyric, url = ' '):
        """
            Processes of Tkinter Text()
            Inserts the lyrics, adds names of tracks to the title bar...
        """
        self.top.title(song_name)
        self.text.delete("1.0",END) # when song change, delete previous lyric
        self.text.insert(INSERT, song_name,'bold')
        self.text.insert(INSERT, "\n\n\n")
        self.text.insert(INSERT, lyric)
        self.text.insert(INSERT, "\n\n----\n")
        self.text.insert(INSERT, url, 'tiny')
        self.text.pack(expand=True, fill=BOTH)
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)

    def get_song_name(self):
        """
            Returns the song name that is currently playing on Spotify Desktop App.
        """
        return title_of_window("spotify")

    def get_lyric(self, song_name):
        """
            Returns the lyric of song which given as parameter.
        """
        return lyric_main(song_name)

    def run(self):
        song = self.get_song_name()
        if self.temp_song_name != song and song != None:
            # if program runs first time or playing song changes
            lyric = self.get_lyric(song)
            self.temp_song_name = song
            self.add_lyric_to_tk(song, lyric[0], lyric[1])
        self.top.after(10000,self.run)


# start
SpotiLyric()
