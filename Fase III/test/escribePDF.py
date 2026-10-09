from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER

canvas = Canvas("hello.pdf", pagesize=LETTER)
canvas.drawString(72, 144, "Hello, World")
canvas.drawString(72, 72, "Bye, World")
canvas.save()
