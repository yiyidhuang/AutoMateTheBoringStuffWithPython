#! python3
# combinepdfs.py - Combines all the PDFS in the current working directory into
# a singer PDF

import PyPDF2
import os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages(except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('E:/Workspace/project-python/AutoMateTheBoringStuffWithPython/ch15/allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
