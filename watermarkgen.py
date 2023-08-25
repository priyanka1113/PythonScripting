import PyPDF2

template=PyPDF2.PdfFileReader(open('new.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('thumbnailwtr.pdf','rb'))
output=PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page=template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)



with open('watermarked1.pdf','wb') as file:
	output.write(file)
