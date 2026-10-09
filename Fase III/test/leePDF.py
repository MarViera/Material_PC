#Leer
from PyPDF2 import PdfFileReader

pdfFileObj = open('Manual2.pdf', 'rb')
pdf = PdfFileReader(pdfFileObj)
print("Páginas: ",pdf.getNumPages())
print("Título: ", pdf.documentInfo.title)
primera_hoja = pdf.getPage(16)
print(primera_hoja.extractText())
print(type(primera_hoja.extractText()))






