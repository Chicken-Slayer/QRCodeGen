import qrcode
from tkinter import *
from tkinter import ttk

# A simple graphical interface intended to make a QR code out of any given string, complete with advanced customisation options.

def makeQR(toConvert, outfile):
    img = qrcode.make(toConvert)
    type(img)
    img.save(outFile)
                    


