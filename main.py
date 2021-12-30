# The Main File with the main Source Code !!!!!!

from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
from pytube import YouTube


root = Tk() # Tkinter root
root.title("Youtube Video Downloader (By:Archer)") #Tkinter title
#root.geometry("900x500") #tkinter window Size


class app:
    def __init__(self, root):
        self.root = root

        #main page
        self.mainframe = self.create_frame(self.root)
        self.mainframe.pack()

        #-----------#
        titleframe = self.create_frame(self.mainframe) #title
        titleframe.pack()
        title_font = tkFont.Font(family="Segoe UI Black", size=30)
        title = Label(titleframe, text="Yt Video Downloader", font=title_font, fg="#383838")
        title.pack()



        #the loop
        self.root.mainloop()
    
    def create_frame(self, root):
        return Frame(root, highlightthickness=0, borderwidth=0)


if __name__ == '__main__':
    app(root)

    