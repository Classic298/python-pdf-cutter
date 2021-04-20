# Needs "pip install PyPDF2"
# Needs "pip install pyinstaller"
# PyInstaller -F ./Sourcefile.py

from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import os

def split(path, name_of_split):
    pdf = PdfFileReader(path)

    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(0))
    with open("./FirstPage/" + name_of_split, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == '__main__':
    try:
        os.mkdir("./FirstPage") 
    except:
        pass
    
    files = glob.glob("./*.pdf")
    
    for name in files:
        name = name.replace("./", "")
        print(name)
        split(name, name)