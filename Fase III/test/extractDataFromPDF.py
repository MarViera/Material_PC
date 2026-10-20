# -*- encoding: utf-8 -*-

from PyPDF2 import PdfFileReader, PdfFileWriter
import os 

def printMeta():
    ruta = input("Ruta de imágenes: ")
    # "C:\Users\marle\OneDrive\Documentos\GitHub\Material_PC\Fase III\test\pdf"
    os.chdir(ruta)
    ruta = os.getcwd()
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            ext = name.lower().rsplit('.', 1)[-1] #archivo.nombre.algo.pdf
            print(name.lower().rsplit('.', 1))
            if ext in ['pdf']:
                print("[+] Metadata for file: %s " %(ruta+os.path.sep+name))
                pdfFile = PdfFileReader(open(ruta+os.path.sep+name, 'rb'))
                docInfo = pdfFile.getDocumentInfo()
                print("Tipo: ", type(docInfo)) 
                for metaItem in docInfo:
                    print('[+] ' + metaItem + ':' + docInfo[metaItem])
                print("\n")
printMeta()
