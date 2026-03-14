import qrcode
from tkinter import *
from tkinter import ttk

# A simple graphical interface intended to make a QR code out of any given string, complete with advanced customisation options.

def makeQR(toConvert, outFile):
    img = qrcode.make(toConvert)
    type(img)
    img.save(outFile)

makeQR(input("enter: "), "outfile.png")

