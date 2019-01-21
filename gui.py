import tkinter as tk
from tkinter import *
import pyqrcode
import PIL.Image
import PIL.ImageTk
import threading
import time
import blockgen
import main

class guiCreate(Frame):

    globalX = 0
    globalY = 0

    def __init__(self, master, **kwargs):

        pad = 3
        x = master.winfo_screenwidth() - pad
        y = master.winfo_screenheight() - pad

        self.globalX = x
        self.globalY = y

        Frame.__init__(self, master)
        self.recievingAdress = Listbox(self.master, width=int(x / 40), height=int(y / 24))
        self.recievingAdress.pack(side=tk.RIGHT)
        self.recievingAdress.place(x=x / 1.4, y=y / 10)

        self.recievingAdressAmount = Listbox(self.master, width=int(x / 80), height=int(y / 24))
        self.recievingAdressAmount.pack(side=tk.RIGHT)
        self.recievingAdressAmount.place(x=x / 1.1, y=y / 10)

        self.public_adressEntry = Entry(self.master, width=int(40))
        self.public_adressEntry.pack(side=tk.LEFT)
        self.public_adressEntry.place(x=x / 6, y=y / 1.5)

        #w = Canvas(master, width=x/4, height=y/2.2)
        #w.pack()

        #w.create_rectangle(x/22, y/2, x/4, y/4, fill="#d1d1d1")

        self.master = master
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            x, y))

        self.sender_Label = Label(self.master, text="Sender")
        self.sender_Label.pack(side=tk.RIGHT)
        self.sender_Label.place(x=x / 1.4, y=y / 13)

        self.amount_Label = Label(self.master, text="Amount                        (ICX)")
        self.amount_Label.pack(side=tk.RIGHT)
        self.amount_Label.place(x=x / 1.1, y=y / 13)

        self.qr_input_button = Button(self.master, text = "Public Address" , command = self.create_Qr_Code)
        self.qr_input_button.pack(side=tk.LEFT)
        self.qr_input_button.place(x=x / 2.87, y=y / 1.5)

    def create_Qr_Code(self):
        text = self.public_adressEntry.get()

        qr = pyqrcode.create(text)
        qr.png("text.png", scale=7)

        qrImg = PIL.Image.open("text.png")
        photo = PIL.ImageTk.PhotoImage(qrImg)

        label = Label(self.master, image=photo)
        label.image = photo
        label.pack(side=tk.LEFT)
        label.place(x=self.globalX / 5.45, y=self.globalY / 2.56)

    def addPayment(self, index , address, amount):

            self.recievingAdress.insert(index, address)
            self.recievingAdressAmount.insert(index, amount)
#
 #       if self.recievingAdress > 0:
  #          for i in range(0, self.recievingAdress.size()):
 #               self.recievingAdress.delete(i, tk.END)
 ##               self.recievingAdressAmount.delete(i, tk.END)

#        for i in blockgen.adressList:
 #           self.recievingAdress.insert(len(blockgen.adressList) - i, address)
 #           self.recievingAdressAmount.insert(len(blockgen.adressList) - i, amount)

#        listIndexBox = index - 1
#       self.recievingAdress.insert(listIndexBox, address)
#        self.recievingAdressAmount.insert(listIndexBox, amount)

def test():

    root = Tk()
    t = guiCreate(root)
    icxObject = blockgen.iconBlockGen()
    blockgen.iconBlockGen.getGuiInstance(object, t)
    handlerThrd = threading.Thread(target=icxObject.startLoop, args= (t, object))
    handlerThrd.start()
    root.mainloop()