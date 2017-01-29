# -*- coding: utf-8 -*-
import os
import shutil
from winreg import *


with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

images_extensions = ["jpeg", "tiff", "bmp", "jpg", "png"]
image_path = os.path.join(path, "images")
for filename in os.listdir(path):
    print(filename)
    if (os.path.isdir(os.path.join(path, filename))):
        pass
    else:
        try:
            ext = filename.split(".")[-1]
            print (ext)
            if ext in images_extensions:
                if not (os.path.exists(image_path)):
                    os.makedirs(image_path)
                shutil.move(os.path.join(path, filename),
                                image_path)
            elif not (os.path.exists(os.path.join(path, ext))):
                os.makedirs(os.path.join(path, ext))
            shutil.move(os.path.join(path, filename), os.path.join(path, ext))
        except:
            pass
