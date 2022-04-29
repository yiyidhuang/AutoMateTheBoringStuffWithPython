import win32com.client
import docx

wordFilename = 'E:/Workspace/project-python/AutoMateTheBoringStuffWithPython/ch15/demo.docx'
pdfFilename = 'E:/Workspace/project-python/AutoMateTheBoringStuffWithPython/ch15/demo.pdf'

doc = docx.Document()
# Code to create Word document goes here.
doc.save(wordFilename)

wdFormatPDF = 17    # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
