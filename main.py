# The Main File with the main Source Code !!!!!!

from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import io
from pytube import YouTube
import threading
import time
from urllib.request import urlopen


root = Tk() # Tkinter root
root.title("Youtube Video Downloader (By:Archer)") #Tkinter title
#root.geometry("500x150") #tkinter window Size


class app:
    def __init__(self, root):
        self.root = root

        #main page
        self.frame = self.create_frame(self.root)
        self.frame.pack()

        self.mainframe = self.create_frame(self.frame)
        self.mainframe.grid(row=0, column=0)

        #-----------#
        titleframe = self.create_frame(self.mainframe) # title
        titleframe.pack()
        title_font = tkFont.Font(family="Segoe UI Black", size=30)
        title = Label(titleframe, text="Yt Video Downloader", font=title_font, fg="#383838", padx=20)
        title.pack()

        #-----------#
        self.searchframe = self.create_frame(self.mainframe) # Search
        self.searchframe.config(pady=25)
        self.searchframe.pack()

        entrytitle_font = tkFont.Font(family="Segoe UI", size=12) # Search Title
        entrytitle = Label(self.searchframe, text="Enter the URL: ", font=entrytitle_font, fg="#383838")
        entrytitle.grid(row=0, column=0)
        entry = Entry(self.searchframe, width=50, borderwidth=0)
        entry.grid(row=0, column=1, ipady=5, pady=15)


        searchbutton = Button(self.searchframe, fg='#ffffff', bg='#212121', text='Search', 
        command=lambda: threading.Thread(target=lambda: self.searching(entry.get())).start(),pady=10, padx=15) # Search Button
        searchbutton.grid(row=2, column=0, columnspan=2)

        # List of things to eliminate
        self.everything = []

        #the loop
        self.root.mainloop()
    
    def create_frame(self, root):
        return Frame(root, highlightthickness=0, borderwidth=0)

    def add(self, data):
        return self.everything.append(data)
    
    def get_resolution_list(self, data):
        lista = []
        for n in data:
            if n.resolution != None:
                if n.resolution not in lista:
                    lista.append(n.resolution)
        lista.sort()
        lista.sort(key=len)
        lista.insert(0, 'Audio')

        return lista

    def download(self, value):
        print('Suquecesso')
    
    def get_image(self, url):
        my_page = urlopen(url)
        my_picture = io.BytesIO(my_page.read())
        img = Image.open(my_picture)
        resized_image = img.resize((300,200), Image.ANTIALIAS)
        tk_img = ImageTk.PhotoImage(resized_image)
        return tk_img
    
    def searching(self, url):

        # Trying to Eliminate everything
        #-----------#
        try:
            for a in self.everything:
                a.destroy()
        except NameError:
            pass
        
        resultframe = self.create_frame(self.frame)
        resultframe.grid(row=0, column=1, padx=20, pady=5)

        # Searching the Video
        #-----------#

        try:
            # Progress Bar
            #-----------#
            search_text_font = tkFont.Font(family="Segoe UI", size=15)
            search_text = Label(resultframe, text="Searching...")
            self.add(search_text)
            search_text.pack()
            progressbar = ttk.Progressbar(resultframe, orient=HORIZONTAL, length=200, mode="indeterminate")
            self.add(progressbar)
            progressbar.pack()
            progressbar.start(20)
            self.yt = YouTube(url)
            self.thumb = self.get_image(self.yt.thumbnail_url)
            # Go get the list of Resolutions.
            self.streams = self.yt.streams
            self.resol_list = self.get_resolution_list(self.streams)
            
            
            print('Success')
            for a in self.everything:
                a.destroy()


        except Exception as e:
            messagetext = Label(self.searchframe, text='Insert a Valid URL')
            messagetext.grid(row=1, column=0, columnspan=2)
            try:
                for a in self.everything:
                    a.destroy()
            except NameError:
                pass
            self.add(messagetext)
            return False
        
        #-----------#
        rframe = LabelFrame(resultframe, text='Results: ')
        rframe.pack()
        self.add(rframe)
        
        yt_title_font = tkFont.Font(family='Segoe UI', size=10)
        yt_title = Label(rframe, text=f'Title: {self.yt.title}', font=yt_title_font)
        self.add(yt_title)
        yt_title.pack()

        yt_thumbnail = Label(rframe, image=self.thumb)
        self.add(yt_thumbnail)
        yt_thumbnail.pack()

        # Radio Buttons
        #-----------#
        rbframe = self.create_frame(rframe)
        self.add(rbframe)
        rbframe.pack()

        self.resol = IntVar()
        self.resol.set('0')
        
        for x, n in enumerate(self.resol_list):
            radio_buttons = Radiobutton(rbframe, text=n, variable=self.resol, value=x)
            radio_buttons.grid(column=(x), row=0, pady=10)
            self.add(radio_buttons)

        # Download Button

        download_button = Button(rframe, fg='#ffffff', bg='#212121', text='Search', 
        command=lambda: threading.Thread(target=lambda: self.download()).start(),
        pady=10, padx=15) # Search Button
        self.add(download_button)
        download_button.pack()

        
        





        

        


            


if __name__ == '__main__':
    app(root)

    

