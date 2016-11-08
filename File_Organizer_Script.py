# -*- coding: utf-8 -*-
import os
import sys
import shutil


images_extensions = ["jpeg", "tiff", "bmp", "jpg", "png"]
#You can change the path below to your current Download's path 
#(or any path that you want to organize)
path = "C:\\Users\\luisdeolpy\\Downloads"
for filename in os.listdir(path):
	if (os.path.isdir(os.path.join(path,filename))):
		pass
	else:
		ext = filename.split(".")[-1]
		#I'm grouping all the images formats under the same unique label "images"
		if ext in images_extensions:
			if not (os.path.exists(os.path.join(path, "images"))):
				os.makedirs(os.path.join(path, "images"))
			shutil.move(os.path.join(path, filename), os.path.join(path, "images"))
		else:
			shutil.move(os.path.join(path, filename), os.path.join(path, ext))
			