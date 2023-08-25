import os
import sys
from PIL import Image


#grab first and sec args
image_folder=sys.argv[1]
output_folder=sys.argv[2]

#check if dest folder exists if not create new one
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
#convert jpg files to png
for filename in os.listdir(image_folder):
	img=Image.open(f'{image_folder}{filename}')
	clean_file_name=os.path.splitext(filename)[0]
	print(clean_file_name)
	img.save(f'{output_folder}{filename}','png')
	print("all done!")	