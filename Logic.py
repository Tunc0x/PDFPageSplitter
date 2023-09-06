from PyPDF2 import PdfFileReader, PdfFileWriter
import re
import os



def process_pdf(filepath):
    
    print(filepath)
    reader = PdfFileReader(filepath)
    numPages = reader.getNumPages()
    for pageNum in range(numPages):
        writer = PdfFileWriter()
        page = reader.getPage(pageNum)
        writer.addPage(page)
        output = f"page{pageNum}.pdf"
        with open(output, 'wb') as output_pdf:
            writer.write(output_pdf)

    



