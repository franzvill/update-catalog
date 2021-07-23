#!/usr/bin/env python3

from PIL import Image
from os import listdir

source_folder = "supplier-data/images/"
dest_folder = "supplier-data/images/"
size = (600,400)
file_format = ".jpeg"


def change_image(file):
    with Image.open(source_folder + file) as im:
        edited = im.resize(size).convert("RGB")
        edited.save(dest_folder + file.replace(".tiff",".jpeg"))


files = listdir(source_folder)
for file in files:
    if file.endswith(".tiff"):
        change_image(file)


