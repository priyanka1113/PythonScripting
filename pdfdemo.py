import PyPDF2
with open("dumy.pdf","rb") as file:
	print(file)
	reader=PyPDF2.PdfFileReader(file)
	print(reader.numPages)
	page1=reader.getPage(0)
	page1.rotateClockwise(180)
	print(reader.getPage(0))
	writer=PyPDF2.PdfFileWriter()
	writer.addPage(page1)
	with open("tilt.pdf",'wb') as new_file:
		writer.write(new_file)


