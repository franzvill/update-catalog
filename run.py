#!/usr/bin/env python3

import os
import requests

folder = "supplier-data/descriptions/"
url = "http://34.133.37.67/fruits/"

def get_data(file):
    data = {}
    with open(folder + file) as f:
        data['name'] = f.readline().strip()
        data['weight'] = int(f.readline().replace("lbs","").strip())
        data['description'] = f.readlines()[0]
        data['image_name'] = file.replace(".txt", ".jpeg")

    return data


files = os.listdir(folder)
for file in files:
    if file.endswith(".txt"):
        data = get_data(file)
        res = requests.post(url, json=data)
        print(res.status_code)
