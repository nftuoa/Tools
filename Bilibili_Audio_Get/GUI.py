import tkinter as tk
import audioget as ag

class RootPage:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Bilibili-Audio-Get')
        self.root.geometry('400x200')

        MainPage(self.root)

class MainPage:

    def __init__(self, root):
        self.root = root
        self.mainpage = tk.Frame(self.root)
        self.mainpage.pack()

        info = tk.Label(self.mainpage, text='Bilibili-Audio-Get')
        songbutton = tk.Button(self.mainpage, text='Download Single Song', command=self.download_song)
        listbutton = tk.Button(self.mainpage, text='Download Song List', command=self.download_list)

        info.pack(pady=10, side="top")
        songbutton.pack(padx=10, side="left")
        listbutton.pack(padx=10, side="right")

    def download_song(self):
        
        self.mainpage.destroy()
        SongPage(self.root)

    def download_list(self):

        self.mainpage.destroy()
        ListPage(self.root)

class SongPage:

    def __init__(self, root):
        self.root = root
        self.songpage = tk.Frame(self.root)
        self.songpage.pack()

        tip =tk.Label(self.songpage, text='Please type in song\'s ID:')
        self.song_id_box = tk.Entry(self.songpage)
        surebutton = tk.Button(self.songpage, text='OK', command=self.download_song)
        backbutton = tk.Button(self.songpage, text='Back', command=self.backpage)

        tip.grid(column=0,row=0)
        self.song_id_box.grid(column=1, row=0)
        surebutton.grid(column=2, row=0)
        backbutton.grid(column=2,row=1)

    def download_song(self):
        info = tk.Label(self.songpage, text='Downloading...')
        success = tk.Label(self.songpage, text='Finish Download.')
        id = int(self.song_id_box.get())
        info.grid(column=0, row=1)
        ag.savesong(id)
        success.grid(column=0,row=2)

    def backpage(self):
        self.songpage.destroy()
        MainPage(self.root)
        
class ListPage:

    def __init__(self, root):
        self.root = root
        self.listpage = tk.Frame(self.root)
        self.listpage.pack()

        tip =tk.Label(self.listpage, text='Please type in song list\'s ID:')
        self.list_id_box = tk.Entry(self.listpage)
        surebutton = tk.Button(self.listpage, text='OK', command=self.download_list)
        backbutton = tk.Button(self.listpage, text='Back', command=self.backpage)

        tip.grid(column=0,row=0)
        self.list_id_box.grid(column=1, row=0)
        surebutton.grid(column=2, row=0)
        backbutton.grid(column=2,row=1)

    def download_list(self):
        info = tk.Label(self.listpage, text='Downloading...')
        success = tk.Label(self.listpage, text='Finish Download.')
        id = int(self.list_id_box.get())
        info.grid(column=0, row=1)
        ag.savelist(id)
        success.grid(column=0,row=2)

    def backpage(self):
        self.listpage.destroy()
        MainPage(self.root)