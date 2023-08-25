import PyPDF2
import sys


inputs=sys.argv[1:]

def pdf_combiner(pdf_list):
	merger=PyPDF2.PdfFileMerger()
	for file in pdf_list:
		print(file)
		merger.append(file)
	merger.write('new.pdf')
	print("combined pdf generated!")

pdf_combiner(inputs)



