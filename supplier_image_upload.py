#!/usr/bin/env python3
import requests
from os import listdir

url = "http://localhost/upload/"
source_folder = "supplier-data/images/" 

def upload_image(file):
    with open(file, "rb") as file:
        r = requests.post(url, files={'file':file})


images = listdir(source_folder)
for image in images:
    if image.endswith(".jpeg"):
        upload_image(source_folder + image)
