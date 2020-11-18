from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from urllib.request import urlopen
from io import BytesIO
from threading import *


def onClickSearch():
    global video
    video = YouTube(url.get())

    raw_data = urlopen(video.thumbnail_url).read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((round(im.size[0] * 0.15), round(im.size[1] * 0.15)))

    thumb_img = ImageTk.PhotoImage(im)
    thumb = Label(image=thumb_img)
    thumb.image = thumb_img
    thumb.pack(anchor=W, padx=30, pady=5)

    video_label = Label(root, text=video.title)
    video_label.pack(anchor=W, padx=30, pady=5)


def btnClicked():
    try:
        downloadBtn["text"] = "Please Wait..."
        downloadBtn["state"] = "disabled"
        print(video)
        thread = Thread(target=startDownload, args=(url,))  # bloody comma is important
        thread.start()
    except Exception as e:
        print(e)


# Download Function
def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        st = video.streams.first()

        video.register_on_complete_callback(completeDownload)
        video.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)
    except Exception as e:
        print(e)
        downloadBtn["text"] = "Something went wrong"


def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = 100 * ((file_size - bytes_remaining) / file_size)
    downloadBtn["text"] = "{:00.0f}% downloaded ".format(percent)


def completeDownload(stream=None, file_path=None):
    print("Download completed")
    showinfo("Message", "File has been downloaded")
    downloadBtn["text"] = "Download Video"
    downloadBtn["state"] = "active"
    url.delete(0, END)


# GUI Coding
root = Tk()
root.title("Youtube Downloader")
root.iconbitmap("youtube-downloader-gui\iconfinder_play_alt_118620.ico")
root.geometry("700x500")

file = PhotoImage(file="youtube-downloader-gui/youtube-icon-vid.png")
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP, pady=3)

url_frame = LabelFrame(root, padx=10, pady=10)
url_frame.pack(padx=30, pady=20)

url_label = Label(url_frame, padx=10, anchor=W, text="URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url = Entry(url_frame, borderwidth=5, width=50)
url.grid(row=0, column=1, padx=10, pady=10)

button = Button(url_frame, text="Search", padx=10, command=onClickSearch)
button.grid(row=0, column=3, padx=10, pady=10)

downloadBtn = Button(root, text="Download Video", relief="ridge", command=btnClicked)
downloadBtn.pack(side=BOTTOM, pady=20)

root.mainloop()

# cool icon - Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Test video: https://www.youtube.com/watch?v=9XaS93WMRQQ