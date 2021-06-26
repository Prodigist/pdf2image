import fitz
from tkinter import Tk
import os
import tkinter as tk
import tkinter.filedialog as fd
from tkinter.filedialog import askdirectory

docs=[]
directory=askdirectory(title='Select Folder')

def extracto(xRes,yRes,name):
##    Tk().withdraw()
        doc =fitz.open(name)
        for page in range(len(doc)):
            for image in doc.getPageImageList(page):
                xref = image[0]
                pix = fitz.Pixmap(doc, xref)     
                if(pix.height>60 and pix.width>60):                
                    pix.set_dpi(xRes, yRes)
                    if pix.n < 5:       
                        pix.writePNG("Page%s-%s.png" % (page, xref))
                    else:               
                        pix1 = fitz.Pixmap(fitz.csRGB, pix)
                        pix1.writePNG("Page%s-%s.png" % (page, xref))
                        pix1 = None
                pix = None   


for file in os.listdir(directory):
    if file.endswith(".pdf"): 
        docs.append(os.path.join(directory, file))
for i in range(len(docs)):
    extracto(4800,4800,docs[i])            
            




