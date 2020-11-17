from pytube import YouTube
from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen
from io import BytesIO

root = Tk()
root.title("Youtube Downloader")
root.iconbitmap("iconfinder_play_alt_118620.ico")

def onClick():
    video = YouTube(url.get())

    raw_data = urlopen(video.thumbnail_url).read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((round(im.size[0]*0.15), round(im.size[1]*0.15)))

    thumb_img = ImageTk.PhotoImage(im)
    thumb = Label(image=thumb_img)
    thumb.image = thumb_img
    thumb.pack(anchor=W, padx=30, pady=5)

    video_label = Label(root, text=video.title)
    video_label.pack(anchor=W, padx=30, pady=5)


url_frame = LabelFrame(root, padx=10, pady=10)
url_frame.pack(padx=30, pady=20)

url_label = Label(url_frame, padx=10, anchor=W, text="URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url = Entry(url_frame, borderwidth=5, width=50)
url.grid(row=0, column=1, padx=10, pady=10)


button = Button(url_frame, text="Search", padx=10, command=onClick)
button.grid(row=0, column=3, padx=10, pady=10)



root.mainloop()