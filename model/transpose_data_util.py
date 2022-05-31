# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:10:26 2022

@author: 17096
"""

from PIL import Image
from PIL import ImageFilter
import os


# path of the folder containing the raw images
inPath ="D:/git/igvc-autonomous-navigation/Cam2BEV/data/zedcam_F/val/bev+occlusion"

# path of the folder that will contain the modified image
outPath ="D:/git/igvc-autonomous-navigation/Cam2BEV/data/zedcam_F/val/bev+occlusion+rotation"

for imagePath in os.listdir(inPath):
    # imagePath contains name of the image
    inputPath = os.path.join(inPath, imagePath)

    # inputPath contains the full directory name
    img = Image.open(inputPath)

    fullOutPath = os.path.join(outPath, imagePath)
    # fullOutPath contains the path of the output
    # image that needs to be generated
    img.transpose(Image.ROTATE_270).save(fullOutPath)
    #img.resize((512, 256), Image.NEAREST).save(fullOutPath)
