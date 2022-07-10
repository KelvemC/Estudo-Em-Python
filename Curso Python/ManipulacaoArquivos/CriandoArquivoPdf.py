from html.entities import html5
import pydf

pdf = pydf.generate_pdf('<h1>Olá mundo</h1><p>Testando meu documento</p>')
with open('MeuPdf.pdf', 'wb') as file:
    file.write(pdf)

