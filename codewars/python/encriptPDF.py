import PyPDF2
pdfFile = open('demo.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
           pdfWriter.addPage(pdfReader.getPage(pageNum))


pdfWriter.encrypt('Encription_password')
resultPdf = open('new_pdf_name.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()