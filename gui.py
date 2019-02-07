import tkinter as tk
from tkinter import *
import pyqrcode
import PIL.Image
import PIL.ImageTk
from PIL import Image
import threading
import time
import blockgen
import main
import sys


class guiCreate(Frame):

    globalX = 0
    globalY = 0

    def __init__(self, master, **kwargs):

        x = master.winfo_screenwidth()
        y = master.winfo_screenheight()

        self.globalX = x
        self.globalY = y

        Frame.__init__(self, master)
        self.recievingAdress = Listbox(self.master, width=int(x / 40), height=int(y / 22))
        self.recievingAdress.pack(side=tk.RIGHT)
        self.recievingAdress.place(x=x / 1.75, y=y / 10)

        self.recievingAdressAmount = Listbox(self.master, width=int(x / 60), height=int(y / 22))
        self.recievingAdressAmount.pack(side=tk.RIGHT)
        self.recievingAdressAmount.place(x=x / 1.35, y=y / 10)

        self.public_adressEntry = Entry(self.master, width=int(40))
        self.public_adressEntry.pack(side=tk.LEFT)
        self.public_adressEntry.place(x=x / 6, y=y / 1.25)

        self.master = master
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            x, y))

        self.master.overrideredirect(True)
        self.master.overrideredirect(False)
        self.master.attributes("-fullscreen", True)

        self.master.title("")

        self.sender_Label = Label(self.master, text="Sender")
        self.sender_Label.pack(side=tk.RIGHT)
        self.sender_Label.place(x=x / 1.75, y=y / 13)

        self.amount_Label = Label(self.master, text="Amount (ICX)")
        self.amount_Label.pack(side=tk.RIGHT)
        self.amount_Label.place(x=x / 1.35, y=y / 13)

        self.qr_input_button = Button(self.master, text = "Public Address" , command = self.create_Qr_Code)
        self.qr_input_button.pack(side=tk.LEFT)
        self.qr_input_button.place(x=x / 2.87, y=y / 1.25)

        self.createBannerImg()

        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        sys.exit(0)

    def createBannerImg(self):

        bannerImg = PIL.Image.open("/Users/adam/PycharmProjects/igotmemed/res/icon.jpg").convert("RGB")
        bannerPhoto = PIL.ImageTk.PhotoImage(bannerImg)

        label = Label(self.master, image=bannerPhoto)
        label.image = bannerPhoto # reference
        label.place(x=self.globalX / 18.5, y=self.globalY / 26)

    def create_Qr_Code(self):

        text = self.public_adressEntry.get()
        blockgen.iconBlockGen.transactionAddress = text #give the back-end functionality which address to monitor

        qr = pyqrcode.create(text)
        qr.png("text.png", scale=7)

        qrImg = PIL.Image.open("text.png")
        photo = PIL.ImageTk.PhotoImage(qrImg)

        label = Label(self.master, image=photo)
        label.image = photo #reference
        label.pack(side=tk.LEFT)
        label.place(x=self.globalX / 5.45, y=self.globalY / 2.05)


    def addPayment(self, _instance, index , address, amount):
        self.recievingAdress.insert(index, address)
        self.recievingAdressAmount.insert(index, amount)

#        root2 = Tk()

#        screenPopUpThrd = threading.Thread(target=screenPopup, args=(root2, _instance))
#        screenPopUpThrd.daemon = True
#        screenPopUpThrd.start()

class popUpScreen(Frame):

    displayAddress = ""
    displayAmount = 0

    def __init__(self, master, **kwargs):

        x = master.winfo_screenwidth()
        y = master.winfo_screenheight()

        Frame.__init__(self, master)

        self.master = master

        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            x, y))

        self.master.title("ICONHAWK")

        self.master.overrideredirect(True)
        self.master.overrideredirect(False)
        self.master.attributes("-fullscreen", True)

        self.master.configure(background="#00edff")

        self.canvas = Canvas(self.master, width=x, height=y, bg='#00edff', highlightthickness=0)
        self.canvas.create_text(x/2, y/3.9, fill="white", font=("/Users/adam/PycharmProjects/igotmemed/res/KeepCalm-Medium.ttf", 90),
                                text=("New Payment: " + str(blockgen.adressListAmount[main.listIndex]) + " ICX"))
        self.canvas.pack(side='top', expand=True)

        self.canvas.create_text(x/2, y/1.05, fill="white", font=("/Users/adam/PycharmProjects/igotmemed/res/KeepCalm-Medium.ttf", 25),
                                text=("Sender: " + str(blockgen.adressList[main.listIndex])))
        self.canvas.pack(side='top', expand=True)

    def getValues(self):
        print("Testing testing")
#        self.displayAddress = _address
#        self.displayAmount = _amount


def screenPopup(root2, _instance):

    _instance.guicreate()
    popup = popUpScreen(root2)
    popUpScreen.getValues(popup)
    root2.after(5000, lambda: root2.destroy())
    root2.mainloop()

def test():

    root = Tk()
    t = guiCreate(root)
    icxObject = blockgen.iconBlockGen()
    handlerThrd = threading.Thread(target=icxObject.startLoop, args=(t, object))
    handlerThrd.daemon = True
    handlerThrd.start()
    root.mainloop()