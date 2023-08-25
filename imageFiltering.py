from PIL import Image,ImageFilter
img=Image.open('mypic.jpeg')
print(img.format)
print(img.size)
print(img.mode)
#print(dir(img))

filtered_img=img.filter(ImageFilter.BLUR)
filtered_img.save("blur.jpeg",'jpeg')
filtered_img=img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.jpeg",'jpeg')
convert_img=img.convert("L")
convert_img.save("grey.png",'png')
convert_img.show()
filtered_img=img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.jpeg",'jpeg')
crooked_img=img.rotate(90)
crooked_img.save("crooked.png",'png')
resize_img=img.resize((300,300))
resize_img.save("resized.png",'png')
box=(100,100,400,400)
cropped_img=img.crop(box)
cropped_img.save("cropped.png",'png')

img.thumbnail((400,200))
img.save("thumbnail.jpg")


#jpg to png convertor
