import youtube_dl as yt
from tkinter import *
import os

"""Global variable"""
file_type = ''
mp3_folder = os.path.join(os.getcwd(), "Audio")
mp4_folder = os.path.join(os.getcwd(), "Videos")

class Menu(object):
    """GUI for the program"""
    def __init__(self):
        self.options_menu = Tk()
        self.options_menu.geometry("350x150")
        self.checkvar = IntVar()

    def make_folders(self):
        if os.path.exists(mp3_folder): #check for Audio folder
            pass
        else:
            os.mkdir(mp3_folder)
        
        if os.path.exists(mp4_folder): #check for Videos folder
            pass
        else:
            os.mkdir(mp4_folder)


    def output(self):
        """Create GUI"""
        link = Entry(self.options_menu)
        link.pack()
        global status_text #Needs to be called after window is created
        status_text = StringVar()
        status_text.set('Would you link an Mp3 or Mp4?')
        radio_mp3 = Radiobutton(self.options_menu, text="MP3/Music", variable=self.checkvar, value=1, command = lambda: self.change_file_type('mp3')).pack()
        radio_mp4 = Radiobutton(self.options_menu, text="MP4/Video", variable=self.checkvar, value=2, command = lambda: self.change_file_type('mp4')).pack()
        download_button = Button(self.options_menu, text="Download", command = lambda: download_mp(link.get()))
        download_button.pack()
        status_gui = Label(self.options_menu, textvariable=status_text)
        status_gui.pack()
        self.options_menu.mainloop()


    def change_file_type(self, f_type):
        """Change variable to mp3 or mp4"""
        file_type = f_type
        status_text.set(f"Paste the link and click download for you {f_type}") 

def download_mp(video):
    """Download file and sort"""
    if file_type == 'mp3':
        os.chdir(mp3_folder)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
    else:
        os.chdir(mp4_folder)
        ydl_opts = {
        'format':'mp4',
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        }
    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video])      

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    """Status of download"""
    if d['status'] == 'finished':
            status_text.set(f'{file_type} downloaded')

youtube_mp3 = Menu()
youtube_mp3.make_folders()
youtube_mp3.output()


