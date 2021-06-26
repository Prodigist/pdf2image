import fitz
from tkinter import Tk
import os
from tkinter.filedialog import askopenfilename
##import tkinter as tk

xRes=6
yRes=6
name=askopenfilename()
tk().withdraw()
error=True

doc =fitz.open(name)

while (error):
    try:
        name=askopenfilename()
        doc =fitz.open(name)
        tk().withdraw() 
        print(name)
        error=False
    except :    
        print("Please select a pdf")
        error=True
        
  



##    cwd = os.getcwd()
##    if (not (os.path.exists(cwd+'/pythonFiles'))):
##        os.makedirs(cwd +'/pythonFiles')
    
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


