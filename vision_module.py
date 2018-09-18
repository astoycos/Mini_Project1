# coding: utf-8

#export GOOGLE_APPLICATION_CREDENTIALS="/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/miniproject1-3785356094c8.json"

#https://stackoverflow.com/questions/6996603/delete-a-file-or-folder
#http://www.xappsoftware.com/wordpress/2013/04/25/how-to-add-a-text-to-a-picture-using-python/
#https://opensource.com/life/15/2/resize-images-python
#https://cloud.google.com/vision/docs/quickstart-client-libraries#client-libraries-usage-python
#https://pillow.readthedocs.io/en/3.0.x/reference/ImageDraw.html

import io
import os
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

picfiles = []

#makes sure none of the pictures are currupted and sorts them based on filename 
for filename in os.listdir('pic_downloads'):
	statinfo = os.stat('pic_downloads/' + filename)	
	if statinfo.st_size > 0:
		picfiles.append(filename)
	else:
		os.remove('pic_downloads/' + filename)

picfiles.sort(key = lambda f: int(filter(str.isdigit, f)))

#loops throgh pictures 
for pics in picfiles:

	# The name of the image file to annotate
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    'pic_downloads/' + pics)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)
		
	# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations	
	print(pics)

	#makes sure the API did respond with a label 
	if len(labels) > 1:
		print(labels[0].description)
			
		font = ImageFont.truetype('Crimson-BoldItalic.ttf',30)
		 
		# Opening the file gg.png
		imageFile = 'pic_downloads/' + pics
		im1=Image.open(imageFile)
		
		#resize image so that all images approximately match in video 
		basewidth = 600 
		wpercent = (basewidth / float(im1.size[0]))
		hsize = int((float(im1.size[1]) * float(wpercent)))
		im1 = im1.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
		
		try:		
			im1.save('pic_downloads/' + pics)
		except: 
			os.remove('pic_downloads/' + pics)

		# Drawing the text on the picture
		draw = ImageDraw.Draw(im1)
		draw.text((0,0),labels[0].description,fill = "red",font=font)
		draw = ImageDraw.Draw(im1)
		try:		
			im1.save('pic_downloads/' + pics)
		except: 
			os.remove('pic_downloads/' + pics)
	else:
		os.remove('pic_downloads/' + pics) 
		continue 


