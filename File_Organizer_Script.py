# -*- coding: utf-8 -*-
import os
import shutil


images_extensions = ["jpeg", "tiff", "bmp", "jpg", "png"]
path = "C:\\Users\\luisdeolpy\\Downloads"
for filename in os.listdir(path):
    if (os.path.isdir(os.path.join(path, filename))):
        pass
    else:
        ext = filename.split(".")[-1]
        if ext in images_extensions:
            if not (os.path.exists(os.path.join(path, "images"))):
                os.makedirs(os.path.join(path, "images"))
                shutil.move(os.path.join(path, filename),
                            os.path.join(path, "images"))
        elif not (os.path.exists(os.path.join(path, ext))):
            os.makedirs(os.path.join(path, ext))
            shutil.move(os.path.join(path, filename), os.path.join(path, ext))
        else:
            shutil.move(os.path.join(path, filename), os.path.join(path, ext))
