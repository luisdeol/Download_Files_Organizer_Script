# -*- coding: utf-8 -*-
import os
import sys
import shutil



path = "C:\\Users\\luisdeolpy\\Downloads"
for filename in os.listdir(path):
	if (os.path.isdir(os.path.join(path,filename))):
		pass
	else:
		ext = filename.split(".")[-1]
		if not (os.path.exists(os.path.join(path, ext))):
			os.makedirs(os.path.join(path, ext))
		else:
			print("dir already exists")
			shutil.move(os.path.join(path, filename), os.path.join(path, ext))
			