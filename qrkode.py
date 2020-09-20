import pyqrcode
from tkinter import *
import tkinter.ttk as tk
from PIL import Image,ImageTk

win=Tk()
win.title("QR kod teyin etmek")
win.config(background="skyblue")
win.geometry("420x480")

def generate():
    text=entry1.get()
    qr=pyqrcode.create(text)
    file_name="Qr_kodum"
    save_path=r"C:\Users\Xanim\Desktop\ "
    name=save_path+file_name+".png"

    qr.png(name,scale=10)
    image=Image.open(name)
    image=image.resize((400,400),Image.ANTIALIAS)
    image=ImageTk.PhotoImage(image)
    win.imagelabel.config(image=image)
    win.imagelabel.photo=image

text=tk.Label(win,text="Linki daxil et :")
text.grid(row=0,column=0,padx=3,pady=3)

entry1=tk.Entry(win,width=40)
entry1.grid(row=0,column=1,padx=3,pady=3)

button=tk.Button(win,text="Yarat",command=generate)
button.grid(row=0,column=2,padx=3,pady=3)

show_qr=tk.Label(win,text="QR Kod :")
show_qr.grid(row=1,column=0,padx=3,pady=3)

win.imagelabel=tk.Label(win,background="skyblue")
win.imagelabel.grid(row=2,column=0,padx=3,pady=3,columnspan=3)

win.mainloop()

