from PIL import Image, ImageDraw
degree_sign= u'\N{DEGREE SIGN}'

image3 = Image.open("/Volumes/LMF_Microscope/1-Data/2015/12_December/01_Images/Image3.tif")
image4 = Image.open("/Volumes/LMF_Microscope/1-Data/2015/12_December/01_Images/Image4.tif")
image5 = Image.open("/Volumes/LMF_Microscope/1-Data/2015/12_December/01_Images/Image5.tif")
image6 = Image.open("/Volumes/LMF_Microscope/1-Data/2015/12_December/01_Images/Image6.tif")
image7 = Image.open("/Volumes/LMF_Microscope/1-Data/2015/12_December/01_Images/Image7.tif")
image8 = Image.open("/Volumes/LMF_Microscope/1-Data/2015/12_December/01_Images/Image8.tif")
image9 = Image.open("/Volumes/LMF_Microscope/1-Data/2015/12_December/01_Images/Image9.tif")
image10 = Image.open("/Volumes/LMF_Microscope/1-Data/2015/12_December/01_Images/Image10.tif")

new_im = Image.new('RGBA', (250, 450), (255, 255, 255, 0))

image3.thumbnail((100, 100))
image4.thumbnail((100, 100))
image5.thumbnail((100, 100))
image6.thumbnail((100, 100))
image7.thumbnail((100, 100))
image8.thumbnail((100, 100))
image9.thumbnail((100, 100))
image10.thumbnail((100, 100))

new_im.paste(image3, (50, 50))
new_im.paste(image4, (150, 50))
new_im.paste(image9, (50, 150))
new_im.paste(image10, (150, 150))
new_im.paste(image5, (50, 250))
new_im.paste(image6, (150, 250))
new_im.paste(image7, (50, 350))
new_im.paste(image8, (150, 350))

draw = ImageDraw.Draw(new_im)
draw.text((20, 100),"0" + degree_sign,(0,0,0))
draw.text((20, 200),"90" + degree_sign,(0,0,0))
draw.text((20, 300),"180" + degree_sign,(0,0,0))
draw.text((20, 400),"270" + degree_sign,(0,0,0))
draw.text((100, 30),"s" ,(0,0,0))
draw.text((200, 30),"p" ,(0,0,0))

new_im.save('scatter_different_angles.png', optimize = 1)
new_im.show()
